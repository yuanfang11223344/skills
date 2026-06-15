#!/usr/bin/env python3
"""Append *structural* inferred relations to the ontology — derivable from the graph
alone, no LLM:

- ``advised_by``  : a likely-member who repeatedly first-authors papers where the PI is
                    last/corresponding author (and shares the PI's institution) is
                    inferred to be advised by that PI. Always tagged ``confidence:
                    inferred`` with the supporting evidence — never asserted as fact.
- ``diffused_to`` : when a Method (from the semantic layer) co-occurs with a Theme, the
                    earliest such year is the method's diffusion into that thread.

Usage:  infer.py <lab_dir> [--min-first-author 2]
"""
from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict


def load_jsonl(path):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def infer(lab_dir: str, min_first_author: int) -> dict:
    gdir = os.path.join(lab_dir, "graph")
    ents = {e["id"]: e for e in load_jsonl(os.path.join(gdir, "entities.jsonl"))}
    relations = list(load_jsonl(os.path.join(gdir, "relations.jsonl")))
    rel_keys = {(r["s"], r["p"], r["o"]) for r in relations}

    pis = {i for i, e in ents.items() if e.get("type") == "Researcher" and e.get("role") == "PI"}
    members = {i for i, e in ents.items() if e.get("type") == "Researcher" and e.get("role") == "likely_member"}

    # paper -> first/last authors, year
    first_of = defaultdict(set)
    last_of = defaultdict(set)
    paper_year = {}
    for r in relations:
        if r["p"] == "authored_by":
            if r.get("position") == "first":
                first_of[r["s"]].add(r["o"])
            elif r.get("position") == "last":
                last_of[r["s"]].add(r["o"])
            if r.get("year") is not None:
                paper_year[r["s"]] = r["year"]

    # advised_by: member first-author + PI last-author, recurring
    pair_years = defaultdict(list)
    for pid_paper, firsts in first_of.items():
        lasts = last_of.get(pid_paper, set())
        for m in firsts & members:
            for pi in lasts & pis:
                pair_years[(m, pi)].append(paper_year.get(pid_paper))
    added = defaultdict(int)
    for (m, pi), yrs in pair_years.items():
        yrs = [y for y in yrs if y is not None]
        if len(yrs) >= min_first_author and ents[m].get("shares_pi_institution"):
            key = (m, "advised_by", pi)
            if key not in rel_keys:
                relations.append({
                    "s": m, "p": "advised_by", "o": pi, "confidence": "inferred",
                    "evidence": f"first-authored {len(yrs)} papers with the PI as last author, "
                                f"shared institution",
                    "year_range": [min(yrs), max(yrs)],
                })
                rel_keys.add(key)
                added["advised_by"] += 1

    # method diffusion: Method -> Theme, earliest co-occurrence year
    explores = defaultdict(set)   # paper -> {theme}
    uses = defaultdict(set)       # paper -> {method}
    for r in relations:
        if r["p"] == "explores":
            explores[r["s"]].add(r["o"])
        elif r["p"] == "uses_method":
            uses[r["s"]].add(r["o"])
    diffusion = defaultdict(lambda: None)  # (method,theme) -> first_year
    for paper, methods in uses.items():
        themes = explores.get(paper, set())
        y = paper_year.get(paper)
        for mth in methods:
            for th in themes:
                cur = diffusion[(mth, th)]
                if y is not None and (cur is None or y < cur):
                    diffusion[(mth, th)] = y
    for (mth, th), y in diffusion.items():
        key = (mth, "diffused_to", th)
        if key not in rel_keys:
            relations.append({"s": mth, "p": "diffused_to", "o": th, "first_year": y})
            rel_keys.add(key)
            added["diffused_to"] += 1

    with open(os.path.join(gdir, "relations.jsonl"), "w", encoding="utf-8") as fh:
        for r in relations:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[infer] added {dict(added)}")
    return {"added": dict(added)}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Infer structural relations (advised_by, diffused_to).")
    p.add_argument("lab_dir")
    p.add_argument("--min-first-author", type=int, default=2)
    args = p.parse_args(argv)
    infer(args.lab_dir, args.min_first_author)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
