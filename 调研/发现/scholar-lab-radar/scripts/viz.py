#!/usr/bin/env python3
"""Render the lab knowledge graph as a self-contained, interactive HTML you can open
in any browser:

- zoom / drag / hover, toggle node types, toggle edge labels
- **click any node** for a detail panel (attributes, DOI/links, summary, connections)
- **year slider + play** — drag (or press play) and nodes/edges *grow in year by year*,
  so you watch the lab's graph assemble over time (every relation is time-stamped)

Uses vis-network from a CDN — no install. The JSONL/JSON-LD remain the canonical data.

Usage:  viz.py <lab_dir> [-o <lab_dir>/graph.html] [--include-external] [--max-nodes 450]
"""
from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict

COLORS = {
    "Paper": "#4338ca", "Researcher": "#0891b2", "Theme": "#b91c1c",
    "Method": "#ea580c", "Topic": "#6b7280", "Venue": "#15803d",
    "Institution": "#a16207", "Funder": "#7c3aed", "Dataset": "#db2777",
}


def load_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def label_of(e):
    return e.get("name") or e.get("label") or e.get("title") or e["id"]


def _edge_year(r):
    y = r.get("year")
    if y is None:
        y = r.get("first_year")
    if y is None and r.get("year_range"):
        y = r["year_range"][0]
    return y


def build(lab_dir, out, include_external, max_nodes):
    gdir = os.path.join(lab_dir, "graph")
    ents = {e["id"]: e for e in load_jsonl(os.path.join(gdir, "entities.jsonl"))}
    rels = load_jsonl(os.path.join(gdir, "relations.jsonl"))
    summaries = {t["id"]: t.get("summary") for t in load_jsonl(os.path.join(lab_dir, "tags.jsonl"))}

    keep = {i for i, e in ents.items()
            if not (e["type"] == "Researcher" and e.get("role") == "external" and not include_external)}

    deg = defaultdict(int)
    kept = []
    for r in rels:
        if r["s"] in keep and r["o"] in keep:
            deg[r["s"]] += 1
            deg[r["o"]] += 1
            kept.append(r)

    ranked = sorted((i for i in keep if i in ents), key=lambda i: -deg.get(i, 0))
    if max_nodes and len(ranked) > max_nodes:
        ranked = ranked[:max_nodes]
    node_set = set(ranked)
    kept = [r for r in kept if r["s"] in node_set and r["o"] in node_set]

    # ---- year each node/edge first "appears" (for the time slider) ----
    node_years = defaultdict(list)
    edge_years = []
    for r in kept:
        y = _edge_year(r)
        edge_years.append(y)
        if y is not None:
            node_years[r["s"]].append(y)
            node_years[r["o"]].append(y)
    for i in node_set:
        e = ents[i]
        for k in ("year", "first_year"):
            if e.get(k):
                node_years[i].append(e[k])
    all_years = [y for ys in node_years.values() for y in ys]
    miny = min(all_years) if all_years else 2000
    maxy = max(all_years) if all_years else miny
    appear = {i: (min(node_years[i]) if node_years.get(i) else miny) for i in node_set}
    edge_years = [(y if y is not None else max(appear[r["s"]], appear[r["o"]]))
                  for y, r in zip(edge_years, kept)]

    nodes, details = [], {}
    for i in node_set:
        e = ents[i]
        t, lab = e["type"], label_of(e)
        short = lab if len(lab) <= 40 else lab[:38] + "…"
        title = f"{t}: {lab}"
        if t == "Paper" and e.get("year"):
            title += f" ({e['year']}, {e.get('citations', 0)} cites)"
        nodes.append({"id": i, "label": short, "title": title, "group": t,
                      "value": deg.get(i, 1), "color": COLORS.get(t, "#999"),
                      "shape": "dot", "appearYear": appear[i]})
        attrs = {}
        for k, v in e.items():
            if k in ("id", "type", "name", "label", "title") or v in (None, "", [], {}):
                continue
            if k == "home_institution" and v in ents:
                v = ents[v].get("label")
            attrs[k] = v
        if t == "Paper" and summaries.get(i):
            attrs["summary"] = summaries[i]
        details[i] = {"type": t, "label": lab, "attrs": attrs}

    vis_edges = [{"id": f"e{idx}", "from": r["s"], "to": r["o"], "label": r["p"],
                  "title": r["p"], "year": y}
                 for idx, (r, y) in enumerate(zip(kept, edge_years))]

    legend = "".join(
        f'<span style="display:inline-block;margin:0 10px 6px 0">'
        f'<span style="display:inline-block;width:11px;height:11px;border-radius:50%;'
        f'background:{c};margin-right:5px;vertical-align:middle"></span>{t}</span>'
        for t, c in COLORS.items())

    html = _TEMPLATE.format(
        title=os.path.basename(os.path.abspath(lab_dir)),
        n_nodes=len(nodes), n_edges=len(vis_edges), legend=legend,
        miny=miny, maxy=maxy,
        nodes=json.dumps(nodes, ensure_ascii=False),
        edges=json.dumps(vis_edges, ensure_ascii=False),
        details=json.dumps(details, ensure_ascii=False))
    out = out or os.path.join(lab_dir, "graph.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"[viz] {len(nodes)} nodes · {len(vis_edges)} edges · years {miny}-{maxy} -> {out}")
    print(f"[viz] open it: file://{os.path.abspath(out)}")
    return out


_TEMPLATE = """<!doctype html><html><head><meta charset="utf-8">
<title>scholar-lab-radar — {title}</title>
<script src="https://unpkg.com/vis-network@9.1.9/standalone/umd/vis-network.min.js"></script>
<style>
 *{{box-sizing:border-box}} body{{margin:0;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#111}}
 header{{padding:10px 16px;border-bottom:1px solid #e5e7eb}}
 h1{{font-size:16px;margin:0 0 4px}} .meta{{color:#6b7280;font-size:12px}}
 #legend{{padding:8px 16px;font-size:12px;border-bottom:1px solid #e5e7eb}}
 #legend label{{margin-right:12px;cursor:pointer;user-select:none}}
 #time{{padding:8px 16px;font-size:12px;border-bottom:1px solid #e5e7eb;display:flex;align-items:center;gap:10px}}
 #time input[type=range]{{flex:1;max-width:520px}} #yrlabel{{font-variant-numeric:tabular-nums}}
 #play{{border:1px solid #d4d4d8;background:#fff;border-radius:6px;padding:3px 10px;cursor:pointer;font-size:12px}}
 #wrap{{display:flex;height:calc(100vh - 170px)}}
 #net{{flex:1;min-width:0}}
 #panel{{width:340px;border-left:1px solid #e5e7eb;overflow:auto;padding:14px 16px;font-size:13px;line-height:1.5}}
 #panel .ptype{{display:inline-block;font-size:11px;font-weight:700;color:#fff;background:#111;border-radius:4px;padding:2px 7px}}
 #panel h2{{font-size:15px;margin:8px 0 10px}}
 #panel dl{{margin:0 0 10px;display:grid;grid-template-columns:auto 1fr;gap:2px 10px}}
 #panel dt{{color:#6b7280;font-weight:600}} #panel dd{{margin:0;word-break:break-word}}
 #panel h3{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:#6b7280;margin:12px 0 4px}}
 #panel .rel{{margin:3px 0}} #panel .pred{{display:inline-block;font-size:11px;background:#f1f5f9;border-radius:4px;padding:1px 6px;margin-right:4px}}
 #panel a{{color:#2563eb}} .hint{{color:#9ca3af}}
</style></head><body>
<header><h1>{title}</h1><div class="meta">{n_nodes} nodes · {n_edges} edges · scroll=zoom, drag=move, <b>click a node for details →</b></div></header>
<div id="legend">{legend}<br><span style="color:#6b7280">show edge labels
 <input type="checkbox" id="edgelabels"> · filter:</span> <span id="filters"></span></div>
<div id="time">📅 year ≤ <b id="yrlabel"></b>
 <input type="range" id="yr"> <button id="play">▶ play</button>
 <span class="meta">drag to grow the graph year by year</span></div>
<div id="wrap"><div id="net"></div><div id="panel"><div class="hint">Click a node to see its details.</div></div></div>
<script>
const allNodes={nodes};
const allEdges={edges};
const DETAILS={details};
const MINY={miny}, MAXY={maxy};
const NODES=new vis.DataSet([]);
const EDGES=new vis.DataSet([]);
const id2node={{}}; allNodes.forEach(n=>id2node[n.id]={{label:n.label,group:n.group}});
let sliderYear=MAXY, showLabels=false;
const state={{}}; [...new Set(allNodes.map(n=>n.group))].sort().forEach(t=>state[t]=true);
const net=new vis.Network(document.getElementById('net'),{{nodes:NODES,edges:EDGES}},{{
  nodes:{{scaling:{{min:6,max:42}},font:{{size:12}}}},
  edges:{{color:{{color:'#cbd5e1',highlight:'#475569'}},width:0.5,smooth:false,font:{{size:0,color:'#94a3b8'}},arrows:{{to:{{enabled:true,scaleFactor:0.4}}}}}},
  physics:{{solver:'forceAtlas2Based',forceAtlas2Based:{{gravitationalConstant:-45,springLength:90}},stabilization:{{iterations:150}}}},
  interaction:{{hover:true,tooltipDelay:120}}
}});
function render(){{
  const wantN=allNodes.filter(n=>state[n.group] && n.appearYear<=sliderYear);
  const wantNids=new Set(wantN.map(n=>n.id));
  const wantE=allEdges.filter(e=>e.year<=sliderYear && wantNids.has(e.from) && wantNids.has(e.to));
  const wantEids=new Set(wantE.map(e=>e.id));
  const curN=new Set(NODES.getIds()), curE=new Set(EDGES.getIds());
  NODES.remove([...curN].filter(id=>!wantNids.has(id)));
  NODES.add(wantN.filter(n=>!curN.has(n.id)));
  EDGES.remove([...curE].filter(id=>!wantEids.has(id)));
  EDGES.add(wantE.filter(e=>!curE.has(e.id)).map(e=>({{...e,font:{{size:showLabels?9:0}}}})));
}}
// edge labels
document.getElementById('edgelabels').onchange=ev=>{{showLabels=ev.target.checked;
  EDGES.forEach(e=>EDGES.update({{id:e.id,font:{{size:showLabels?9:0}}}}));}};
// type filters
const fdiv=document.getElementById('filters');
Object.keys(state).forEach(t=>{{
 const l=document.createElement('label');l.innerHTML=`<input type=checkbox checked> ${{t}}`;
 l.querySelector('input').onchange=ev=>{{state[t]=ev.target.checked;render();}};
 fdiv.appendChild(l);}});
// year slider
const yr=document.getElementById('yr'),yrlabel=document.getElementById('yrlabel');
yr.min=MINY;yr.max=MAXY;yr.value=MAXY;yr.step=1;yrlabel.textContent=MAXY;
yr.oninput=ev=>{{sliderYear=+ev.target.value;yrlabel.textContent=sliderYear;render();}};
// play
let timer=null;const play=document.getElementById('play');
play.onclick=()=>{{
  if(timer){{clearInterval(timer);timer=null;play.textContent='▶ play';return;}}
  sliderYear=MINY;yr.value=MINY;yrlabel.textContent=MINY;render();
  play.textContent='⏸ pause';
  timer=setInterval(()=>{{
    if(sliderYear>=MAXY){{clearInterval(timer);timer=null;play.textContent='▶ play';return;}}
    sliderYear++;yr.value=sliderYear;yrlabel.textContent=sliderYear;render();
  }},900);
}};
// detail panel
function esc(s){{return String(s).replace(/[&<>]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c]));}}
function grp(title,obj){{
  const keys=Object.keys(obj).sort(); if(!keys.length) return '';
  let s=`<h3>${{title}}</h3>`;
  for(const p of keys){{
    const items=obj[p].slice(0,25).map(id=>esc((id2node[id]||{{}}).label||id)).join(', ');
    s+=`<div class=rel><span class=pred>${{esc(p)}}</span>${{items}}${{obj[p].length>25?' …':''}}</div>`;}}
  return s;
}}
function showNode(id){{
  const d=DETAILS[id],panel=document.getElementById('panel');
  if(!d){{panel.innerHTML='<div class=hint>Click a node to see its details.</div>';return;}}
  let h=`<div class=ptype>${{esc(d.type)}}</div><h2>${{esc(d.label)}}</h2><dl>`;
  for(const [k,v] of Object.entries(d.attrs||{{}})){{
    let val;
    if(k==='doi') val=`<a href="https://doi.org/${{esc(v)}}" target=_blank>${{esc(v)}}</a>`;
    else if(k==='oa_url'||k==='url') val=`<a href="${{esc(v)}}" target=_blank>open</a>`;
    else if(k==='summary'){{h+=`</dl><div style="margin:0 0 10px">${{esc(v)}}</div><dl>`;continue;}}
    else val=esc(typeof v==='object'?JSON.stringify(v):v);
    h+=`<dt>${{esc(k)}}</dt><dd>${{val}}</dd>`;
  }}
  h+='</dl>';
  const outg={{}},inc={{}};
  EDGES.forEach(e=>{{ if(e.from===id)(outg[e.label]=outg[e.label]||[]).push(e.to);
                     if(e.to===id)(inc[e.label]=inc[e.label]||[]).push(e.from);}});
  h+=grp('Connections →',outg)+grp('← Referenced by',inc);
  panel.innerHTML=h;
}}
net.on('click',p=>{{ showNode(p.nodes&&p.nodes.length?p.nodes[0]:null); }});
render();
</script></body></html>"""


def main(argv=None):
    p = argparse.ArgumentParser(description="Render the lab graph as interactive HTML.")
    p.add_argument("lab_dir")
    p.add_argument("-o", "--out", default=None)
    p.add_argument("--include-external", action="store_true",
                   help="include one-off external co-authors (default: hidden)")
    p.add_argument("--max-nodes", type=int, default=450)
    args = p.parse_args(argv)
    build(args.lab_dir, args.out, args.include_external, args.max_nodes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
