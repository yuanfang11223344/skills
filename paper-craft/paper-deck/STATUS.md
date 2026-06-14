# paper-deck 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/paper-craft/paper-deck`
- 入口：`SKILL.md`
- 分类：`paper-craft`
- 来源：`https://github.com/zsyggg/paper-craft-skills`（MIT）
- 最近维护：`2026-06-15`

## 主要用途

将论文/技术文章制作成高真实感 AIGC 幻灯片。先做叙事结构和逐页视觉导演，再调用生图模型生成 16:9 slide image，最后合成为 PPTX/PDF。4 种风格：journal-minimal（Nature/IEEE 学术风）、business-research（战略报告）、warm-notes（学习笔记）、liquid-glass（Apple 风）。

与 `nature-paper2ppt` 的区别：nature-paper2ppt 用 python-pptx 生成文字排版式 PPTX；paper-deck 用生图模型逐页生成视觉 slide image 再合成，幻灯片更像设计稿而非模板。

## 推荐触发

- 论文PPT、AI生成PPT、高质感幻灯片
- 逐页生图PPT、不像AI的PPT
- 组会PPT、学术汇报、论文展示
- 技术分享、公开课、商业化研究展示

## 调度关系

- 首选场景：需要视觉设计感强、不像模板的论文汇报 PPT
- 可联动：`nature-reader`（先精读理解内容）、`nature-figure`（数据图嵌入 slide）、`nature-paper2ppt`（二选一：文字型选 paper2ppt，视觉型选 deck）
- 不适合：只需要简单文字排版 PPT（用 nature-paper2ppt 更快）

## 维护记录

- `2026-06-15`：从 zsyggg/paper-craft-skills 下载安装，创建情况说明。

## 待办与风险

- 无 version 字段，上游未标注版本号
- 输出依赖生图模型，每页 slide image 生成耗时较长
- 与 nature-paper2ppt 功能重叠，需根据用户偏好选择
