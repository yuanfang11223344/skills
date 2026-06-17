# pdf-translator 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/分析/pdf-translator`
- 入口：`SKILL.md`
- 分类：`分析`
- 来源：`https://github.com/ForceInjection/AI-fundamentals`
- 最近维护：`2026-06-17`

## 主要用途

从PDF提取文本→翻译成目标语言→保存为Markdown文件。自带extract_text.py和generate_md.py脚本，适合批量PDF翻译。

## 调度关系

- 首选场景：PDF/英文文档→中文翻译
- 与 nature-reader（中英对照精读）、paper-reading（论文结构化阅读）互补
- 翻译型 skill，输入非中文PDF/文档，输出翻译后的Markdown

## 维护记录

- `2026-06-17`：从 GitHub 安装，创建情况说明。

## 待办与风险

- baoyu-translate 的精翻模式需要更多 token 和时间
- pdf-translator 依赖 Python 脚本（extract_text.py, generate_md.py）
