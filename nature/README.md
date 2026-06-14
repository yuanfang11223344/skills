# Nature Skills — 学术写作全流程 AI 工具箱

> 来源：[nature-skills](https://github.com/Yuan1z0825/nature-skills) (v1.0.0)
> 作者：袁一哲
> 协议：MIT

12 个 AI skill，覆盖从文献检索、论文精读、学术写作/润色、图表制作、引文管理，到审稿回复、PPT 汇报、专利申请的完整学术工作流。

---

## 架构

```
nature/
├── README.md          # 本文件
├── _shared/           # 跨 skill 共享规则（伦理、术语、论文分类、期刊格式）
│   ├── core/
│   │   ├── ethics.md                 # 学术伦理红线
│   │   ├── paper-type-taxonomy.md    # 论文类型分类体系
│   │   ├── reader-workflow.md        # 5 步审读问题链
│   │   └── terminology-ledger.md     # 术语一致性账本
│   └── journal-formats/
│       └── nat-comms.md              # Nature Communications 格式规范
│
├── nature-academic-search/    # ① 文献检索
├── nature-reader/             # ② 论文精读
├── nature-writing/            # ③ 论文写作
├── nature-polishing/          # ④ 论文润色/中译英
├── nature-citation/           # ⑤ 引文管理
├── nature-figure/             # ⑥ 学术图表
├── nature-data/               # ⑦ 数据声明
├── nature-reviewer/           # ⑧ 审稿模拟
├── nature-response/           # ⑨ 审稿回复
├── nature-paper2ppt/          # ⑩ 论文转PPT
└── nature-paper-to-patent/    # ⑪ 论文转专利
```

所有 skill 均为文件夹形式（含 `SKILL.md` + 配套 `static/`、`references/`、`manifest.yaml`），不可只复制单个 `SKILL.md`。

---

## Skill 一览

### ① nature-academic-search — 多源文献检索

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | CrossRef / PubMed / arXiv / Scopus / ScienceDirect 多源检索，MeSH 策略，.nbib/.ris/.bib 转换，参考文献管理 |
| 触发词 | 文献检索、引文验证、查找文献、搜索论文 |
| 输入 | 关键词、研究问题、MeSH 术语 |
| 输出 | 文献列表、BibTeX 导出、引文文件 |

### ② nature-reader — 论文精读/中英对照

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | 全文中英对照翻译，保留图表位置，每段带源锚点，生成结构化 Markdown reader |
| 触发词 | 读论文、论文翻译、精读、英文对照、全文翻译 |
| 输入 | PDF / DOI / arXiv / 出版商 HTML / 粘贴文本 |
| 输出 | 中英对照 Markdown（图表固定在原文位置） + 术语表 |

### ③ nature-writing — 从零起草 Nature 风格稿件

| 属性 | 值 |
|---|---|
| 版本 | 1.0.0 |
| 核心功能 | 从作者提供的论点/结果/图表/笔记/中文草稿出发，起草或重构摘要、引言、方法、实验、讨论、结论、标题 |
| 触发词 | 写论文、起草论文、搭论文框架、写引言/摘要/讨论、SCI 写作 |
| 输入 | 论文大纲、实验数据、结果描述、中文草稿 |
| 输出 | 各部分的结构化学术英文稿件 |

> 与 `nature-polishing` 的区别：writing 是「从零写」，polishing 是「改写/润色已有的」。

### ④ nature-polishing — 论文润色/中译英

| 属性 | 值 |
|---|---|
| 版本 | 6.1.0 |
| 核心功能 | 学术英文润色，中文→英文翻译，Nature 写作策略，Academic Phrasebank 支持，LaTeX 排版修复（跨页、浮动体、"Float too large"、补充材料空白页等） |
| 触发词 | 润色、改写、学术写作、中译英、论文润色、语言润色、英文写作 |
| 输入 | 英文学术段落 / 中文学术草稿 / LaTeX 源文件 |
| 输出 | 润色后的 Nature 风格英文稿件 |

> 版本 6.1，迭代最成熟的 skill。

### ⑤ nature-citation — Nature/CNS 引文管理

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | 将长段拆分为可引片段，仅检索 Nature Portfolio / AAAS Science / Cell Press 的可引期刊，按时间范围筛选，导出参考管理器格式 |
| 触发词 | 添加引文、引文格式、Nature 引用、参考文献 |
| 输入 | 稿件文本 |
| 输出 | 带段-引文映射的参考文献列表 |

### ⑥ nature-figure — 学术图表（Python/R）

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | 投稿级学术图表：matplotlib/seaborn (Python)，ggplot2/patchwork/ComplexHeatmap (R)，导出 SVG/PDF/TIFF |
| 触发词 | 科研绘图、论文配图、画图、作图、出图、论文图表、academic plotting |
| 输入 | 数据 + 图表需求 |
| 输出 | 出版格式图表 + QA 检查报告 |

> 不支持仪表盘或 Illustrator 修图。Python 或 R 二选一，不可混用。

### ⑦ nature-data — Data Availability 声明

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | 准备/审计/修订 Nature 级 Data Availability 声明、数据仓库计划、数据集引用、FAIR 元数据 |
| 触发词 | 数据可用性声明、Data Availability、FAIR 数据、数据仓库 |
| 输入 | 稿件信息、数据类型 |
| 输出 | 符合期刊要求的数据声明 |

### ⑧ nature-reviewer — Nature 风格审稿模拟

| 属性 | 值 |
|---|---|
| 版本 | 0.1.0 |
| 核心功能 | 从审稿人视角评估：新颖性/重要性/技术正确性，返回 3 份审稿报告 + 交叉综合 |
| 触发词 | 预审稿、审稿人视角、nature reviewer、peer review |
| 输入 | 完整稿件 |
| 输出 | 3 份审稿报告 + 综合评估 |

> 版本 0.1.0，仍在早期迭代。

### ⑨ nature-response — 审稿回复信

| 属性 | 值 |
|---|---|
| 版本 | 1.0.0 |
| 核心功能 | 起草/审计/修订逐点审稿回复信，Nature 系列期刊模板 |
| 触发词 | 审稿回复、逐点回复、修回信、大修/小修回复 |
| 输入 | 审稿意见 + 修订后的稿件 |
| 输出 | 逐点回复信 |

### ⑩ nature-paper2ppt — 论文 → 组会中文 PPT

| 属性 | 值 |
|---|---|
| 版本 | 2.0.0 |
| 核心功能 | 论文→Nature 风格中文 PPTX：识别论文类型和论证线，筛选必要图表，撰写中文幻灯片内容和演讲者备注，自检循环审查图表质量/文字溢出/排版 |
| 触发词 | 组会PPT、论文汇报、学术汇报、做幻灯片、讲paper、读书报告PPT |
| 输入 | 论文 PDF/文本/摘要/图注/阅读笔记 |
| 输出 | .pptx 文件 |

### ⑪ nature-paper-to-patent — 论文 → 中国发明专利

| 属性 | 值 |
|---|---|
| 版本 | - |
| 核心功能 | 论文/报告/源码 → 证据驱动的中国发明专利草案：提取可专利技术贡献，逐条映射到源证据，保留核心公式为可编辑 Office Math，生成与权利要求对齐的流程图和方法图，输出独立 DOCX（权利要求书 + 说明书 + 摘要 + 摘要附图） |
| 触发词 | 论文转专利、发明专利、专利草案 |
| 输入 | 论文/论文/源代码 |
| 输出 | 多个 .docx 文件（权利要求书、说明书、摘要、附图） |

---

## 共享资源 `_shared/`

| 文件 | 作用 | 使用者 |
|---|---|---|
| `core/ethics.md` | 学术伦理红线（不可突破的安全边界） | polishing, writing |
| `core/paper-type-taxonomy.md` | 论文类型分类体系 | polishing, writing |
| `core/reader-workflow.md` | 5 步审读问题链 | polishing, writing |
| `core/terminology-ledger.md` | 术语一致性账本规则 | polishing, writing, reader, paper2ppt |
| `journal-formats/nat-comms.md` | Nature Communications 格式规范 | polishing, writing |

---

## 典型工作流

```
文献检索                    论文精读                    产出
┌──────────────┐    ┌──────────────────┐
│ ac-search    │───→│ reader           │
│ 找文献/引文   │    │ 中英对照+图表定位  │
└──────────────┘    └──────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ writing  │  │polishing │  │citation  │
        │ 从零写作  │  │ 润色/翻译 │  │ 引文管理  │
        └──────────┘  └──────────┘  └──────────┘
              │              │              │
              └──────────────┼──────────────┘
                             ↓
              ┌─────────────────────────┐
              │ figure + data            │
              │ 图表制作 + 数据声明       │
              └─────────────────────────┘
                             │
                             ↓
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
        ┌──────────┐  ┌──────────┐  ┌──────────────┐
        │reviewer  │  │response  │  │paper2ppt     │
        │ 预审把关  │  │ 审稿回复  │  │ 组会PPT汇报  │
        └──────────┘  └──────────┘  └──────────────┘
                                           │
                                           ↓ (如需专利)
                                    ┌───────────────┐
                                    │paper-to-patent│
                                    │ 论文转专利     │
                                    └───────────────┘
```

---

## 版本成熟度

| 成熟度 | Skill |
|---|---|
| 高强度迭代 | `polishing` (6.1.0) |
| 中等迭代 | `figure` (2.0), `paper2ppt` (2.0), `reader` (2.0), `ac-search` (2.0), `citation` (2.0), `data` (2.0) |
| 稳定可用 | `writing` (1.0), `response` (1.0) |
| 早期开发 | `reviewer` (0.1.0), `paper-to-patent` (未标注) |

---

## 更新方式

```bash
cd /path/to/nature-skills && git pull
# 覆盖复制到 skills/nature/
cp -R skills/_shared /Users/ganxuanzhi/skills/nature/_shared
cp -R skills/nature-polishing /Users/ganxuanzhi/skills/nature/
# ... 其他更新的 skill
```

---

## 注意事项

1. **不可只复制 SKILL.md** — 每个 skill 依赖同目录的 `static/`、`references/`、`manifest.yaml` 等支撑文件
2. **路由型 skill 依赖 `_shared/`** — `polishing`、`writing`、`reader`、`paper2ppt` 等新版 skill 必须配合 `_shared/` 使用
3. **Python/R 二选一** — `figure` 不允许混用两个后端
4. **MIT 协议** — 可自由使用、修改、分发
