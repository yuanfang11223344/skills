# AI Skills 通用目录

此目录为 **跨 AI 工具** 的通用 skill/指令文件存放目录，可供 Claude Code、Codex 及未来的 AI 编程助手共享使用。

## 管理入口

- 管理手册：[MANAGEMENT.md](MANAGEMENT.md)
- 当前索引：[INDEX.md](INDEX.md)
- 情况说明模板：[_management/templates/SKILL_STATUS_TEMPLATE.md](_management/templates/SKILL_STATUS_TEMPLATE.md)
- 索引脚本：[_management/scripts/list-skills.sh](_management/scripts/list-skills.sh)

以后每次新增、下载、修改或调用 skill 时，默认按 `MANAGEMENT.md` 执行：先盘点，再写情况说明，再更新索引，最后同步 GitHub 与 Obsidian 记录。

## 目录结构

```
skills/
├── README.md                  # 本文件，规则说明
├── _management/               # 管理手册、模板、脚本
├── <category>/                # 分类目录，一组相关 skill 放一起
│   ├── _shared/               # 该分类的共享资源
│   ├── <skill-name>/          # 单个 skill（文件夹形式，含 SKILL.md）
│   │   ├── SKILL.md           # 主 skill 文件
│   │   ├── manifest.yaml      # 路由配置（可选）
│   │   ├── static/            # 静态规则（可选）
│   │   └── references/        # 参考资料（可选）
│   └── ...
└── <standalone-skill>.md      # 独立 skill（单文件形式）
```

当前已安装：

```
skills/
├── README.md
├── _management/                # 管理工具（手册、模板、脚本）
├── nature/                    # 学术写作（11 skill，Yuan1z0825/nature-skills）
├── paper-craft/               # 论文可视化（3 skill，zsyggg/paper-craft-skills）
├── academic-research/         # 学术研究（4 skill，Imbad0202/academic-research-skills）
└── superpowers/               # 软件开发（14 skill，obra/superpowers）
```

| 分类 | 来源 | 领域 | 数量 | 入口 |
|---|---|---|---|---|
| `nature/` | Yuan1z0825/nature-skills | 学术写作 | 11 | [nature/README.md](nature/README.md) |
| `paper-craft/` | zsyggg/paper-craft-skills | 论文可视化 | 3 | [paper-craft/README.md](paper-craft/README.md) |
| `academic-research/` | Imbad0202/academic-research-skills | 学术研究 | 4 | [academic-research/README.md](academic-research/README.md) |
| `superpowers/` | obra/superpowers | 软件开发 | 14 | [superpowers/README.md](superpowers/README.md) |

## Skill 文件格式

### 单文件 Skill

适用于简单指令，一个 `.md` 文件即一个 skill：

```yaml
---
name: <skill-name>
description: <一句话描述 skill 功能，供 AI 工具在 skill 列表中展示>
---
```

紧接着是 skill 的具体指令/内容（markdown 格式）。

### 文件夹 Skill

适用于复杂工作流，每个 skill 一个文件夹，包含 `SKILL.md` 及支撑文件：

```
<skill-name>/
├── SKILL.md          # 主文件（含 frontmatter）
├── manifest.yaml     # 路由配置
├── static/           # 静态规则/模板
├── references/       # 参考资料
├── scripts/          # 辅助脚本
└── ...
```

> **设计原则**：采用最通用的 frontmatter + markdown 格式。不依赖任何单一 AI 工具的私有字段，确保跨工具兼容。

## 添加分类目录

**核心原则：一个来源 = 一个分类目录。不同 GitHub 仓库/作者的 skill 必须放在独立分类目录下，绝不可混入已有分类。**

```bash
# 1. 先判断来源，确认不在已有分类中
# 2. 新建独立分类目录
mkdir -p skills/<new-category>
# 3. 写入该分类的 README.md
# 4. 复制 skill 到分类目录下
cp -R /path/to/skill-folder skills/<new-category>/
# 5. 创建 STATUS.md，更新 INDEX.md
```

当前分类：
| 分类 | 来源 |
|---|---|
| `nature/` | Yuan1z0825/nature-skills |
| `paper-craft/` | zsyggg/paper-craft-skills |

## 各 AI 工具接入方式

### Claude Code

Claude Code 自动加载 `~/.claude/skills/` 目录。通过软链接指向此目录：

```bash
ln -s /Users/ganxuanzhi/skills ~/.claude/skills
```

已执行，无需再次操作。

### Codex (OpenAI)

```bash
ln -s /Users/ganxuanzhi/skills ~/.codex/skills
```

### 其他/未来 AI 工具

```bash
# 软链接法（推荐）
ln -s /Users/ganxuanzhi/skills <AI工具skills目录>

# 环境变量法
export AI_SKILLS_PATH="/Users/ganxuanzhi/skills"
```

## 更新 Skill

1. 直接编辑对应的文件/文件夹
2. 若为 git clone 来源，在源仓库 `git pull` 后覆盖复制到对应分类目录
3. 更新该 skill 的 `STATUS.md`
4. 运行或更新 `INDEX.md`
5. 同步 GitHub 与 Obsidian 记录
6. 更新后各 AI 工具在下次调用时自动加载

## 删除 Skill

1. 删除对应的 `.md` 文件或 skill 文件夹
2. 若需彻底移除，在各 AI 工具的配置中取消对应目录注册

## 命名规范

- 分类目录使用小写单词：`nature`、`devops`、`frontend`
- 单文件 skill：`my-skill.md`（小写 + 连字符）
- 文件夹 skill：目录名与 SKILL.md 中 `name` 一致
- 避免与各 AI 工具的内置 skill 重名

## 跨工具兼容注意事项

- 仅使用 `name` 和 `description` 两个 frontmatter 字段保证最大兼容
- Skill 内容避免使用仅特定工具支持的特殊语法
- 各 AI 工具读取自己关心的字段，忽略不认识的字段
