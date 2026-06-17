# translate-polisher 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/分析/translate-polisher`
- 入口：`SKILL.md`
- 分类：`分析`
- 来源：`https://github.com/rookie-ricardo/erduo-skills`
- 最近维护：`2026-06-17`

## 主要用途

四步精翻工作流（分析→初译→审校→终稿）。中英/中日互译，支持读者预设（普通/技术/学术/商务）和风格预设（故事/正式/技术/直译/学术/商务/幽默/口语/精炼）。882⭐，质量最高。

## 调度关系

- 首选场景：PDF/英文文档→中文翻译
- 与 nature-reader（中英对照精读）、paper-reading（论文结构化阅读）互补
- 翻译型 skill，输入非中文PDF/文档，输出翻译后的Markdown

## 维护记录

- `2026-06-17`：从 GitHub 安装，创建情况说明。

## 待办与风险

- baoyu-translate 的精翻模式需要更多 token 和时间
- pdf-translator 依赖 Python 脚本（extract_text.py, generate_md.py）
