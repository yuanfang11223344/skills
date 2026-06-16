# 分析 — Markdown 友好型文档分析可视化

> 来源：SkillsMP + GitHub 精选
> 安装日期：2026-06-16
> 总计：17 个 skill

分析报告/文章/PDF，输出 Markdown 原生内嵌的可视化图表。从输入到理解到呈现，全链路 Markdown 友好。

---

## 架构

```
分析/
├── README.md
├── paper-reading/      # ① 论文结构化阅读（HTML/Markdown双模式+手绘SVG图）
├── paper-onion/        # ② 4层剥洋葱深度阅读（思维导图笔记卡）
├── pdf-analysis/       # ③ 通用PDF分析（报告/白皮书/电子书）
└── markdown-viewer/    # ④ Markdown原生内嵌图表（14个引擎）
    ├── vega/             # 数据图表（柱线散饼热力雷达词云）
    ├── infographic/      # 信息图（KPI/路线图/SWOT/漏斗）
    ├── canvas/           # 思维导图/概念图/知识图谱
    ├── uml/              # 14种UML + 9500+图标
    ├── cloud/            # 云架构（AWS/Azure/GCP）
    ├── network/          # 网络拓扑（Cisco/Citrix）
    ├── security/         # 安全架构（IAM/防火墙/加密）
    ├── archimate/        # 企业架构（ArchiMate）
    ├── bpmn/             # 业务流程（BPMN/EIP/价值流）
    ├── data-analytics/   # 数据管道（ETL/仓库/ML）
    ├── iot/              # IoT架构
    ├── mindmap/          # PlantUML思维导图
    ├── architecture/     # 系统架构HTML图
    └── infocard/         # 编辑型知识卡片
```

---

## 四阶段工作流

```
PDF/论文/报告
      │
      ▼
┌─────────────────┐
│ ① 输入分析       │  paper-reading (论文) / pdf-analysis (通用)
│ 提取关键信息      │  自动识别类型、提取图表、结构化输出
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ② 深度理解       │  paper-onion
│ 四层剥洋葱        │  30s扫描→5min骨架→20min深挖→10min内化
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ③ 可视化呈现     │  markdown-viewer (14引擎)
│ Markdown原生图表  │  Vega/Canvas/PlantUML/Infographic
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ④ 输出到 Obsidian│  所有图表写在 .md 文件内
│ 直接打开即看      │  无需外链图片/HTML/PNG
└─────────────────┘
```

---

## Skill 一览

### ① paper-reading — 论文结构化阅读 (230⭐)

| 属性 | 值 |
|---|---|
| 来源 | Mizoreww/awesome-claude-code-config |
| 核心功能 | 自动识别论文类型（实证/理论/综述/系统），提取图表（pymupdf4llm 200DPI），**手绘SVG架构图/流程图**，HTML/Markdown双模式输出，Andrew Ng 3视角评估框架 |
| 触发词 | read paper, summarize paper, analyze this paper, literature review |
| 输出 | Markdown（轻量快速）或 HTML+手绘SVG（视觉效果更好） |

### ② paper-onion — 4层剥洋葱阅读 (38⭐)

| 属性 | 值 |
|---|---|
| 来源 | didixuxu/didi-skills |
| 核心功能 | Layer 1(30s)：第一印象 / Layer 2(5min)：骨架映射（痛点→灵感→方案→证据）/ Layer 3(20min)：核心机制+隐藏假设 / Layer 4(10min)：内化连接+个人洞察 |
| 输出 | 手绘风格思维导图笔记卡（React artifact），纸张纹理背景+手写字体+箭头连接 |

### ③ pdf-analysis — 通用PDF分析

| 属性 | 值 |
|---|---|
| 来源 | az9713/cerebro |
| 核心功能 | 处理报告、白皮书、电子书、手册等非论文PDF。结构化Markdown输出，含摘要、关键点和数据提取 |
| 触发词 | analyze PDF, extract from PDF, summarize document |

### ④ markdown-viewer — Markdown原生内嵌图表（14引擎）

| 引擎 | 用途 | 格式 |
|---|---|---|
| `vega` | 柱/线/散点/热力/雷达/词云图表 | ```vega-lite |
| `infographic` | KPI卡片/路线图/SWOT/漏斗/组织图 | YAML模板 |
| `canvas` | 思维导图/概念图/知识图谱/规划板 | JSON Canvas |
| `uml` | 14种UML图+9500+图标 | PlantUML |
| `cloud` | AWS/Azure/GCP云架构 | PlantUML+图标 |
| `network` | 网络拓扑（Cisco/Citrix设备） | PlantUML+图标 |
| `security` | IAM/防火墙/加密/零信任 | PlantUML |
| `archimate` | 企业架构（ArchiMate） | PlantUML |
| `bpmn` | 业务流程（BPMN+EIP+价值流） | PlantUML |
| `data-analytics` | ETL/数据仓库/ML架构 | PlantUML |
| `iot` | 传感器/边缘计算/数字孪生 | PlantUML |
| `mindmap` | 原生思维导图 | PlantUML |
| `architecture` | 13布局×12风格系统架构图 | HTML |
| `infocard` | 13布局×14风格知识卡片 | HTML |

> 所有图表写在 Markdown 文件内部，在 Obsidian 等阅读器中直接渲染。无需 PNG 外链、无需 HTML 导出。

---

## 与其他分类的关系

| 分类 | 定位 |
|---|---|
| `调研/` | **发现**信息——搜索论文、监控动态、聚合资讯 |
| `分析/` | **理解**信息——阅读论文、分析报告、可视化呈现 |
| `nature/` | **学术写作**——写作、润色、审稿、引用 |

```
调研/ 发现 → 分析/ 理解消化 → nature/ 写作产出
```

---

## 注意事项

- markdown-viewer 为基础版本（GitHub SSL 连接问题），可通过 `npx skills add markdown-viewer/skills` 获取完整版
- paper-reading 的 HTML 模式需要 `pymupdf4llm` Python 库
- 所有 Markdown 图表在 Obsidian 中可能需要对应插件渲染（Vega/PlantUML/Mermaid）
