# academic-research — 学术研究全流程 AI 工具箱

> 来源：[academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
> 作者：Imbad0202
> 协议：见 LICENSE

4 个 AI skill，覆盖从深度研究、论文写作、审稿到全流程编排的学术研究完整工作流。

---

## 架构

```
academic-research/
├── README.md                  # 本文件
├── deep-research/             # 13-agent 深度研究
├── academic-paper/            # 12-agent 论文写作
├── academic-paper-reviewer/   # 5-reviewer 多视角审稿
└── academic-pipeline/         # 全流程编排（研究→写作→审稿→修订）
```

---

## Skill 一览

### deep-research — 深度研究

| 属性 | 值 |
|---|---|
| 版本 | 2.9.4 |
| 核心功能 | 13-agent 深度学习管道，7 种模式：完整研究/快速简报/论文评审/文献综述/事实核查/苏格拉底引导对话/系统综述+可选荟萃分析。覆盖研究问题制定、方法论设计、系统文献检索、来源验证、跨源综合、偏倚风险评估、APA 7.0 报告编译 |
| 触发词 | research, deep research, literature review, systematic review, meta-analysis, PRISMA, 研究, 深度研究, 文献回顾 |
| 输入 | 研究主题/问题 |
| 输出 | APA 7.0 研究报告 |

> 与 `nature-academic-search` 的区别：search 做文献检索和 BibTeX 管理；deep-research 做 13-agent 完整研究管道。

### academic-paper — 12-agent 论文写作

| 属性 | 值 |
|---|---|
| 版本 | 3.2.0 |
| 核心功能 | 12-agent 学术论文写作管道，10 种模式（全文/计划/大纲/修订/修订教练/摘要/文献综述/格式转换/引文检查/声明），6 种论文类型，5 种引文格式，双语摘要，LaTeX/DOCX/PDF 输出 |
| 触发词 | write paper, academic paper, guide my paper, AI disclosure, 写论文, 学术论文 |
| 输入 | 研究数据/大纲/草稿 |
| 输出 | LaTeX/DOCX/PDF 论文 |

> 与 `nature-writing` 的区别：nature-writing 从 claims 起草段落；academic-paper 用 12-agent 管道生成完整论文。

### academic-paper-reviewer — 多视角审稿

| 属性 | 值 |
|---|---|
| 版本 | 1.10.0 |
| 核心功能 | 5 个独立审稿人（EIC + 3 位同行评审 + Devil's Advocate），6 种模式：完整审稿/再审稿/快速评估/方法论焦点/苏格拉底引导/校准模式 |
| 触发词 | review paper, peer review, manuscript review, referee report, critique paper |
| 输入 | 完整稿件 |
| 输出 | 5 份独立审稿报告 + 综合评估 |

> 与 `nature-reviewer` (0.1.0 Draft) 相比，成熟度高得多。

### academic-pipeline — 全流程编排

| 属性 | 值 |
|---|---|
| 版本 | 3.12.0 |
| 核心功能 | 10 阶段全流程：研究→写作→完整性检查→审稿→修订→再审稿→再修订→最终完整性检查→定稿 |
| 触发词 | academic pipeline, research to paper, full paper workflow |
| 依赖 | deep-research, academic-paper, academic-paper-reviewer |
| 输入 | 研究问题 |
| 输出 | 完整管道的定稿论文 |

---

## 与 nature/ 分类的关系

| 任务 | nature 方案 | academic-research 方案 | 选哪个 |
|---|---|---|---|
| 写论文 | nature-writing (1.0) | academic-paper (3.2) | 简单起草用 nature，复杂多格式用 academic-research |
| 审稿 | nature-reviewer (0.1 Draft) | academic-paper-reviewer (1.10) | academic-research 成熟得多 |
| 文献检索 | nature-academic-search (2.0) | deep-research (2.9) | 简单检索用 nature，深度研究用 academic-research |
| 全流程 | 需手动串联 | academic-pipeline (3.12) | 自动化端到端 |

---

## 更新方式

```bash
cd /path/to/academic-research-skills && git pull
cp -RL deep-research /Users/ganxuanzhi/skills/academic-research/
cp -RL academic-paper /Users/ganxuanzhi/skills/academic-research/
cp -RL academic-paper-reviewer /Users/ganxuanzhi/skills/academic-research/
cp -RL academic-pipeline /Users/ganxuanzhi/skills/academic-research/
```
