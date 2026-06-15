#!/usr/bin/env python3
"""Export the lab knowledge graph to JSON-LD for external/graph tooling.

Reads graph/{entities,relations}.jsonl and writes graph/ontology.jsonld: each entity
becomes a node ({@id, @type, attrs}) and each relation is embedded on its subject as a
predicate property carrying the object id plus the relation's attributes (year, weight,
score, confidence, …). The JSONL files remain the canonical, easy-to-grep form.

Usage:  export_jsonld.py <lab_dir>
"""
from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict

BASE = "https://openalex.org/"
VOCAB = "https://github.com/TaewoooPark/scholar-lab-radar/ns#"


def load_jsonl(path):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def export(lab_dir: str) -> str:
    gdir = os.path.join(lab_dir, "graph")
    nodes = {}
    for e in load_jsonl(os.path.join(gdir, "entities.jsonl")):
        node = {"@id": e["id"], "@type": e["type"]}
        for k, v in e.items():
            if k not in ("id", "type"):
                node[k] = v
        nodes[e["id"]] = node

    out_edges = defaultdict(lambda: defaultdict(list))
    for r in load_jsonl(os.path.join(gdir, "relations.jsonl")):
        s, p, o = r["s"], r["p"], r["o"]
        edge = {"@id": o}
        for k, v in r.items():
            if k not in ("s", "p", "o"):
                edge[k] = v
        out_edges[s][p].append(edge)

    for sid, preds in out_edges.items():
        node = nodes.setdefault(sid, {"@id": sid, "@type": "Unknown"})
        for p, edges in preds.items():
            node[p] = edges

    doc = {
        "@context": {
            "@base": BASE,
            "@vocab": VOCAB,
            "label": "http://www.w3.org/2000/01/rdf-schema#label",
        },
        "@graph": list(nodes.values()),
    }
    out_path = os.path.join(gdir, "ontology.jsonld")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
    print(f"[jsonld] {len(nodes)} nodes -> {out_path}")
    return out_path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Export the lab graph to JSON-LD.")
    p.add_argument("lab_dir")
    args = p.parse_args(argv)
    export(args.lab_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
