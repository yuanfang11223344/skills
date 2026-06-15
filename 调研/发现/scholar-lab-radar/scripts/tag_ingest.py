#!/usr/bin/env python3
"""Merge the LLM semantic layer into the ontology.

The skill fans out over papers and writes one tag record per paper to
``<lab>/tags.jsonl`` (the contract below). This script is the *deterministic* merge:
it adds Theme / Method / Dataset entities and explores / uses_method / evaluates_on
relations to the graph, derives Theme active-year spans, and emits the per-paper
Markdown cards. Run ``analyze.py`` afterwards to fold themes into the metrics/report.

tags.jsonl record (one JSON object per line):
    {"id": "W123",
     "themes":  [{"slug": "contrastive-ssl", "label": "Contrastive self-supervised learning"}],
     "methods": [{"slug": "transformer", "label": "Transformer", "aliases": ["self-attention"]}],
     "datasets":[{"slug": "imagenet", "label": "ImageNet"}],
     "summary": "one-line takeaway"}

Usage:  tag_ingest.py <lab_dir>
"""
from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict


def load_jsonl(path):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def slugify(text: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "untitled").lower()).strip("-")
    return s[:maxlen] or "untitled"


def ingest(lab_dir: str) -> dict:
    gdir = os.path.join(lab_dir, "graph")
    entities = {e["id"]: e for e in load_jsonl(os.path.join(gdir, "entities.jsonl"))}
    relations = list(load_jsonl(os.path.join(gdir, "relations.jsonl")))
    rel_keys = {(r["s"], r["p"], r["o"]) for r in relations}
    papers = {i: e for i, e in entities.items() if e["type"] == "Paper"}
    tags = {t["id"]: t for t in load_jsonl(os.path.join(lab_dir, "tags.jsonl"))}

    # paper -> topics, members (from existing structured relations)
    paper_topics = defaultdict(list)
    paper_members = defaultdict(list)
    for r in relations:
        if r["p"] == "has_topic" and r["o"] in entities:
            paper_topics[r["s"]].append(entities[r["o"]]["label"])
        elif r["p"] == "authored_by" and r["o"] in entities:
            au = entities[r["o"]]
            if au.get("role") in ("PI", "likely_member"):
                paper_members[r["s"]].append({"name": au.get("name"),
                                              "role": au.get("role"),
                                              "position": r.get("position")})

    theme_years = defaultdict(list)
    added = defaultdict(int)
    for wid, tag in tags.items():
        paper = papers.get(wid)
        yr = paper.get("year") if paper else None
        for kind, prefix, rel in (("themes", "theme", "explores"),
                                  ("methods", "method", "uses_method"),
                                  ("datasets", "dataset", "evaluates_on")):
            for item in tag.get(kind) or []:
                slug = item.get("slug") or slugify(item.get("label", ""))
                eid = f"{prefix}:{slug}"
                ent = entities.get(eid)
                if ent is None:
                    ent = {"id": eid, "type": prefix.capitalize(), "label": item.get("label"),
                           "derived_by": "llm"}
                    if item.get("aliases"):
                        ent["aliases"] = item["aliases"]
                    entities[eid] = ent
                    added[prefix.capitalize()] += 1
                elif item.get("aliases"):
                    ent.setdefault("aliases", [])
                    ent["aliases"] = sorted(set(ent["aliases"]) | set(item["aliases"]))
                key = (wid, rel, eid)
                if key not in rel_keys:
                    relations.append({"s": wid, "p": rel, "o": eid, "year": yr})
                    rel_keys.add(key)
                    added[rel] += 1
                if prefix == "theme" and yr:
                    theme_years[eid].append(yr)

    # theme active spans
    for eid, yrs in theme_years.items():
        entities[eid]["first_year"] = min(yrs)
        entities[eid]["last_year"] = max(yrs)

    with open(os.path.join(gdir, "entities.jsonl"), "w", encoding="utf-8") as fh:
        for e in entities.values():
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    with open(os.path.join(gdir, "relations.jsonl"), "w", encoding="utf-8") as fh:
        for r in relations:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # per-paper Markdown cards
    pdir = os.path.join(lab_dir, "papers")
    os.makedirs(pdir, exist_ok=True)
    n_cards = 0
    for wid, tag in tags.items():
        p = papers.get(wid)
        if not p:
            continue
        fm = {
            "id": wid, "title": p.get("title"), "year": p.get("year"),
            "venue": p.get("venue"), "doi": p.get("doi"), "citations": p.get("citations"),
            "oa_url": p.get("oa_url"), "pi_position": p.get("pi_position"),
            "topics": sorted(set(paper_topics.get(wid, []))),
            "themes": [t.get("label") for t in (tag.get("themes") or [])],
            "methods": [m.get("label") for m in (tag.get("methods") or [])],
            "datasets": [d.get("label") for d in (tag.get("datasets") or [])],
            "members": paper_members.get(wid, []),
            "summary": tag.get("summary"),
        }
        lines = ["---"]
        for k, v in fm.items():
            lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
        lines += ["---", "", f"# {p.get('title')}", "", tag.get("summary") or ""]
        fname = f"{p.get('year') or 'na'}-{slugify(p.get('title') or wid, 50)}.md"
        with open(os.path.join(pdir, fname), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        n_cards += 1

    summary = {"tagged_papers": len(tags), "cards": n_cards, "added": dict(added)}
    print(f"[tag_ingest] {len(tags)} tagged · {n_cards} cards · added {dict(added)}")
    return summary


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Merge LLM tags into the lab ontology.")
    p.add_argument("lab_dir")
    args = p.parse_args(argv)
    ingest(args.lab_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
