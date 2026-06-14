# Skills 索引

更新时间：2026-06-15

根目录：`/Users/ganxuanzhi/skills`
管理入口：[MANAGEMENT.md](MANAGEMENT.md) | [README.md](README.md)

## 总览

| Skill | 状态 | 主要用途 | 推荐触发 |
| --- | --- | --- | --- |
| `nature-academic-search` | Active | 多源文献检索、引文核对、参考文献管理 | 文献检索、查论文、引文核对、参考文献去重 |
| `nature-citation` | Active | 给论文段落自动补充 Nature/CNS/Cell 等支撑引用 | 加引用、补文献、支撑文献、RIS/EndNote |
| `nature-data` | Active | Data Availability、数据仓库、FAIR 元数据与数据引用 | 数据可用性、数据共享、代码可用性 |
| `nature-figure` | Active | 高水平期刊论文图表、Python/R 科研绘图与导出 QA | 论文配图、科研绘图、作图、可视化 |
| `nature-paper-to-patent` | Active | 科研论文、代码、图表转中国发明专利草案 | 论文转专利、权利要求、说明书、专利审查 |
| `nature-paper2ppt` | Active | 从论文生成中文组会、文献汇报、学术 PPTX | 论文做 PPT、组会 PPT、文献汇报 |
| `nature-polishing` | Active | Nature 风格英文润色、中译英、章节重构、LaTeX 排版 | 论文润色、学术英语、中译英、SCI 写作 |
| `nature-reader` | Active | 论文全文精读、中英对照、图表就位、源锚点 Markdown | 读论文、论文翻译、中英文对照、精读 |
| `nature-response` | Beta | 审稿意见逐点回复、rebuttal、修回信 | 审稿回复、大修、小修、回应 reviewer |
| `nature-reviewer` | Draft | 投稿前模拟 Nature 风格审稿和交叉评估 | 模拟审稿、预审、审稿人视角 |
| `nature-writing` | Active | 从 claims、结果和笔记起草或重构论文段落 | 写论文、起草摘要/引言/方法/讨论 |

## Markdown 入口目录

```text
/Users/ganxuanzhi/skills/README.md              ← 根目录规则说明
/Users/ganxuanzhi/skills/MANAGEMENT.md           ← 管理手册
/Users/ganxuanzhi/skills/INDEX.md                ← 本文件，索引
/Users/ganxuanzhi/skills/nature/README.md        ← nature 分类入口，11 个 skill 详细介绍
/Users/ganxuanzhi/skills/nature/nature-academic-search/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-citation/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-data/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-figure/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-paper-to-patent/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-paper2ppt/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-polishing/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-reader/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-response/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-reviewer/SKILL.md
/Users/ganxuanzhi/skills/nature/nature-writing/SKILL.md
```

## 调度建议

用户给出任务时，先判断任务阶段：

| 阶段 | 首选 skill | 可联动 skill |
| --- | --- | --- |
| 找资料 | `nature-academic-search` | `nature-citation` |
| 读论文 | `nature-reader` | `nature-academic-search` |
| 写初稿 | `nature-writing` | `nature-citation`, `nature-data` |
| 润色与中译英 | `nature-polishing` | `nature-citation` |
| 补引用 | `nature-citation` | `nature-academic-search` |
| 做图 | `nature-figure` | `nature-data` |
| 做汇报 | `nature-paper2ppt` | `nature-reader`, `nature-figure` |
| 回审稿人 | `nature-response` | `nature-polishing`, `nature-citation` |
| 投稿前自审 | `nature-reviewer` | `nature-writing`, `nature-polishing` |
| 转专利 | `nature-paper-to-patent` | `nature-reader` |

## 维护命令

列出当前 skill：

```bash
/Users/ganxuanzhi/skills/_management/scripts/list-skills.sh
```

检查 Git 状态：

```bash
git -C /Users/ganxuanzhi/skills status --short
```
