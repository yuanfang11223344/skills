# Data sources

All free, no key required. **OpenAlex** is the backbone (~90%): one cursor-paginated
sweep returns works with authorships, topics, citations, references, abstracts, OA, and
grants — enough to populate the whole structured ontology. The others fill gaps or enrich.

| Source | Role | Used by |
|---|---|---|
| **OpenAlex** | works · authors · institutions · topics · sources · funders · citations · abstracts | `resolve.py`, `collect.py` (primary) |
| **ORCID** | author disambiguation (the cleanest key) | `resolve.py --orcid` → OpenAlex `filter=orcid:` |
| **ROR** | institution normalization | via OpenAlex institution ids |
| Semantic Scholar / Crossref | abstract / metadata backfill, TLDR | optional enrichment (session MCP) |
| Unpaywall | OA full-text PDF links | optional |
| OpenCitations | citation-edge backfill (lineage/influence) | optional |
| Papers With Code | code/dataset/leaderboard (method·dataset normalization) | optional, semantic layer |

## OpenAlex query reference (polite pool via `mailto`)

```
# resolve institution → institution id
GET /institutions?search=<school>

# resolve author (optionally scoped) → author id(s); prefer ORCID
GET /authors?search=<name>&filter=last_known_institutions.id:<inst>
GET /authors/orcid:<orcid>

# collect every work in range (cursor paging; full objects so `grants` is included)
GET /works?filter=author.id:<A1>|<A2>,from_publication_date:<Y1>-01-01,to_publication_date:<Y2>-12-31
         &per-page=200&cursor=*&mailto=<email>

# restrict to works produced while at an institution
   ...,authorships.institutions.id:<inst>
```

Notes:
- OpenAlex `select` does **not** whitelist `grants`; `collect.py` fetches full work objects.
- Cursor value `*` is fine URL-encoded (`%2A`); pass a contact email for the polite pool.
- Retry 429/5xx with backoff (`scripts/oa.py:get_json`). A very prolific PI → use a year
  range and/or `--max`.
- Data licensing: OpenAlex is **CC0**. Individual abstracts/records may carry their own
  upstream licenses; cite OpenAlex when you publish derived analysis.
