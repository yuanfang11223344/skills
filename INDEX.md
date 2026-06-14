# Skills 索引

更新时间：2026-06-15

根目录：`/Users/ganxuanzhi/skills`
管理入口：[MANAGEMENT.md](MANAGEMENT.md) | [README.md](README.md)

## 分类

| 分类 | 说明 | 入口 |
|---|---|---|
| `nature/` | 学术写作全流程（11 个 skill） | [nature/README.md](nature/README.md) |
| `paper-craft/` | 论文可视化与呈现（3 个 skill） | [paper-craft/README.md](paper-craft/README.md) |

---

## nature/ — 学术写作全流程

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

## paper-craft/ — 论文可视化与呈现

| Skill | 状态 | 主要用途 | 推荐触发 |
| --- | --- | --- | --- |
| `paper-analyzer` | Active | 论文→深度 HTML 长文（6 轮工作流、KaTeX/Mermaid、3 种写作风格） | 论文解读、论文深度解析、HTML 论文报告 |
| `paper-comic` | Active | 论文方法图解（生图模型，paper-figure/sketchnote 两风格） | 论文图解、方法图、概念图、论文配图 |
| `paper-deck` | Active | 论文→AIGC 高质感幻灯片（逐页生图，4 种风格，PPTX/PDF） | 论文PPT、高质感幻灯片、逐页生图PPT |

---

## Markdown 入口目录

```text
/Users/ganxuanzhi/skills/README.md                    ← 根目录规则说明
/Users/ganxuanzhi/skills/MANAGEMENT.md                 ← 管理手册
/Users/ganxuanzhi/skills/INDEX.md                      ← 本文件，索引
/Users/ganxuanzhi/skills/nature/README.md              ← nature 分类入口
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
/Users/ganxuanzhi/skills/paper-craft/README.md         ← paper-craft 分类入口
/Users/ganxuanzhi/skills/paper-craft/paper-analyzer/SKILL.md
/Users/ganxuanzhi/skills/paper-craft/paper-comic/SKILL.md
/Users/ganxuanzhi/skills/paper-craft/paper-deck/SKILL.md
```

---

## 调度建议

用户给出任务时，先判断分类，再选 skill：

### nature 类

| 阶段 | 首选 skill | 可联动 skill |
| --- | --- | --- |
| 找资料 | `nature-academic-search` | `nature-citation` |
| 读论文 | `nature-reader` | `nature-academic-search` |
| 写初稿 | `nature-writing` | `nature-citation`, `nature-data` |
| 润色与中译英 | `nature-polishing` | `nature-citation` |
| 补引用 | `nature-citation` | `nature-academic-search` |
| 做数据图表 | `nature-figure` | `nature-data` |
| 做汇报 | `nature-paper2ppt` | `nature-reader`, `nature-figure` |
| 回审稿人 | `nature-response` | `nature-polishing`, `nature-citation` |
| 投稿前自审 | `nature-reviewer` | `nature-writing`, `nature-polishing` |
| 转专利 | `nature-paper-to-patent` | `nature-reader` |

### paper-craft 类

| 阶段 | 首选 skill | 可联动 skill |
| --- | --- | --- |
| 论文深度解读 | `paper-analyzer` | `nature-reader`, `nature-academic-search` |
| 方法概念图解 | `paper-comic` | `nature-reader`, `nature-figure` |
| 高质感视觉PPT | `paper-deck` | `nature-reader`, `nature-figure` |

### 跨分类关键区分

| 容易混淆 | 选哪个 | 为什么 |
|---|---|---|
| 翻译 vs 解读 | `nature-reader` (翻译) / `paper-analyzer` (深度解读) | reader 输出中英对照 Markdown，analyzer 输出深度 HTML 长文 |
| 数据图 vs 概念图 | `nature-figure` (数据图) / `paper-comic` (概念图) | figure 用 Python/R 代码绘数据，comic 用生图模型画概念 |
| 文字PPT vs 视觉PPT | `nature-paper2ppt` (文字排版) / `paper-deck` (逐页生图) | paper2ppt 快速文字排版，deck 设计感强但耗时 |

---

## 维护命令

列出当前 skill：

```bash
/Users/ganxuanzhi/skills/_management/scripts/list-skills.sh
```

检查 Git 状态：

```bash
git -C /Users/ganxuanzhi/skills status --short
```

---

## 跨工具加载状态

| 工具 | 软链接 | 文件可读 | 说明 |
|---|---|---|---|
| Claude Code | OK | OK | `~/.claude/skills` → skills | 重启 session 生效 |
| Codex | OK | OK | `~/.codex/skills/shared-user-skills` → skills |
