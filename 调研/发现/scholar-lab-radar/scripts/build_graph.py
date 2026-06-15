#!/usr/bin/env python3
"""Populate the temporal knowledge graph (ontology) from a collected corpus.

Reads ``<lab>/works.jsonl`` + ``<lab>/meta.json`` (the confirmed PI author ids) and
writes typed, time-stamped entities and relations. Everything here is derived from
OpenAlex's *structured* fields — no LLM, fully reproducible. The semantic layer
(Theme / Method / Dataset extraction) is added later by the skill.

Entities:  Paper · Researcher · Topic · Venue · Institution · Funder
Relations: authored_by · has_topic · published_in · funded_by · cites(internal) ·
           collaborates_with(PI ego, aggregated)

Usage:  build_graph.py <lab_dir>
Writes: <lab_dir>/graph/entities.jsonl , <lab_dir>/graph/relations.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def build(lab_dir: str) -> dict:
    meta = json.load(open(os.path.join(lab_dir, "meta.json"), encoding="utf-8"))
    pi = set(meta.get("authors") or [])
    works = list(load_jsonl(os.path.join(lab_dir, "works.jsonl")))
    corpus_ids = {w["id"] for w in works}

    entities: dict[str, dict] = {}
    relations: list[dict] = []
    rs: dict[str, dict] = defaultdict(lambda: {
        "name": None, "orcid": "", "papers": 0, "first_author": 0, "last_author": 0,
        "years": [], "insts": defaultdict(int)})

    for w in works:
        wid, yr = w["id"], w["year"]
        pi_pos = next((a["position"] for a in w["authorships"] if a["id"] in pi), None)
        entities[wid] = {
            "id": wid, "type": "Paper", "title": w["title"], "year": yr,
            "venue": (w["venue"] or {}).get("name"), "doi": w["doi"],
            "citations": w["citations"], "oa_status": (w["oa"] or {}).get("status"),
            "oa_url": (w["oa"] or {}).get("url"), "url": w["url"],
            "pi_position": pi_pos, "work_type": w["type"],
        }
        v = w["venue"] or {}
        if v.get("id"):
            entities.setdefault(v["id"], {"id": v["id"], "type": "Venue",
                                          "label": v.get("name"), "venue_type": v.get("type")})
            relations.append({"s": wid, "p": "published_in", "o": v["id"], "year": yr})
        for t in w["topics"]:
            if t.get("id"):
                entities.setdefault(t["id"], {"id": t["id"], "type": "Topic", "label": t["name"],
                                              "subfield": t.get("subfield"), "field": t.get("field"),
                                              "domain": t.get("domain")})
                relations.append({"s": wid, "p": "has_topic", "o": t["id"],
                                  "score": t.get("score"), "year": yr})
        for g in w["grants"]:
            if g.get("funder"):
                entities.setdefault(g["funder"], {"id": g["funder"], "type": "Funder",
                                                  "label": g.get("funder_name")})
                relations.append({"s": wid, "p": "funded_by", "o": g["funder"],
                                  "award_id": g.get("award_id"), "year": yr})
        coauthors = []
        for a in w["authorships"]:
            aid = a["id"]
            if not aid:
                continue
            coauthors.append(aid)
            st = rs[aid]
            st["name"] = a["name"] or st["name"]
            st["orcid"] = a["orcid"] or st["orcid"]
            st["papers"] += 1
            if yr:
                st["years"].append(yr)
            if a["position"] == "first":
                st["first_author"] += 1
            if a["position"] == "last":
                st["last_author"] += 1
            for inst in a["institutions"]:
                if inst.get("id"):
                    st["insts"][inst["id"]] += 1
                    entities.setdefault(inst["id"], {"id": inst["id"], "type": "Institution",
                                                     "label": inst.get("name"), "country": inst.get("country")})
            relations.append({"s": wid, "p": "authored_by", "o": aid,
                              "position": a["position"], "year": yr})
        for pid in pi & set(coauthors):
            for aid in coauthors:
                if aid != pid:
                    relations.append({"s": pid, "p": "collaborates_with", "o": aid, "year": yr})
        for ref in w["referenced_works"]:
            if ref in corpus_ids:
                relations.append({"s": wid, "p": "cites", "o": ref, "internal": True, "year": yr})

    pi_insts: set[str] = set()
    for pid in pi:
        pi_insts.update(rs[pid]["insts"].keys())
    for aid, st in rs.items():
        years = st["years"]
        first, last = (min(years), max(years)) if years else (None, None)
        home = max(st["insts"].items(), key=lambda x: x[1])[0] if st["insts"] else None
        shares = bool(set(st["insts"]) & pi_insts)
        if aid in pi:
            role = "PI"
        elif st["first_author"] >= 1 and (shares or (first and last and last - first <= 7)):
            role = "likely_member"
        elif st["papers"] >= 3:
            role = "long_term_collaborator"
        else:
            role = "external"
        entities[aid] = {
            "id": aid, "type": "Researcher", "name": st["name"], "orcid": st["orcid"],
            "role": role, "papers": st["papers"], "first_author_count": st["first_author"],
            "last_author_count": st["last_author"], "first_year": first, "last_year": last,
            "active_span": (last - first + 1 if first and last else None),
            "home_institution": home, "shares_pi_institution": shares,
        }

    # aggregate PI ego collaboration edges
    collab: dict[tuple, dict] = defaultdict(lambda: {"count": 0, "years": []})
    final_rel = []
    for r in relations:
        if r["p"] == "collaborates_with":
            k = (r["s"], r["o"])
            collab[k]["count"] += 1
            if r.get("year"):
                collab[k]["years"].append(r["year"])
        else:
            final_rel.append(r)
    for (s, o), v in collab.items():
        yrs = v["years"]
        final_rel.append({"s": s, "p": "collaborates_with", "o": o, "weight": v["count"],
                          "first_year": min(yrs) if yrs else None,
                          "last_year": max(yrs) if yrs else None})

    gdir = os.path.join(lab_dir, "graph")
    os.makedirs(gdir, exist_ok=True)
    with open(os.path.join(gdir, "entities.jsonl"), "w", encoding="utf-8") as fh:
        for e in entities.values():
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    with open(os.path.join(gdir, "relations.jsonl"), "w", encoding="utf-8") as fh:
        for r in final_rel:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_type: dict[str, int] = defaultdict(int)
    for e in entities.values():
        by_type[e["type"]] += 1
    rel_by_type: dict[str, int] = defaultdict(int)
    for r in final_rel:
        rel_by_type[r["p"]] += 1
    summary = {"entities": dict(by_type), "relations": dict(rel_by_type),
               "entity_total": len(entities), "relation_total": len(final_rel)}
    print(f"[graph] entities={summary['entity_total']} {dict(by_type)}", file=sys.stderr)
    print(f"[graph] relations={summary['relation_total']} {dict(rel_by_type)}", file=sys.stderr)
    return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build the lab knowledge graph.")
    p.add_argument("lab_dir")
    args = p.parse_args(argv)
    summary = build(args.lab_dir)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
