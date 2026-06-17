# baoyu-translate 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/分析/baoyu-translate`
- 入口：`SKILL.md`
- 分类：`分析`
- 来源：`https://github.com/JimLiu/baoyu-skills`
- 最近维护：`2026-06-17`

## 主要用途

三模式翻译（快翻/标准/精翻）。支持中英互译，可自定义术语表，适合需要精确翻译的专业文档。快翻=直接输出译文；标准=分析+翻译；精翻=分析+翻译+审校+润色。

## 调度关系

- 首选场景：PDF/英文文档→中文翻译
- 与 nature-reader（中英对照精读）、paper-reading（论文结构化阅读）互补
- 翻译型 skill，输入非中文PDF/文档，输出翻译后的Markdown

## 维护记录

- `2026-06-17`：从 GitHub 安装，创建情况说明。

## 待办与风险

- baoyu-translate 的精翻模式需要更多 token 和时间
- pdf-translator 依赖 Python 脚本（extract_text.py, generate_md.py）
