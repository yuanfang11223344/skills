#!/usr/bin/env python3
"""Compute metrics over the lab knowledge graph and emit a structured dashboard +
report. Deterministic (no LLM): every number is derived from the graph, so the
narrative the skill writes later can be grounded in `metrics.json` and never
invents trends. The LLM semantic layer (Themes/Methods, prose) is layered on top.

Usage:  analyze.py <lab_dir> [--top-topics 12] [--top-papers 15]
Writes: <lab_dir>/metrics.json
        <lab_dir>/data/{topics_by_year.csv, roster.csv}
        <lab_dir>/index.md          structured dashboard
        <lab_dir>/report.md         structured narrative (LLM-enriched in R2+)
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from collections import defaultdict


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def primary_topic(paper_topics: list[dict]):
    best = None
    for t in paper_topics:
        if t.get("id") and (best is None or (t.get("score") or 0) > (best.get("score") or 0)):
            best = t
    return best


def md_table(headers, rows) -> str:
    out = ["| " + " | ".join(str(h) for h in headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def _theme_view(lab_dir: str, years: list[int]) -> dict:
    """Theme × year view from the semantic layer (explores relations), if present."""
    gdir = os.path.join(lab_dir, "graph")
    ents = {e["id"]: e for e in load_jsonl(os.path.join(gdir, "entities.jsonl"))}
    themes = {i: e for i, e in ents.items() if e["type"] == "Theme"}
    if not themes:
        return {"has_themes": False}
    by_year = defaultdict(lambda: defaultdict(int))
    total = defaultdict(int)
    for r in load_jsonl(os.path.join(gdir, "relations.jsonl")):
        if r["p"] == "explores" and r["o"] in themes:
            total[r["o"]] += 1
            if r.get("year") is not None:
                by_year[r["o"]][r["year"]] += 1
    label = {i: (themes[i].get("label") or i) for i in themes}
    top = [t for t, _ in sorted(total.items(), key=lambda x: -x[1])[:12]]
    shift = []
    if years and years[-1] > years[0]:
        mid = (years[0] + years[-1]) / 2
        early_tot = sum(c for t in total for y, c in by_year[t].items() if y <= mid)
        late_tot = sum(c for t in total for y, c in by_year[t].items() if y > mid)
        for t in total:
            e = sum(c for y, c in by_year[t].items() if y <= mid)
            l = sum(c for y, c in by_year[t].items() if y > mid)
            es = e / early_tot if early_tot else 0
            ls = l / late_tot if late_tot else 0
            shift.append({"theme": label[t], "early": e, "late": l,
                          "early_share": round(es, 3), "late_share": round(ls, 3),
                          "delta": round(ls - es, 3)})
        shift.sort(key=lambda x: x["delta"])
    os.makedirs(os.path.join(lab_dir, "data"), exist_ok=True)
    with open(os.path.join(lab_dir, "data", "themes_by_year.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["theme"] + [str(y) for y in years] + ["total"])
        for t in top:
            w.writerow([label[t]] + [by_year[t].get(y, 0) for y in years] + [total[t]])
    return {
        "has_themes": True,
        "top_themes": [{"theme": label[t], "papers": total[t]} for t in top],
        "themes_by_year": {label[t]: {str(y): by_year[t].get(y, 0) for y in years} for t in top},
        "emerging": [s for s in reversed(shift) if s["delta"] > 0.02][:6],
        "declining": [s for s in shift if s["delta"] < -0.02][:6],
    }


def analyze(lab_dir: str, top_topics: int, top_papers: int) -> dict:
    meta = json.load(open(os.path.join(lab_dir, "meta.json"), encoding="utf-8"))
    pi_ids = set(meta.get("authors") or [])
    works = list(load_jsonl(os.path.join(lab_dir, "works.jsonl")))
    ents = {e["id"]: e for e in load_jsonl(os.path.join(lab_dir, "graph", "entities.jsonl"))}
    researchers = {i: e for i, e in ents.items() if e["type"] == "Researcher"}

    years = sorted({w["year"] for w in works if w["year"]})
    y_min, y_max = (years[0], years[-1]) if years else (None, None)

    papers_per_year = defaultdict(int)
    citations_per_year = defaultdict(int)
    oa_per_year = defaultdict(lambda: [0, 0])  # [oa, total]
    prim_topic_year = defaultdict(lambda: defaultdict(int))  # topic -> year -> count
    topic_total = defaultdict(int)
    topic_label = {}
    field_total = defaultdict(int)
    venue_total = defaultdict(int)
    for w in works:
        y = w["year"]
        papers_per_year[y] += 1
        citations_per_year[y] += w["citations"] or 0
        oa = w.get("oa") or {}
        is_oa = bool(oa.get("status") and oa.get("status") != "closed")
        oa_per_year[y][0] += 1 if is_oa else 0
        oa_per_year[y][1] += 1
        pt = primary_topic(w["topics"])
        if pt:
            prim_topic_year[pt["id"]][y] += 1
            topic_total[pt["id"]] += 1
            topic_label[pt["id"]] = pt["name"]
            if pt.get("field"):
                field_total[pt["field"]] += 1
        v = (w["venue"] or {}).get("name")
        if v:
            venue_total[v] += 1

    top_topic_ids = [tid for tid, _ in sorted(topic_total.items(), key=lambda x: -x[1])[:top_topics]]

    # focus shift: early vs late half of the year span (primary-topic share)
    shift = []
    if y_min is not None and y_max is not None and y_max > y_min:
        mid = (y_min + y_max) / 2
        early_tot = sum(1 for w in works if w["year"] and w["year"] <= mid)
        late_tot = sum(1 for w in works if w["year"] and w["year"] > mid)
        for tid in topic_total:
            e = sum(c for y, c in prim_topic_year[tid].items() if y <= mid)
            l = sum(c for y, c in prim_topic_year[tid].items() if y > mid)
            es = e / early_tot if early_tot else 0
            ls = l / late_tot if late_tot else 0
            shift.append({"topic": topic_label[tid], "early": e, "late": l,
                          "early_share": round(es, 3), "late_share": round(ls, 3),
                          "delta": round(ls - es, 3)})
        shift.sort(key=lambda x: x["delta"])
    emerging = [s for s in reversed(shift) if s["delta"] > 0.02][:6]
    declining = [s for s in shift if s["delta"] < -0.02][:6]

    # roster (members, sorted by role then papers)
    role_rank = {"PI": 0, "likely_member": 1, "long_term_collaborator": 2, "external": 3}
    roster = sorted(researchers.values(),
                    key=lambda r: (role_rank.get(r["role"], 9), -(r["papers"] or 0)))
    rising = [r for r in researchers.values()
              if r["role"] == "likely_member" and r.get("last_year")
              and y_max and r["last_year"] >= y_max - 1 and r["first_author_count"] >= 1]
    rising.sort(key=lambda r: -(r["first_author_count"] or 0))

    # collaboration growth: cumulative distinct co-authors over time
    first_seen = defaultdict(lambda: 9999)
    for r in researchers.values():
        if r["id"] not in pi_ids and r.get("first_year"):
            first_seen[r["id"]] = r["first_year"]
    new_collab_year = defaultdict(int)
    for _, fy in first_seen.items():
        new_collab_year[fy] += 1

    notable = sorted(works, key=lambda w: -(w["citations"] or 0))[:top_papers]

    metrics = {
        "lab_dir": os.path.basename(os.path.abspath(lab_dir)),
        "pi_ids": list(pi_ids),
        "year_span": [y_min, y_max],
        "totals": {
            "papers": len(works),
            "citations": sum(w["citations"] or 0 for w in works),
            "researchers": len(researchers),
            "likely_members": sum(1 for r in researchers.values() if r["role"] == "likely_member"),
            "topics": len(topic_total),
        },
        "papers_per_year": {str(y): papers_per_year[y] for y in years},
        "citations_per_year": {str(y): citations_per_year[y] for y in years},
        "oa_ratio_per_year": {str(y): round(oa_per_year[y][0] / oa_per_year[y][1], 3)
                              for y in years if oa_per_year[y][1]},
        "top_topics": [{"topic": topic_label[t], "papers": topic_total[t]} for t in top_topic_ids],
        "top_fields": sorted(({"field": f, "papers": c} for f, c in field_total.items()),
                             key=lambda x: -x["papers"])[:8],
        "emerging_topics": emerging,
        "declining_topics": declining,
        "new_collaborators_per_year": {str(y): new_collab_year[y] for y in years},
        "top_venues": sorted(({"venue": v, "papers": c} for v, c in venue_total.items()),
                             key=lambda x: -x["papers"])[:10],
        "rising_members": [{"name": r["name"], "first_author_count": r["first_author_count"],
                            "papers": r["papers"], "years": [r["first_year"], r["last_year"]]}
                           for r in rising[:8]],
        "notable_papers": [{"title": w["title"], "year": w["year"], "citations": w["citations"],
                            "doi": w["doi"], "venue": (w["venue"] or {}).get("name")}
                           for w in notable],
    }

    metrics["themes"] = _theme_view(lab_dir, years)

    os.makedirs(os.path.join(lab_dir, "data"), exist_ok=True)
    with open(os.path.join(lab_dir, "metrics.json"), "w", encoding="utf-8") as fh:
        json.dump(metrics, fh, ensure_ascii=False, indent=2)

    # topics_by_year.csv
    with open(os.path.join(lab_dir, "data", "topics_by_year.csv"), "w", newline="", encoding="utf-8") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(["topic"] + [str(y) for y in years] + ["total"])
        for tid in top_topic_ids:
            wcsv.writerow([topic_label[tid]] + [prim_topic_year[tid].get(y, 0) for y in years]
                          + [topic_total[tid]])
    # roster.csv
    with open(os.path.join(lab_dir, "data", "roster.csv"), "w", newline="", encoding="utf-8") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(["name", "role", "papers", "first_author", "last_author",
                       "first_year", "last_year", "orcid"])
        for r in roster:
            wcsv.writerow([r["name"], r["role"], r["papers"], r["first_author_count"],
                           r["last_author_count"], r["first_year"], r["last_year"], r["orcid"]])

    _write_index(lab_dir, metrics, years, top_topic_ids, topic_label, prim_topic_year, roster, pi_ids)
    _write_report(lab_dir, metrics)
    print(f"[analyze] {metrics['totals']['papers']} papers · "
          f"{metrics['totals']['researchers']} researchers · "
          f"{len(top_topic_ids)} top topics · span {y_min}-{y_max}")
    return metrics


def _write_index(lab_dir, m, years, top_topic_ids, topic_label, prim_topic_year, roster, pi_ids):
    lines = [f"# {m['lab_dir']} — dashboard", ""]
    t = m["totals"]
    lines += [f"**{t['papers']}** papers · **{t['citations']:,}** citations · "
              f"**{t['researchers']}** researchers ({t['likely_members']} likely members) · "
              f"span **{m['year_span'][0]}–{m['year_span'][1]}**", ""]
    lines += ["## Papers per year", "",
              md_table(["year"] + [str(y) for y in years],
                       [["papers"] + [m["papers_per_year"].get(str(y), 0) for y in years]]), ""]
    lines += ["## Topic × year (primary topic)", "",
              md_table(["topic"] + [str(y) for y in years],
                       [[topic_label[tid]] + [prim_topic_year[tid].get(y, 0) for y in years]
                        for tid in top_topic_ids]), ""]
    th = m.get("themes") or {}
    if th.get("has_themes"):
        tby = th["themes_by_year"]
        lines += ["## Theme × year (lab research threads)", "",
                  md_table(["theme"] + [str(y) for y in years],
                           [[name] + [tby[name].get(str(y), 0) for y in years] for name in tby]), ""]
    lines += ["## Roster (PI + likely members + long-term collaborators)", "",
              md_table(["name", "role", "papers", "1st-author", "active"],
                       [[r["name"], r["role"], r["papers"], r["first_author_count"],
                         f"{r['first_year']}–{r['last_year']}"]
                        for r in roster if r["role"] != "external"][:30]), ""]
    with open(os.path.join(lab_dir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def _write_report(lab_dir, m):
    t = m["totals"]
    sp = m["year_span"]
    L = [f"# {m['lab_dir']} — lab report", "",
         "> Structured draft from `metrics.json`. The skill enriches this with research "
         "themes, methods, and prose narrative; every claim stays grounded in the counts below.",
         "", "## Summary", "",
         f"- **{t['papers']}** papers ({sp[0]}–{sp[1]}), **{t['citations']:,}** total citations.",
         f"- **{t['researchers']}** distinct researchers; **{t['likely_members']}** likely lab members.",
         f"- **{len(m['top_topics'])}** active topics; top field: "
         f"{m['top_fields'][0]['field'] if m['top_fields'] else 'n/a'}.", ""]
    L += ["## Year-by-year output", "",
          md_table(["year", "papers", "citations(of that year's work)", "new collaborators"],
                   [[y, m["papers_per_year"][y], m["citations_per_year"][y],
                     m["new_collaborators_per_year"].get(y, 0)] for y in m["papers_per_year"]]), ""]
    L += ["## Focus shift (기조 변화)", "",
          "Primary-topic share, early half vs late half of the span (grounded in paper counts):", ""]
    if m["emerging_topics"]:
        L += ["**Emerging** (share ↑):", ""]
        L += [f"- {s['topic']}: {s['early_share']:.0%} → {s['late_share']:.0%} "
              f"({s['early']}→{s['late']} papers)" for s in m["emerging_topics"]]
        L += [""]
    if m["declining_topics"]:
        L += ["**Declining** (share ↓):", ""]
        L += [f"- {s['topic']}: {s['early_share']:.0%} → {s['late_share']:.0%} "
              f"({s['early']}→{s['late']} papers)" for s in m["declining_topics"]]
        L += [""]
    if not m["emerging_topics"] and not m["declining_topics"]:
        L += ["_No significant shift in primary-topic distribution over the span (or span too short)._", ""]
    L += ["## Top topics", "",
          md_table(["topic", "papers"], [[x["topic"], x["papers"]] for x in m["top_topics"]]), ""]
    th = m.get("themes") or {}
    if th.get("has_themes"):
        L += ["## Research themes (lab threads)", "",
              md_table(["theme", "papers"], [[x["theme"], x["papers"]] for x in th["top_themes"]]), ""]
        if th.get("emerging") or th.get("declining"):
            L += ["**Theme focus shift** (share, early half → late half):", ""]
            L += [f"- ↑ {s['theme']}: {s['early_share']:.0%} → {s['late_share']:.0%} "
                  f"({s['early']}→{s['late']} papers)" for s in th.get("emerging", [])]
            L += [f"- ↓ {s['theme']}: {s['early_share']:.0%} → {s['late_share']:.0%} "
                  f"({s['early']}→{s['late']} papers)" for s in th.get("declining", [])]
            L += [""]
    if m["rising_members"]:
        L += ["## Rising members (recent first-authors — likely current students/stars)", "",
              md_table(["name", "1st-author papers", "total", "active"],
                       [[r["name"], r["first_author_count"], r["papers"],
                         f"{r['years'][0]}–{r['years'][1]}"] for r in m["rising_members"]]), ""]
    L += ["## Notable / most-cited papers", ""]
    for p in m["notable_papers"]:
        doi = f" · doi:{p['doi']}" if p["doi"] else ""
        L += [f"- **{p['citations']:,}** · {p['year']} · {p['title']} ({p['venue']}){doi}"]
    L += ["", "## Caveats", "",
          "- Author disambiguation: corpus = the confirmed PI author id(s); a wrong id taints everything.",
          "- `likely_member` / `collaborator` roles are **inferred** from co-authorship + affiliation, not declared.",
          "- OpenAlex coverage varies (older work, some fields, non-English, books); abstracts can be missing.",
          "- Small per-year samples make trend claims noisy — counts are shown so they can be judged.", ""]
    with open(os.path.join(lab_dir, "report.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Analyze the lab graph into metrics + report.")
    p.add_argument("lab_dir")
    p.add_argument("--top-topics", type=int, default=12)
    p.add_argument("--top-papers", type=int, default=15)
    args = p.parse_args(argv)
    analyze(args.lab_dir, args.top_topics, args.top_papers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
