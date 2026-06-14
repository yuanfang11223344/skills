# Skills 管理手册

本手册是 `/Users/ganxuanzhi/skills` 的长期维护准则。每次用户要求处理、下载、整理、推荐或同步 skills 时，默认执行这里的流程。

## 目标

1. 把所有可共享 skills 统一放在 `/Users/ganxuanzhi/skills`。
2. 让 Claude Code、Codex 和未来工具都通过同一目录读取。
3. 每个新 skill 都有独立文件夹、`SKILL.md` 和情况说明 `STATUS.md`。
4. 用 `INDEX.md` 维护可读目录，用脚本快速列出 Markdown 与 skill 入口。
5. 本地目录以 Git 管理，并同步到 GitHub 仓库 `yuanfang11223344/skills`。
6. Obsidian Vault 同步记录每次管理动作、推荐逻辑和目录变化。

## 固定目录

- Skills 根目录：`/Users/ganxuanzhi/skills`
- Obsidian 同步目录：`/Users/ganxuanzhi/Documents/Obsidian Vault/AI Skills 管理`
- GitHub 目标仓库：`https://github.com/yuanfang11223344/skills`
- GitHub remote：`git@github.com:yuanfang11223344/skills.git`

## 每次处理流程

1. 盘点目录：列出新增、修改、缺失的 `SKILL.md`、`README.md`、`manifest.yaml`、`STATUS.md`。
2. 校验结构：复杂 skill 必须是文件夹形式，入口为 `SKILL.md`；简单 skill 可以是单个 Markdown。
3. 写情况说明：每个新 skill 文件夹必须新增或更新 `STATUS.md`。
4. 更新索引：更新 `INDEX.md`，记录 skill 名称、用途、触发词、状态、路径。
5. 推荐调度：根据用户当前任务，从 `INDEX.md` 和 `SKILL.md` 描述中推荐最匹配的 skill。
6. 同步 Obsidian：更新 Obsidian 中的管理笔记，记录本次变更和推荐规则。
7. Git 同步：提交本地 changes；如果远端仓库可用，推送到 `yuanfang11223344/skills`。

## 新 Skill 接入规范

新下载的 skill 放入：

```text
/Users/ganxuanzhi/skills/<category>/<skill-name>/
```

必需文件：

- `SKILL.md`：主入口，包含 `name` 和 `description` frontmatter。
- `STATUS.md`：情况说明，记录来源、用途、状态、维护动作。

建议文件：

- `README.md`：给人看的说明。
- `manifest.yaml`：路由轴、加载片段、动态调度配置。
- `static/`：稳定规则、模板、片段。
- `references/`：按需读取的参考材料。
- `scripts/`：可复用脚本。
- `tests/` 或 `evals/`：测试与评估样例。

## STATUS.md 要写什么

每个 skill 的 `STATUS.md` 至少包含：

- 当前状态：Active、Beta、Draft、Archived。
- 主要用途。
- 推荐触发词。
- 与其他 skills 的关系。
- 最近维护记录。
- 风险或待办。

模板见：`_management/templates/SKILL_STATUS_TEMPLATE.md`。

## 推荐调度规则

优先级从高到低：

1. 用户明确点名某个 skill。
2. 用户任务与 `description` 高度匹配。
3. 任务涉及文件类型或工具链，例如 PDF、PPTX、论文配图、专利文档。
4. 任务涉及阶段，例如读论文、写论文、润色、加引用、审稿回复、做 PPT。
5. 多个 skill 都匹配时，推荐主 skill，并说明可能联动的辅助 skill。

常用路由：

- 读论文、全文翻译、中英对照：`nature-reader`
- 文献检索、查论文、引文核对：`nature-academic-search`
- 写论文结构、起草章节：`nature-writing`
- 论文润色、中译英、LaTeX 排版：`nature-polishing`
- 自动补引用、Nature/CNS 支撑文献：`nature-citation`
- 数据可用性、代码和数据共享声明：`nature-data`
- 科研绘图、论文图表：`nature-figure`
- 论文转组会 PPT：`nature-paper2ppt`
- 审稿意见回复、rebuttal：`nature-response`
- 投稿前模拟审稿：`nature-reviewer`
- 论文转中国发明专利：`nature-paper-to-patent`

## GitHub 同步规则

本地仓库设在 `/Users/ganxuanzhi/skills`。远端目标为：

```bash
git remote add origin git@github.com:yuanfang11223344/skills.git
```

如果 GitHub 仓库尚不存在，先完成本地 Git 初始化和 Obsidian 记录；等仓库创建后再执行：

```bash
git push -u origin main
```

每次同步前先检查：

```bash
git status --short
```

提交信息格式：

```text
skills: <本次维护内容>
```

## Obsidian 同步规则

Obsidian 中维护：

- `Skills 管理手册.md`：镜像本手册摘要。
- `Skills 索引.md`：镜像当前索引。
- `Skills 维护日志.md`：追加每次变更记录。

记录格式：

```text
YYYY-MM-DD HH:mm - <动作> - <影响的 skill 或文件> - <Git 状态>
```

## 本机共享接入

推荐用软链接让其他工具共享：

```bash
ln -s /Users/ganxuanzhi/skills ~/.codex/skills
ln -s /Users/ganxuanzhi/skills ~/.claude/skills
```

如果目标目录已存在，先确认是否已是软链接，避免覆盖已有用户内容。
