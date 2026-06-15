"""Shared OpenAlex helpers for scholar-lab-radar (stdlib only).

OpenAlex is free and needs no key. Passing a contact email puts requests in the
"polite pool" for higher, more stable rate limits. All network access goes through
``get_json`` which retries on 429/5xx with backoff.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

OPENALEX = "https://api.openalex.org"
USER_AGENT = "scholar-lab-radar/0.x (https://github.com/TaewoooPark/scholar-lab-radar)"


def get_json(path: str, params: dict | None = None, *, mailto: str | None = None,
             retries: int = 5, timeout: int = 60) -> dict:
    """GET an OpenAlex endpoint and return parsed JSON, retrying transient errors."""
    params = dict(params or {})
    if mailto:
        params.setdefault("mailto", mailto)
    url = path if path.startswith("http") else f"{OPENALEX}{path}"
    if params:
        url = f"{url}{'&' if '?' in url else '?'}{urllib.parse.urlencode(params)}"
    last_err: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:  # noqa: PERF203
            last_err = exc
            if exc.code in (429, 500, 502, 503, 504):
                time.sleep(min(2 ** attempt, 30))
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as exc:
            last_err = exc
            time.sleep(min(2 ** attempt, 30))
    raise RuntimeError(f"OpenAlex request failed after {retries} tries: {url}\n{last_err}")


def paginate(path: str, params: dict, *, mailto: str | None = None,
             per_page: int = 200, max_records: int | None = None):
    """Yield every result across an OpenAlex list endpoint via cursor paging."""
    cursor = "*"
    seen = 0
    while cursor:
        page_params = dict(params, **{"per-page": per_page, "cursor": cursor})
        data = get_json(path, page_params, mailto=mailto)
        results = data.get("results", [])
        for rec in results:
            yield rec
            seen += 1
            if max_records and seen >= max_records:
                return
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not results:
            break


def short_id(openalex_id: str | None) -> str:
    """``https://openalex.org/A123`` -> ``A123`` (filters accept the short key)."""
    if not openalex_id:
        return ""
    return openalex_id.rstrip("/").rsplit("/", 1)[-1]


def clean_orcid(orcid: str | None) -> str:
    """Normalize an ORCID to the bare ``0000-0000-0000-0000`` form."""
    if not orcid:
        return ""
    return orcid.rstrip("/").rsplit("/", 1)[-1].strip()


def reconstruct_abstract(inverted_index: dict | None) -> str:
    """Rebuild plain-text abstract from OpenAlex's abstract_inverted_index."""
    if not inverted_index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inverted_index.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(word for _, word in positions)
