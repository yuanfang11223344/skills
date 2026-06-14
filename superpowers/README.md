# superpowers — 软件开发工作流 AI 工具箱

> 来源：[superpowers](https://github.com/obra/superpowers)
> 作者：obra
> 协议：见 LICENSE

14 个 AI skill，覆盖从需求分析、计划编写、TDD 开发、调试、代码审查到分支管理的完整软件开发工作流。

> 与 nature/paper-craft/academic-research 完全互补：那些是学术写作，这个是软件开发。

---

## 架构

```
superpowers/
├── README.md                       # 本文件
├── using-superpowers/              # ① 入口：如何使用 superpowers
├── brainstorming/                  # ② 需求分析/创意探索
├── writing-plans/                  # ③ 写实施计划
├── executing-plans/                # ④ 执行实施计划
├── dispatching-parallel-agents/    # ⑤ 并行任务调度
├── subagent-driven-development/    # ⑥ 子 agent 驱动开发
├── test-driven-development/        # ⑦ TDD 测试驱动开发
├── systematic-debugging/           # ⑧ 系统化调试
├── verification-before-completion/ # ⑨ 完成前验证
├── requesting-code-review/         # ⑩ 请求代码审查
├── receiving-code-review/          # ⑪ 接收代码审查
├── finishing-a-development-branch/ # ⑫ 分支完成/合并
├── using-git-worktrees/            # ⑬ Git worktree 隔离
└── writing-skills/                 # ⑭ 编写/维护 skill
```

---

## Skill 一览

| Skill | 主要用途 | 触发场景 |
|---|---|---|
| `using-superpowers` | 入口：建立如何使用和发现 skill | 任何对话开始 |
| `brainstorming` | 创意工作前必须先做：探索用户意图、需求和设计 | 创建功能、添加功能、修改行为 |
| `writing-plans` | 为多步骤任务编写实施计划 | 有 spec 或需求，开始写代码前 |
| `executing-plans` | 在独立 session 中执行计划，带审查检查点 | 有写好的实施计划 |
| `dispatching-parallel-agents` | 并行调度 2+ 个独立任务 | 多个无依赖关系的独立任务 |
| `subagent-driven-development` | 当前 session 中执行带独立任务的计划 | 需要在当前 session 并行开发 |
| `test-driven-development` | 实现任何功能/bugfix 前先写测试 | 实现功能、修复 bug |
| `systematic-debugging` | 遇到 bug/测试失败时，在提出修复前系统分析 | bug、测试失败、意外行为 |
| `verification-before-completion` | 声称完成前必须运行验证命令并确认输出 | 即将 commit、创建 PR |
| `requesting-code-review` | 完成任务/实现主要功能后验证工作 | 完成任务、合并前 |
| `receiving-code-review` | 收到代码审查反馈后，在实现建议前 | 收到审查反馈 |
| `finishing-a-development-branch` | 实现完成、测试通过后决定如何集成 | feature 分支完成 |
| `using-git-worktrees` | 需要隔离的 feature 工作 | 开始新 feature、执行计划前 |
| `writing-skills` | 创建/编辑/验证 skill | 创建新 skill、编辑已有 skill |

---

## 典型工作流

```
brainstorming → writing-plans → [executing-plans 或 subagent-driven-development]
                                    ↓
                              dispatching-parallel-agents
                                    ↓
                              test-driven-development
                                    ↓
                              systematic-debugging
                                    ↓
                              verification-before-completion
                                    ↓
                              requesting-code-review → receiving-code-review
                                    ↓
                              finishing-a-development-branch
                                    ↓
                              using-git-worktrees
```

全程贯穿 `using-superpowers`（入口）和 `writing-skills`（维护）。

---

## 与其他分类的关系

superpowers 专注于 **软件开发**，与学术分类互不重叠：

| 分类 | 领域 |
|---|---|
| `nature/` | 学术写作、润色、审稿 |
| `paper-craft/` | 论文可视化、PPT |
| `academic-research/` | 深度研究、论文管道 |
| **`superpowers/`** | **软件开发全流程** |

---

## 更新方式

```bash
cd /path/to/superpowers && git pull
cp -R skills/* /Users/ganxuanzhi/skills/superpowers/
```
