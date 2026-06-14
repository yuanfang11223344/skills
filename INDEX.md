# Skills 索引

更新时间：2026-06-15

根目录：`/Users/ganxuanzhi/skills`
管理入口：[MANAGEMENT.md](MANAGEMENT.md) | [README.md](README.md)

## 分类（核心规则：一个来源 = 一个分类目录）

不同 GitHub 仓库/作者的 skill 分属独立分类目录，永不混用。新来源必须建新分类。

| 分类 | 来源 | 作者 | 数量 | 领域 | 入口 |
|---|---|---|---|---|---|
| `nature/` | `Yuan1z0825/nature-skills` | 袁一哲 | 11 | 学术写作 | [nature/README.md](nature/README.md) |
| `paper-craft/` | `zsyggg/paper-craft-skills` | zsyggg | 3 | 论文可视化 | [paper-craft/README.md](paper-craft/README.md) |
| `academic-research/` | `Imbad0202/academic-research-skills` | Imbad0202 | 4 | 学术研究 | [academic-research/README.md](academic-research/README.md) |
| `superpowers/` | `obra/superpowers` | obra | 14 | 软件开发 | [superpowers/README.md](superpowers/README.md) |

---

## nature/ — 学术写作全流程（11 skill）

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

## paper-craft/ — 论文可视化与呈现（3 skill）

| Skill | 状态 | 主要用途 | 推荐触发 |
| --- | --- | --- | --- |
| `paper-analyzer` | Active | 论文→深度 HTML 长文（6 轮工作流、KaTeX/Mermaid、3 种写作风格） | 论文解读、论文深度解析、HTML 论文报告 |
| `paper-comic` | Active | 论文方法图解（生图模型，paper-figure/sketchnote 两风格） | 论文图解、方法图、概念图、论文配图 |
| `paper-deck` | Active | 论文→AIGC 高质感幻灯片（逐页生图，4 种风格，PPTX/PDF） | 论文PPT、高质感幻灯片、逐页生图PPT |

## academic-research/ — 学术研究全流程（4 skill）

| Skill | 状态 | 版本 | 主要用途 | 推荐触发 |
| --- | --- | --- | --- | --- |
| `deep-research` | Active | 2.9.4 | 13-agent 深度研究管道，7 种模式，APA 7.0 报告 | 深度研究、文献综述、系统综述、meta-analysis |
| `academic-paper` | Active | 3.2.0 | 12-agent 论文写作管道，10 种模式，LaTeX/DOCX/PDF | 写论文、学术论文、论文格式转换 |
| `academic-paper-reviewer` | Active | 1.10.0 | 5-reviewer 多视角审稿，6 种模式，含校准 | 审稿、peer review、模拟审稿 |
| `academic-pipeline` | Active | 3.12.0 | 10 阶段全流程编排：研究→写作→审稿→定稿 | 全流程、research-to-publication |

> 与 nature/ 重叠但更重量级：nature 做轻量快速任务，academic-research 做多 agent 深度管道。

## superpowers/ — 软件开发工作流（14 skill）

| Skill | 状态 | 主要用途 | 触发场景 |
| --- | --- | --- | --- |
| `using-superpowers` | Active | 入口：建立如何使用和发现 skill | 任何对话开始 |
| `brainstorming` | Active | 创意工作前探索需求 | 创建功能、修改行为 |
| `writing-plans` | Active | 为多步骤任务编写实施计划 | 有 spec 或需求 |
| `executing-plans` | Active | 执行计划，带审查检查点 | 有写好的计划 |
| `dispatching-parallel-agents` | Active | 并行调度 2+ 个独立任务 | 多个无依赖任务 |
| `subagent-driven-development` | Active | 子 agent 驱动开发 | 需要并行开发 |
| `test-driven-development` | Active | 实现功能前先写测试 | 实现功能、修复 bug |
| `systematic-debugging` | Active | 系统化调试 | bug、测试失败 |
| `verification-before-completion` | Active | 完成前验证 | 即将 commit/PR |
| `requesting-code-review` | Active | 请求代码审查 | 完成任务、合并前 |
| `receiving-code-review` | Active | 接收代码审查 | 收到审查反馈 |
| `finishing-a-development-branch` | Active | 分支完成/合并 | feature 分支完成 |
| `using-git-worktrees` | Active | Git worktree 隔离 | 开始新 feature |
| `writing-skills` | Active | 编写/维护 skill | 创建/编辑 skill |

---

## Markdown 入口目录

```text
/Users/ganxuanzhi/skills/README.md                         ← 根目录规则说明
/Users/ganxuanzhi/skills/MANAGEMENT.md                      ← 管理手册
/Users/ganxuanzhi/skills/INDEX.md                           ← 本文件，索引
/Users/ganxuanzhi/skills/nature/README.md                   ← nature 分类入口
/Users/ganxuanzhi/skills/paper-craft/README.md              ← paper-craft 分类入口
/Users/ganxuanzhi/skills/academic-research/README.md        ← academic-research 分类入口
/Users/ganxuanzhi/skills/superpowers/README.md              ← superpowers 分类入口
```

完整 SKILL.md 列表运行：`/Users/ganxuanzhi/skills/_management/scripts/list-skills.sh`

---

## 调度建议

### 按领域分类

| 用户想做什么 | 领域 | 首选分类 |
|---|---|---|
| 写论文、润色、审稿回复 | 学术写作 | `nature/` |
| 论文解读、方法图、AIGC 幻灯片 | 论文可视化 | `paper-craft/` |
| 深度文献研究、多 agent 论文管道 | 学术研究 | `academic-research/` |
| 软件开发、调试、代码审查 | 软件开发 | `superpowers/` |

### 跨分类关键区分

| 混淆场景 | 选哪个 | 为什么 |
|---|---|---|
| 轻量审稿 vs 深度审稿 | `nature-reviewer` (轻量) / `academic-paper-reviewer` (深度) | academic-research 有 5 位审稿人+6 种模式 |
| 起草段落 vs 完整论文 | `nature-writing` (起草) / `academic-paper` (完整) | academic-research 12-agent 全管道 |
| 简单检索 vs 深度研究 | `nature-academic-search` (检索) / `deep-research` (研究) | academic-research 13-agent 管道 |
| 文字PPT vs 视觉PPT | `nature-paper2ppt` (文字) / `paper-deck` (视觉) | paper-craft 逐页生图 |
| 数据图 vs 概念图 | `nature-figure` (数据图) / `paper-comic` (概念图) | paper-craft 生图模型 |

---

## 维护命令

```bash
/Users/ganxuanzhi/skills/_management/scripts/list-skills.sh
git -C /Users/ganxuanzhi/skills status --short
```

---

## 跨工具加载状态

| 工具 | 软链接 | 说明 |
|---|---|---|
| Claude Code | OK | `~/.claude/skills` → skills |
| Codex | OK | `~/.codex/skills/shared-user-skills` → skills |
