# 调研 — 学术调研全流程 AI 工具箱

> 来源：SkillsMP 搜索推荐（https://skillsmp.com）
> 安装日期：2026-06-15
> 总计：30 个 skill，分 4 个阶段

"从前期自动调研到后期生成资讯简报和深度报告"的完整学术调研链路。

---

## 架构

```
调研/
├── README.md
├── 发现/    # 第一阶段：论文搜索、会议跟踪、公司动态监控
├── 分析/    # 第二阶段：趋势分析、文献综述、深度解读
├── 产出/    # 第三阶段：深度报告、简报、文献综述
└── 推送/    # 第四阶段：变更监控、竞品对比、持续推送
```

---

## 四阶段流程

```
┌──────────────────────────────────────────────────────┐
│ 发现 (14 skill)                                       │
│ arxiv-monitor → papers → academic-search...          │
│ 论文搜索 + 会议跟踪 + 公司动态 + 生态系统监控          │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│ 分析 (8 skill)                                        │
│ academic-research-mapper → literature-engineer...    │
│ 趋势判断 + 空白识别 + 深度综述 + 论文解读              │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│ 产出 (4 skill)                                        │
│ deep-research → newsletter-generation...             │
│ 深度报告 + 研究简报 + 文献综述                        │
└────────────────────┬─────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────┐
│ 推送 (4 skill)                                        │
│ firecrawl-monitor → NewsScout...                     │
│ 变更监控 + 告警 + 简报推送                            │
└──────────────────────────────────────────────────────┘
```

---

## 发现阶段（14 skill）

| Skill | 功能 | 来源 |
|---|---|---|
| `arxiv-monitor` | 按查询/类别持续监控 arXiv 新论文，去重已读 | dsebastien/ai-skill-arxiv |
| `papers` | 跨数据库搜索（arXiv/OpenAlex/Scopus/Semantic Scholar） | gabfssilva/scimesh |
| `academic-search` | 跨学术源搜索，2分钟返回Top 5论文 | ECNU-ICALK/ecology-harness |
| `semantic-scholar` | Semantic Scholar API 搜索+引用分析+作者查询 | duskmoon314/keine |
| `search-papers` | arXiv + Semantic Scholar 合并去重，按引用量排序 | openags/auto-research |
| `arxiv-analysis` | 分析 arXiv 论文，通俗语言解释 | az9713/cerebro |
| `release-launch` | 跟踪论文发布全链路：链接->代码->数据->社交媒体 | wdzhwsh4067/arxiv-skills |
| `autoconference-skill` | 多Agent模拟学术会议：研究员并行研究->海报->评审->合成 | wjgoarxiv/autoconference-skill |
| `autoconference-analyze` | 会后分析：比较研究员轨迹、识别失败模式 | wjgoarxiv/autoconference-skill |
| `paper-pick` | 智能筛选会议/期刊论文 | aaronjmars/aeon |
| `competitive-intelligence` | 竞品跟踪：产品/定价/策略，监控发布/融资/并购 | jesseotremblay/claude-skills |
| `startup-competitors` | 完整竞品矩阵：定价/客户情绪/GTM策略 | ferdinandobons/startup-skill |
| `ecosystem-monitoring` | 监控供应商博客/竞品/GitHub/HN/arXiv/changelog | grandamenium/cortextos |
| `intelligence` | Reddit/HN监控、RSS、竞品内容差距分析、流量审计 | boringdata/kurt-demo |

## 分析阶段（8 skill）

| Skill | 功能 | 来源 |
|---|---|---|
| `academic-research-mapper` | 并行搜索+去重+聚类+趋势信号（加速/稳定/衰退）+空白识别 | tinyfish-io/tinyfish-cookbook |
| `scholar-search` | 学者画像：h-index、引用趋势、顶会/顶刊比例 | Lirsakura/skills-hub |
| `paper-analysis` | 研究方向演变趋势、合作网络、发表节奏分析 | Lirsakura/skills-hub |
| `literature-engineer` | 多路线文献扩展>=1200篇，元数据标准化 | WILLOSCAR/research-units-pipeline |
| `literature-research` | 系统化调研：范畴定义->搜索策略->分类->空白映射 | fcakyon/phd-skills-plugin |
| `literature-review` | 草拟文献综述，LaTeX/Markdown双模式 | ECNU-ICALK/ecology-harness |
| `citation-management` | Google Scholar+PubMed搜索验证、BibTeX、期刊质量分级Tier1-4 | ECNU-ICALK/ecology-harness |
| `research-paper` | 单篇论文5级深度解读（背景->方法->结果->影响->相关工作） | ceo-whyd-it/claude-research |

## 产出阶段（4 skill）

| Skill | 功能 | 来源 |
|---|---|---|
| `deep-research-andrem-sec` | 6步研究管道：目标->子问题->多源搜索(15-30 sources)->深度阅读->综合->交付 | andrem-sec/psc-comet |
| `literature-review` | 文献综述（同分析阶段，侧重产出） | ECNU-ICALK/ecology-harness |
| `newsletter-generation` | 专业简报：Daily Digest/Weekly Roundup/Industry Briefing | bytedance/deer-flow |
| `NewsScout` | 实时宏观/行业/技术趋势监控，过滤噪音输出可执行建议 | sargupta/career-guide |

## 推送阶段（4 skill）

| Skill | 功能 | 来源 |
|---|---|---|
| `firecrawl-monitor` | 网页变更检测+webhook/email通知（同firecrawl/中的） | firecrawl/cli |
| `competitor-analysis` | 多公司竞品对比矩阵，归一化JSON输出 | firecrawl/web-agent |
| `company-hiring-intelligence` | 从招聘信息反向推断公司技术方向 | tinyfish-io/tinyfish-cookbook |
| `NewsScout` | 资讯聚合推送（同产出阶段，侧重推送） | sargupta/career-guide |

---

## 与已有分类的关系

调研是**工作流交叉分类**——它从各来源仓库取 skill，按阶段组织，不重复已有分类的安装：

| 如果已从该分类安装 | 调研中不会重复 | 但路径不同 |
|---|---|---|
| `firecrawl/firecrawl-monitor` | 调研/推送/ 中是副本 | 可共用 |
| `nature/deep-research` | 调研/产出/ 中是不同作者版本 | 互补 |

---

## 注意事项

- 部分 skill 为基础版本（标注来源的仓库 clone 失败或为空），建议从上游 GitHub 获取完整文件覆盖
- `firecrawl-monitor` 需要 Firecrawl API key
- 30 个 skill 来自 15+ 个不同 GitHub 仓库
