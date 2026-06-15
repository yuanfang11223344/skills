# Ontology schema

scholar-lab-radar represents a lab as a **temporal knowledge graph**: typed entities and
typed, time-stamped relations. OpenAlex's 4-level Topic taxonomy is the *spine* (a
controlled vocabulary that prevents LLM topic drift); lab-specific **Themes**, **Methods**,
and **Datasets** are layered on top by the semantic step. Because every relation carries a
year, the graph is a time series — trends, lineage, and diffusion are graph queries.

Stored as JSON Lines: `graph/entities.jsonl` (one entity per line) and
`graph/relations.jsonl` (one relation per line). Optionally exported as `graph/ontology.jsonld`.

## Entities (nodes)

| type | key attributes |
|---|---|
| **Paper** | `id` (OpenAlex W…), `title`, `year`, `venue`, `doi`, `citations`, `oa_status`, `oa_url`, `url`, `pi_position` (first/middle/last/corresponding), `work_type` |
| **Researcher** | `id` (A…), `name`, `orcid`, `role` (PI \| likely_member \| long_term_collaborator \| external), `papers`, `first_author_count`, `last_author_count`, `first_year`, `last_year`, `active_span`, `home_institution`, `shares_pi_institution` |
| **Topic** | `id` (T…), `label`, `subfield`, `field`, `domain` *(OpenAlex taxonomy — the spine)* |
| **Theme** | `id` (`theme:slug`), `label`, `description`, `first_year`, `last_year`, `derived_by: llm` *(lab-specific research thread)* |
| **Method** / **Dataset** | `id` (`method:slug` / `dataset:slug`), `label`, `aliases`, `derived_by: llm`, `normalized: true` |
| **Venue** | `id` (S…), `label`, `venue_type` |
| **Institution** | `id` (I…), `label`, `country` |
| **Funder** | `id` (F…), `label` |

## Relations (typed, time-stamped)

| `p` | s → o | attributes |
|---|---|---|
| `authored_by` | Paper → Researcher | `position`, `year` |
| `has_topic` | Paper → Topic | `score`, `year` |
| `explores` | Paper → Theme | `year` *(semantic layer)* |
| `uses_method` | Paper → Method | `year` *(semantic)* |
| `evaluates_on` | Paper → Dataset | `year` *(semantic)* |
| `published_in` | Paper → Venue | `year` |
| `funded_by` | Paper → Funder | `award_id`, `year` |
| `cites` | Paper → Paper | `internal: true`, `year` *(only edges within the corpus — self-building lineage)* |
| `collaborates_with` | Researcher → Researcher | `weight`, `first_year`, `last_year` *(PI ego network, aggregated)* |
| `advised_by` | Researcher → Researcher | `confidence: inferred`, `evidence`, `year_range` *(semantic; never asserted as fact)* |
| `evolved_from` | Theme → Theme | `confidence` *(semantic; thread lineage)* |
| `diffused_to` | Method → Theme/Topic | `first_year` *(semantic; method migration)* |

## Examples

`entities.jsonl`:
```json
{"id":"A1969205032","type":"Researcher","name":"Jane Doe","orcid":"0000-0002-...","role":"PI","papers":84,"first_author_count":3,"first_year":2009,"last_year":2024,"active_span":16,"home_institution":"I123","shares_pi_institution":true}
{"id":"theme:contrastive-ssl","type":"Theme","label":"Contrastive self-supervised learning","first_year":2019,"last_year":2024,"derived_by":"llm"}
```
`relations.jsonl`:
```json
{"s":"W2741809807","p":"has_topic","o":"T10089","score":0.62,"year":2017}
{"s":"W2741809807","p":"explores","o":"theme:contrastive-ssl","year":2020}
{"s":"A_member7","p":"advised_by","o":"A1969205032","confidence":"inferred","evidence":"PI last-author + member first-author x6, same institution","year_range":[2018,2022]}
```

## Per-paper Markdown frontmatter (`papers/<year>-<slug>.md`)

```yaml
---
id: W2741809807
title: "Attention Is All You Need"
year: 2017
venue: NeurIPS
doi: 10.48550/arXiv.1706.03762
citations: 98000
oa_url: https://arxiv.org/abs/1706.03762
pi_position: last
topics: [Deep Learning, Machine Translation]        # OpenAlex taxonomy (spine)
themes: [attention-mechanisms, sequence-modeling]   # lab threads (LLM)
methods: [Transformer, self-attention]
datasets: [WMT14 En-De]
members: [{name: "A. Vaswani", role: likely_member, position: first}]
funders: [Google]
summary: "Sequence transduction with attention only — the Transformer."
---
```

## Roles (controlled enum) & inference

`PI` (the confirmed author id) · `likely_member` (first-authored ≥1 paper **and** shares the
PI's institution or has a short active span) · `long_term_collaborator` (≥3 papers, not a
member signal) · `external` (everyone else). These are **heuristics over co-authorship**,
not declared affiliations — always surfaced as inferred.
