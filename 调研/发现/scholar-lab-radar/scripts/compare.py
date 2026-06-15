#!/usr/bin/env python3
"""Compare two profiled labs side by side (e.g. an applicant comparing advisors).

Both lab dirs must already be analyzed (have metrics.json + graph/entities.jsonl).
Emits a comparison report: productivity, shared vs distinctive topics/themes, each
lab's focus shift, and overlapping collaborators (by OpenAlex author id).

Usage:  compare.py <lab_a> <lab_b> [-o compare.md] [--name-a A] [--name-b B]
"""
from __future__ import annotations

import argparse
import json
import os


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def researchers(lab_dir):
    return {e["id"]: e for e in load_jsonl(os.path.join(lab_dir, "graph", "entities.jsonl"))
            if e.get("type") == "Researcher"}


def topic_set(m, key="top_topics", field="topic"):
    return {x[field] for x in (m.get(key) or [])}


def compare(lab_a, lab_b, out, name_a, name_b) -> str:
    ma, mb = load_json(os.path.join(lab_a, "metrics.json")), load_json(os.path.join(lab_b, "metrics.json"))
    na = name_a or ma.get("lab_dir") or os.path.basename(lab_a.rstrip("/"))
    nb = name_b or mb.get("lab_dir") or os.path.basename(lab_b.rstrip("/"))

    ta, tb = topic_set(ma), topic_set(mb)
    shared = sorted(ta & tb)
    only_a = sorted(ta - tb)
    only_b = sorted(tb - ta)

    ra, rb = researchers(lab_a), researchers(lab_b)
    pis = {i for r in (ra, rb) for i, e in r.items() if e.get("role") == "PI"}
    co_a = {i: e for i, e in ra.items() if i not in pis and e.get("role") != "external"}
    co_b = {i: e for i, e in rb.items() if i not in pis and e.get("role") != "external"}
    shared_collab = [(ra.get(i) or rb.get(i)).get("name") for i in (set(co_a) & set(co_b))]

    def row(m):
        t = m["totals"]
        sp = m["year_span"]
        return [t["papers"], f"{t['citations']:,}", t["likely_members"],
                f"{sp[0]}–{sp[1]}", t["topics"]]

    L = [f"# {na}  vs  {nb} — comparison", "",
         "| metric | " + na + " | " + nb + " |", "|---|---|---|"]
    headers = ["papers", "citations", "likely members", "span", "topics"]
    rva, rvb = row(ma), row(mb)
    for h, a, b in zip(headers, rva, rvb):
        L.append(f"| {h} | {a} | {b} |")
    L += ["", "## Shared research topics", "", (", ".join(shared) or "_none in the top lists_"), ""]
    L += [f"## Distinctive to {na}", "", (", ".join(only_a) or "_none_"), ""]
    L += [f"## Distinctive to {nb}", "", (", ".join(only_b) or "_none_"), ""]

    def emerging(m):
        return ", ".join(s["topic"] for s in (m.get("emerging_topics") or [])[:5]) or "_none_"
    L += ["## Focus shift (emerging topics)", "",
          f"- **{na}**: {emerging(ma)}", f"- **{nb}**: {emerging(mb)}", ""]
    L += ["## Overlapping people (shared non-PI collaborators)", "",
          (", ".join(sorted(c for c in shared_collab if c)) or "_no shared collaborators by OpenAlex id_"), ""]
    L += ["## Caveats", "",
          "- Topic/theme overlap is computed over each lab's *top* lists, not the full corpus.",
          "- Both labs must be collected over comparable year ranges for a fair comparison.",
          "- Shared collaborators are matched by OpenAlex author id (disambiguation applies).", ""]

    text = "\n".join(L) + "\n"
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"[compare] -> {out}")
    else:
        print(text)
    return text


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Compare two profiled labs.")
    p.add_argument("lab_a")
    p.add_argument("lab_b")
    p.add_argument("-o", "--out", default=None)
    p.add_argument("--name-a", default=None)
    p.add_argument("--name-b", default=None)
    args = p.parse_args(argv)
    compare(args.lab_a, args.lab_b, args.out, args.name_a, args.name_b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
