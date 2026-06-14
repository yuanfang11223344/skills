# paper-comic 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/paper-craft/paper-comic`
- 入口：`SKILL.md`
- 分类：`paper-craft`
- 来源：`https://github.com/zsyggg/paper-craft-skills`（MIT）
- 最近维护：`2026-06-15`

## 主要用途

论文方法图解——用视觉图解讲清楚一篇论文的核心方法。先分析论文方法，推荐封面/概述图/机制细节图的生成方案，用户确认范围、张数、语言、风格后生成。支持 2 种风格：paper-figure（论文框架图风）、sketchnote（温暖笔记风）。

与 `nature-figure` 的区别：nature-figure 用 Python/R 代码生成 matplotlib/ggplot2 图表（数据驱动）；paper-comic 用生图模型生成视觉图解（AIGC 驱动），更偏向论文方法学概念图的表达。

## 推荐触发

- 论文图解、方法图解、论文图示
- 论文可视化、画论文架构图
- 论文方法图、paper figure
- 核心机制图、论文配图

## 调度关系

- 首选场景：需要为论文核心方法生成视觉概念图
- 可联动：`nature-figure`（数据图用 figure，概念图用 comic）、`nature-reader`（先精读理解方法）
- 不适合：需要精确数据驱动的图表（用 nature-figure）

## 维护记录

- `2026-06-15`：从 zsyggg/paper-craft-skills 下载安装，创建情况说明。

## 待办与风险

- 无 version 字段，上游未标注版本号
- 输出依赖生图模型，质量受模型能力影响
- 与 nature-figure 功能有交叉（都涉及论文图），注意区分推荐场景：数据图→nature-figure，概念图→paper-comic
