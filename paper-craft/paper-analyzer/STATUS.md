# paper-analyzer 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/paper-craft/paper-analyzer`
- 入口：`SKILL.md`
- 分类：`paper-craft`
- 来源：`https://github.com/zsyggg/paper-craft-skills`
- 版本：`无 version 字段`
- 最近维护：`2026-06-15`

## 主要用途

将学术论文转化为深度 HTML 长文。6 轮强制工作流：论文解析→代码仓库搜索→公式渲染（KaTeX）→Mermaid 图表→写作风格选择→HTML 输出。3 种写作风格：storytelling（公众号爆款）、academic（学术深度）、concise（速查表）。 与 `nature-reader` 的区别：reader 做中英对照全文翻译+图表定位；analyzer 做深度解读+代码搜索+公式拆解+HTML 输出。

## 推荐触发

- 论文解读、论文深度分析、解析论文
- 学术博客、论文科普、论文总结
- HTML 论文报告、论文精读
- 写论文解读文章、论文笔记

## 调度关系

- 首选场景：需要深度解读一篇论文并生成可分享的 HTML 长文
- 可联动：`nature-reader`（先精读再深度解析）、`nature-academic-search`（补充参考文献）
- 不适合：只需简短摘要、只需翻译（用 nature-reader）

## 维护记录

- `2026-06-15`：从 zsyggg/paper-craft-skills 下载安装，创建情况说明。
- `2026-06-15`：按 MANAGEMENT.md 补齐 STATUS 模板字段并校验版本、来源、索引同步。

## 待办与风险

- 无 version 字段，上游未标注版本号
- 依赖 Mermaid/KaTeX 渲染，需浏览器环境查看 HTML 输出
- 与 nature-reader 功能有交叉（都涉及论文阅读），注意区分推荐场景
