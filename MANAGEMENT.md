# Skills 管理手册

本手册是 `/Users/ganxuanzhi/skills` 的长期维护准则。每次用户要求处理、下载、整理、推荐或同步 skills 时，默认执行这里的流程。

## 目标

1. 把所有可共享 skills 统一放在 `/Users/ganxuanzhi/skills`。
2. 让 Claude Code、Codex 和未来工具都通过同一目录读取。
3. 每个新 skill 都有独立文件夹、`SKILL.md` 和情况说明 `STATUS.md`。
4. 用 `INDEX.md` 维护可读目录，用脚本快速列出 Markdown 与 skill 入口。
5. 本地目录以 Git 管理，并同步到 GitHub 仓库 `yuanfang11223344/skills`。
6. Obsidian Vault 同步记录每次管理动作、推荐逻辑和目录变化。
7. 定期检测上游 skill 仓库更新，提醒用户升级。

## 固定目录

- Skills 根目录：`/Users/ganxuanzhi/skills`
- Codex skills 软链接：`~/.codex/skills/shared-user-skills` → `/Users/ganxuanzhi/skills`
- Claude Code skills 软链接：`~/.claude/skills` → `/Users/ganxuanzhi/skills`
- Obsidian 同步目录：`/Users/ganxuanzhi/Documents/Obsidian Vault/AI Skills 管理`
- GitHub 仓库：`https://github.com/yuanfang11223344/skills`
- GitHub remote（实际）：以 `git remote -v` 输出为准（当前为 HTTPS）
- 上游 nature-skills：`https://github.com/Yuan1z0825/nature-skills`
- 上游 paper-craft-skills：`https://github.com/zsyggg/paper-craft-skills`
- 上游 academic-research-skills：`https://github.com/Imbad0202/academic-research-skills`
- 上游 superpowers：`https://github.com/obra/superpowers`
- 调研/ 分类来自 SkillsMP (skillsmp.com) 多源汇总，79 个 skill（发现45/分析19/产出12/推送4），按 4 阶段组织
- 上游 firecrawl-skills：`https://github.com/firecrawl/skills`
- 上游 firecrawl-cli：`https://github.com/firecrawl/cli`

## 分类核心原则：一个来源 = 一个分类目录

**不同来源的 skill 必须放在独立的分类目录下，绝不混入已有分类。**

| 规则 | 说明 |
|---|---|
| 来源隔离 | 每个 GitHub 仓库 / 作者 / 项目的 skill 独占一个分类目录 |
| 分类命名 | 使用来源仓库名或作者名，小写连字符：`nature`、`paper-craft` |
| 混入禁止 | 不要把 A 来源的 skill 放入 B 来源的分类目录 |
| 新建优先 | 新来源 → 新建分类目录 → 独立 README.md → 再放 skill |

### 当前分类映射

| 分类目录 | 来源 | 作者 |
|---|---|---|
| `nature/` | `Yuan1z0825/nature-skills` | 袁一哲 |
| `paper-craft/` | `zsyggg/paper-craft-skills` | zsyggg |
| `academic-research/` | `Imbad0202/academic-research-skills` | Imbad0202 |
| `superpowers/` | `obra/superpowers` | obra |
| `firecrawl/` | `firecrawl/skills` + `firecrawl/cli` | firecrawl |
| `调研/` | SkillsMP 多源汇总 | 社区 |

## 当前任务状态

更新时间：`2026-06-15`

| 项目 | 当前状态 |
|---|---|
| 分类总数 | 6 个：`nature/`、`paper-craft/`、`academic-research/`、`superpowers/`、`firecrawl/`、`调研/` |
| Skill 总数 | 126 个（nature 11 + paper-craft 3 + academic-research 4 + superpowers 14 + firecrawl 15 + 调研 79） |
| `STATUS.md` 覆盖 | 126/126，全部具备情况说明 |
| 本地 Git | `main` 分支，已设置 upstream |
| GitHub 同步 | `origin/main` 可达，远端为 `https://github.com/yuanfang11223344/skills.git` |
| Claude 共享 | `~/.claude/skills` 指向 `/Users/ganxuanzhi/skills` |
| Codex 共享 | `~/.codex/skills/shared-user-skills` 指向 `/Users/ganxuanzhi/skills` |
| Obsidian 镜像 | 位于 `/Users/ganxuanzhi/Documents/Obsidian Vault/AI Skills 管理`，每次维护后同步 |

### 当前分类任务

| 分类 | 数量 | 管理任务 | 调度定位 |
|---|---:|---|---|
| `nature/` | 11 | 保持轻量学术写作、读文献、润色、审稿回复链路稳定 | 论文日常处理首选 |
| `paper-craft/` | 3 | 保持论文可视化、HTML 长文、视觉 PPT 与 nature 区分清楚 | 视觉呈现和生图型输出 |
| `academic-research/` | 4 | 管理多 agent 深度研究和完整论文管道 | 深度研究、完整论文工作流 |
| `superpowers/` | 14 | 管理软件开发方法论、调试、计划、评审流程 | 编程/工程任务的工作法 |
| `firecrawl/` | 15 | 管理 web 搜索、抓取、交互、SDK 集成技能 | 网页数据提取与应用集成 |
| `调研/` | 79 | 管理学术调研全流程技能（发现45/分析19/产出12/推送4），按阶段维护 | 学术调研从发现到推送全链路 |

### 当前维护待办

1. 新增 skill 时继续执行「一个来源 = 一个分类目录」。
2. 每次新增或更新后运行 `_management/scripts/list-skills.sh`，确认 `SKILL.md` 和 `STATUS.md` 数量一致。
3. Obsidian 的 `Skills 管理手册.md`、`Skills 索引.md`、`Skills 维护日志.md` 必须和本目录同步。
4. GitHub 同步失败时写入 `_management/last-unsynced.md`；同步成功后删除该文件。
5. 上游更新只检测和提醒，不自动覆盖本地 skill。

### 新来源接入示例

```bash
# 错误：把 A 来源的 skill 放进 nature/
cp -R new-source/skills/foo /Users/ganxuanzhi/skills/nature/   # ❌

# 正确：给新来源建独立分类目录
mkdir -p /Users/ganxuanzhi/skills/new-source
cp -R new-source/skills/foo /Users/ganxuanzhi/skills/new-source/
# 再写 new-source/README.md、STATUS.md，更新 INDEX.md
```

**以后再下载任何 skill，第一步先判断来源——如果来源不在已有分类中，必须新建分类目录。**

## 每次处理流程

### 第 0 步：启动前健康检查（<30 秒，每次必做）

任何一项失败都要记录原因并报告用户，不要静默跳过。

| 检查项 | 命令/方式 | 失败处理 |
|---|---|---|
| Claude Code 软链接 | `ls -la ~/.claude/skills` | 如断开则重建；如是真实目录则报告用户 |
| Codex 软链接 | `ls -la ~/.codex/skills/shared-user-skills` | 同上 |
| Git remote 可达 | `git remote -v && git fetch --dry-run` | 记录原因，不阻塞其他步骤 |
| Obsidian 目录 | `ls "/Users/ganxuanzhi/Documents/Obsidian Vault/AI Skills 管理"` | 如不存在则创建并初始化三个基础文件 |
| list-skills.sh 可执行 | `test -x _management/scripts/list-skills.sh` | 如不可执行则 `chmod +x` |
| .gitignore 存在 | `test -f .gitignore` | 如不存在则创建，至少排除 .DS_Store |

**注意**：Git remote 格式以实际 `git remote -v` 输出为准。当前为 HTTPS（`https://github.com/yuanfang11223344/skills.git`），如果 MANAGEMENT.md 中写了 SSH 但实际为 HTTPS，以实际为准，报告中标注差异即可。

### 第 1 步：盘点目录

- 列出所有 skill 文件夹和 SKILL.md 入口
- 识别新增、修改、缺失的文件
- 运行 `_management/scripts/list-skills.sh` 获取当前状态
- 检查每个 skill 是否具备：SKILL.md、STATUS.md
- 检查是否有建议但缺失的文件：README.md、manifest.yaml、static/、references/

**排除规则**——以下目录/文件不要当作 skill 盘点：
- `_management/` — 管理工具，不是 skill
- `README.md` / `MANAGEMENT.md` / `INDEX.md` — 顶层管理文件
- `.DS_Store` / `.git/` / `.gitignore` — 系统/版本控制文件
- 没有 `SKILL.md` 的目录 — 可能是分类目录（如 `nature/`）或共享资源目录（如 `_shared/`）

**结构区分**：
| 目录类型 | 特征 | 举例 |
|---|---|---|
| 分类目录 | 无 SKILL.md，有子目录 | `nature/` |
| 共享资源 | 无 SKILL.md，被 manifest.yaml 引用 | `nature/_shared/` |
| Skill 目录 | 有 SKILL.md | `nature/nature-polishing/` |
| 管理目录 | 在 _management/ 下 | `_management/` |

### 第 2 步：校验结构

- 复杂 skill 必须是文件夹形式，入口为 `SKILL.md`
- `SKILL.md` 必须包含 `name` 和 `description` frontmatter
- **从 SKILL.md 中读取 `version` 字段，记录当前版本号**
- 路由型 skill（有 `manifest.yaml`）必须能访问 `_shared/` 共享资源
- 检查相对路径引用是否有效（如 `../_shared/core/xxx.md`）
- 检查 `.gitignore` 是否覆盖了 `.DS_Store`、`*.swp`、`*.tmp` 等常见垃圾文件

### 第 3 步：写情况说明

每个 skill 的 `STATUS.md` 至少包含：

- 当前状态：Active、Beta、Draft、Archived。
- 版本号（与 SKILL.md 的 version 一致）。
- 主要用途。
- 推荐触发词。
- 与其他 skills 的关系。
- 最近维护记录。
- 风险或待办。

模板见：`_management/templates/SKILL_STATUS_TEMPLATE.md`。

### 第 4 步：更新索引

- 更新 `INDEX.md`
- 索引必须包含：
  - 总览表：skill 名称、状态、主要用途、推荐触发词
  - Markdown 入口目录：列出所有 SKILL.md 和重要 README.md 的绝对路径并加简短注释
  - 调度建议表：按任务阶段列出首选 skill 和可联动 skill
  - 维护命令：list-skills.sh 路径、git status 命令
- 索引底部增加「跨工具加载状态」小节

### 第 5 步：上游更新检测

- 记录每个 skill 的当前版本号（从 `SKILL.md` frontmatter 读取 `version`）
- 对于来源为 `Yuan1z0825/nature-skills` 的 skill，检查上游：
  ```bash
  git ls-remote --tags https://github.com/Yuan1z0825/nature-skills.git 2>/dev/null
  ```
- 如果发现新版本：
  - **通知用户**「XX skill 有新版本 vA.B.C，当前版本 vX.Y.Z」
  - **询问用户**是否更新
  - **不要自动覆盖**，等用户确认
- 如果上游不可达：记录原因，标记「本次未检查」
- 更新方式（用户确认后）：
  ```bash
  cd /tmp && git clone --depth 1 https://github.com/Yuan1z0825/nature-skills.git nature-skills-update
  cp -R nature-skills-update/skills/<skill-name> /Users/ganxuanzhi/skills/nature/<skill-name>
  cp -R nature-skills-update/skills/_shared /Users/ganxuanzhi/skills/nature/_shared
  rm -rf nature-skills-update
  ```

### 第 6 步：推荐调度

优先级从高到低：

1. 用户明确点名某个 skill。
2. 用户任务与 `description` 高度匹配。
3. 任务涉及文件类型或工具链，例如 PDF、PPTX、论文配图、专利文档。
4. 任务涉及阶段，例如读论文、写论文、润色、加引用、审稿回复、做 PPT。
5. 多个 skill 都匹配时，推荐主 skill，并说明可能联动的辅助 skill。

常用路由：

| 用户任务 | 首选 skill | 可联动 skill |
|---|---|---|
| 读论文、全文翻译、中英对照 | nature-reader | nature-academic-search |
| 文献检索、查论文、引文核对 | nature-academic-search | nature-citation |
| 写论文结构、起草章节 | nature-writing | nature-citation, nature-data |
| 论文润色、中译英、LaTeX 排版 | nature-polishing | nature-citation |
| 自动补引用、Nature/CNS 支撑文献 | nature-citation | nature-academic-search |
| 数据可用性、代码和数据共享声明 | nature-data | — |
| 科研绘图、论文图表 | nature-figure | nature-data |
| 论文转组会 PPT | nature-paper2ppt | nature-reader, nature-figure |
| 审稿意见回复、rebuttal | nature-response | nature-polishing, nature-citation |
| 投稿前模拟审稿 | nature-reviewer | nature-writing, nature-polishing |
| 论文转中国发明专利 | nature-paper-to-patent | nature-reader |

### 第 7 步：同步 Obsidian

Obsidian 中维护：

- `Skills 管理手册.md`：镜像本手册摘要。
- `Skills 索引.md`：镜像当前索引。
- `Skills 维护日志.md`：追加每次变更记录。

记录格式：

```text
YYYY-MM-DD HH:mm - <动作> - <影响的 skill 或文件> - <Git 状态>
```

### 第 8 步：Git 同步

- 提交前确保 `.gitignore` 覆盖了常见垃圾文件（.DS_Store、*.swp、*.tmp 等）
- 检查 `git status --short`，如果发现垃圾文件在未跟踪列表，先确认 `.gitignore` 生效
- 提交信息格式：`skills: <本次维护内容>`
- **使用实际的 git remote URL**（以 `git remote -v` 输出为准，不要硬编码特定协议）
- 提交前展示变更摘要，等待用户确认
- Push 前确认 upstream 已设置：
  ```bash
  git push --set-upstream origin main
  ```
- **Push 失败降级方案**：
  - 不要静默跳过，记录错误原因
  - 如果因认证问题（HTTPS 需要 token），提示用户检查 git credential
  - 保存变更摘要到 `_management/last-unsynced.md`，下次成功同步后删除
  - 报告中明确标注「Git push 失败，变更已暂存本地」

### 第 9 步：跨工具加载状态

每次执行后在最终报告中增加：

| 工具 | 软链接 | 文件可读 | 说明 |
|---|---|---|---|
| Claude Code | OK/FIXED/FAIL | OK/FAIL | 新 session 生效 |
| Codex | OK/FIXED/FAIL | OK/FAIL | 已通过 shared-user-skills 加载 |

提示用户：
- 如果新安装的 skill 在 Claude Code 中不生效：重启 session 或 `claude --clear-cache`
- 如果新安装的 skill 在 Codex 中不生效：重启 Codex session
- 首次安装的 skill 可能需要 1-2 次交互后才会被 AI 工具自动发现

## Github 同步规则

本地仓库设在 `/Users/ganxuanzhi/skills`。远端目标：

```bash
git remote add origin https://github.com/yuanfang11223344/skills.git
```

如果 GitHub 仓库尚不存在，先完成本地 Git 初始化和 Obsidian 记录；等仓库创建后再执行：

```bash
git push -u origin main
```

### 当前状态

- `2026-06-15`：本地仓库已初始化并推送成功，upstream 已设置。
- `2026-06-15`：Git 仓库 `yuanfang11223344/skills` 已在 GitHub 创建，HTTPS push 正常。
- `2026-06-15`：当前 5 个分类、47 个 skill，`STATUS.md` 覆盖率 100%。

### 每次同步前先检查

```bash
git status --short
```

### 提交信息格式

```text
skills: <本次维护内容>
```

### 不要提交

- .DS_Store、*.swp、*.tmp
- 临时下载文件
- 无关缓存

## 本机共享接入

软链接：

```bash
ln -s /Users/ganxuanzhi/skills ~/.claude/skills
ln -s /Users/ganxuanzhi/skills ~/.codex/skills/shared-user-skills
```

如果目标目录已存在，先确认是否已是软链接，避免覆盖已有用户内容。

## 跨工具兼容注意事项

- Skill 内容使用通用的 frontmatter + markdown 格式，不绑定任何单一 AI 工具
- 各 AI 工具读取自己关心的字段，忽略不认识的字段
- 维护时不要引入仅特定工具支持的私有字段
