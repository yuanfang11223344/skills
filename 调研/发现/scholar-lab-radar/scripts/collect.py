#!/usr/bin/env python3
"""Collect every work by the confirmed author(s) in a year range into a normalized
corpus. Pure OpenAlex (free, no key) — abstracts, topics, citations, authorships,
references, grants all arrive in one paginated sweep.

Usage:
    collect.py --author A5086198262 [--author A...] --from 2015 --to 2025 \
        -o labs/<slug> [--institution I123] [--mailto you@x] [--max 5000]

Writes:
    <out>/works.jsonl   one normalized work per line
    <out>/meta.json     run parameters + counts + year span
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from oa import paginate, reconstruct_abstract, short_id

# NB: OpenAlex `select` does not whitelist `grants`, so we fetch full work objects
# (which include grants, topics, authorships, references, abstract index, …).


def normalize(w: dict) -> dict:
    loc = w.get("primary_location") or {}
    src = loc.get("source") or {}
    oa = w.get("open_access") or {}
    authorships = []
    for a in w.get("authorships") or []:
        au = a.get("author") or {}
        insts = [{"id": short_id(i.get("id")), "name": i.get("display_name"),
                  "country": i.get("country_code")} for i in (a.get("institutions") or [])]
        authorships.append({
            "id": short_id(au.get("id")),
            "name": au.get("display_name"),
            "orcid": (au.get("orcid") or "").rstrip("/").rsplit("/", 1)[-1] if au.get("orcid") else "",
            "position": a.get("author_position"),
            "is_corresponding": a.get("is_corresponding", False),
            "institutions": insts,
        })
    topics = []
    for t in w.get("topics") or []:
        topics.append({
            "id": short_id(t.get("id")),
            "name": t.get("display_name"),
            "score": t.get("score"),
            "subfield": (t.get("subfield") or {}).get("display_name"),
            "field": (t.get("field") or {}).get("display_name"),
            "domain": (t.get("domain") or {}).get("display_name"),
        })
    grants = [{"funder": short_id(g.get("funder")), "funder_name": g.get("funder_display_name"),
               "award_id": g.get("award_id")} for g in (w.get("grants") or [])]
    return {
        "id": short_id(w.get("id")),
        "doi": (w.get("doi") or "").replace("https://doi.org/", "") or None,
        "title": w.get("title") or w.get("display_name"),
        "year": w.get("publication_year"),
        "date": w.get("publication_date"),
        "type": w.get("type"),
        "citations": w.get("cited_by_count", 0),
        "venue": {"id": short_id(src.get("id")), "name": src.get("display_name"),
                  "type": src.get("type")},
        "oa": {"status": oa.get("oa_status"), "url": oa.get("oa_url")},
        "url": loc.get("landing_page_url") or (("https://doi.org/" + w["doi"].replace("https://doi.org/", "")) if w.get("doi") else None),
        "authorships": authorships,
        "topics": topics,
        "referenced_works": [short_id(r) for r in (w.get("referenced_works") or [])],
        "grants": grants,
        "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
    }


def collect(authors: list[str], y_from: int, y_to: int, out: str,
            institution: str | None, mailto: str | None, cap: int | None) -> dict:
    flt = [f"author.id:{'|'.join(authors)}",
           f"from_publication_date:{y_from}-01-01",
           f"to_publication_date:{y_to}-12-31"]
    if institution:
        flt.append(f"authorships.institutions.id:{institution}")
    params = {"filter": ",".join(flt)}

    os.makedirs(out, exist_ok=True)
    seen_doi: set[str] = set()
    seen_title: set[str] = set()
    seen_id: set[str] = set()
    n_raw = n_kept = 0
    years: list[int] = []
    path = os.path.join(out, "works.jsonl")
    with open(path, "w", encoding="utf-8") as fh:
        for w in paginate("/works", params, mailto=mailto, max_records=cap):
            n_raw += 1
            rec = normalize(w)
            key_doi = (rec["doi"] or "").lower()
            key_title = "".join(ch for ch in (rec["title"] or "").lower() if ch.isalnum())
            if rec["id"] in seen_id or (key_doi and key_doi in seen_doi) or \
               (key_title and key_title in seen_title):
                continue
            seen_id.add(rec["id"])
            if key_doi:
                seen_doi.add(key_doi)
            if key_title:
                seen_title.add(key_title)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n_kept += 1
            if rec["year"]:
                years.append(rec["year"])

    meta = {
        "authors": authors,
        "institution": institution,
        "year_from": y_from,
        "year_to": y_to,
        "raw_count": n_raw,
        "unique_count": n_kept,
        "year_span": [min(years), max(years)] if years else None,
        "works_file": "works.jsonl",
    }
    with open(os.path.join(out, "meta.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)
    print(f"[collect] {n_kept} unique works (from {n_raw} raw) "
          f"{meta['year_span']} -> {path}", file=sys.stderr)
    return meta


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Collect a lab's works from OpenAlex.")
    p.add_argument("--author", action="append", required=True,
                   help="OpenAlex author id (repeat to merge a split author)")
    p.add_argument("--from", dest="y_from", type=int, required=True)
    p.add_argument("--to", dest="y_to", type=int, required=True)
    p.add_argument("-o", "--out", required=True, help="output directory")
    p.add_argument("--institution", help="restrict to works affiliated with this institution id")
    p.add_argument("--mailto", default=None)
    p.add_argument("--max", dest="cap", type=int, default=None, help="hard cap on works")
    args = p.parse_args(argv)
    meta = collect([short_id(a) for a in args.author], args.y_from, args.y_to,
                   args.out, args.institution, args.mailto, args.cap)
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
