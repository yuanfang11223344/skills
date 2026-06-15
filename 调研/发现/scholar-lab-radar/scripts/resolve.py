#!/usr/bin/env python3
"""Resolve a lab to canonical OpenAlex entities — the make-or-break first step.

Author disambiguation decides whether the whole report is about the right person,
so this script only *proposes* candidates (with ORCID, institution, counts, recent
titles); a human confirms the id before collection runs.

Usage:
    resolve.py institution "Massachusetts Institute of Technology" [--mailto you@x]
    resolve.py author "Jane Doe" [--institution I123] [--orcid 0000-...] [--mailto you@x]

Prints a JSON object to stdout (machine-readable candidates) and a readable table
to stderr.
"""
from __future__ import annotations

import argparse
import json
import sys

from oa import clean_orcid, get_json, short_id


def _eprint(*a):
    print(*a, file=sys.stderr)


def _topics(entity: dict, k: int = 4) -> list[str]:
    return [t["display_name"] for t in (entity.get("topics") or [])[:k]]


def resolve_institution(name: str, mailto: str | None, limit: int = 8) -> dict:
    data = get_json("/institutions", {"search": name, "per-page": limit}, mailto=mailto)
    cands = []
    for inst in data.get("results", []):
        cands.append({
            "id": short_id(inst.get("id")),
            "name": inst.get("display_name"),
            "country": inst.get("country_code"),
            "type": inst.get("type"),
            "ror": inst.get("ror"),
            "works_count": inst.get("works_count"),
        })
    _eprint(f"\n# Institution candidates for {name!r}")
    for i, c in enumerate(cands):
        _eprint(f"  [{i}] {c['id']}  {c['name']}  ({c['country']}, {c['type']}, "
                f"{c['works_count']} works)")
    _eprint("Confirm the institution id, then run: resolve.py author ... --institution <id>")
    return {"query": name, "kind": "institution", "candidates": cands}


def _recent_titles(author_id: str, mailto: str | None, n: int = 3) -> list[str]:
    try:
        data = get_json("/works", {
            "filter": f"author.id:{author_id}",
            "sort": "publication_date:desc",
            "per-page": n,
            "select": "title,publication_year",
        }, mailto=mailto)
    except Exception:
        return []
    return [f"{w.get('publication_year','?')} · {w.get('title','')}"
            for w in data.get("results", [])]


def resolve_author(name: str, mailto: str | None, institution: str | None,
                   orcid: str | None, limit: int = 8) -> dict:
    if orcid:
        author = get_json(f"/authors/orcid:{clean_orcid(orcid)}", mailto=mailto)
        results = [author]
    else:
        params = {"search": name, "per-page": limit}
        if institution:
            params["filter"] = f"last_known_institutions.id:{institution}"
        data = get_json("/authors", params, mailto=mailto)
        results = data.get("results", [])
        # If an institution filter yielded nothing, retry on affiliations history.
        if institution and not results:
            params["filter"] = f"affiliations.institution.id:{institution}"
            results = get_json("/authors", params, mailto=mailto).get("results", [])

    cands = []
    for a in results[:limit]:
        aid = short_id(a.get("id"))
        last_inst = (a.get("last_known_institutions") or [{}])[0].get("display_name")
        cands.append({
            "id": aid,
            "name": a.get("display_name"),
            "orcid": clean_orcid(a.get("orcid")),
            "last_institution": last_inst,
            "works_count": a.get("works_count"),
            "cited_by_count": a.get("cited_by_count"),
            "top_topics": _topics(a),
            "recent_titles": _recent_titles(aid, mailto) if len(results) <= limit else [],
        })

    _eprint(f"\n# Author candidates for {name!r}"
            + (f" @ {institution}" if institution else "")
            + (f" (ORCID {clean_orcid(orcid)})" if orcid else ""))
    for i, c in enumerate(cands):
        _eprint(f"  [{i}] {c['id']}  {c['name']}  "
                f"ORCID={c['orcid'] or '—'}  {c['works_count']} works, "
                f"{c['cited_by_count']} cites")
        _eprint(f"      inst: {c['last_institution']}")
        if c["top_topics"]:
            _eprint(f"      topics: {', '.join(c['top_topics'])}")
        for t in c["recent_titles"]:
            _eprint(f"      • {t}")
    _eprint("\nConfirm the correct author id(s) (merge several if the person is split), "
            "then run: collect.py --author <id> [--author <id2>] --from <Y1> --to <Y2>")
    return {"query": name, "kind": "author", "institution": institution,
            "orcid": clean_orcid(orcid), "candidates": cands}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Resolve a lab to OpenAlex entities.")
    sub = p.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("institution")
    pi.add_argument("name")
    pa = sub.add_parser("author")
    pa.add_argument("name")
    pa.add_argument("--institution", help="OpenAlex institution id (e.g. I63966007)")
    pa.add_argument("--orcid", help="ORCID — the cleanest disambiguator")
    for sp in (pi, pa):
        sp.add_argument("--mailto", default=None, help="contact email for the polite pool")
        sp.add_argument("--limit", type=int, default=8)
    args = p.parse_args(argv)

    if args.cmd == "institution":
        out = resolve_institution(args.name, args.mailto, args.limit)
    else:
        out = resolve_author(args.name, args.mailto, args.institution, args.orcid, args.limit)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
