# ppt-master 情况说明

状态：Active

## 基本信息

- 路径：`/Users/ganxuanzhi/skills/ppt/ppt-master`
- 入口：`SKILL.md`
- 分类：`ppt`
- 来源：`https://github.com/hugohe3/ppt-master`（MIT）
- 版本：v2.10.0（746 次提交）
- 最近维护：`2026-06-16`

## 主要用途

AI 驱动的多格式 SVG 内容生成系统。将源文档（PDF/DOCX/URL/Markdown）转换为高质量 SVG 页面，并通过多角色协作导出为 PPTX。系统采用多角色架构（Strategist、Template Designer、Image Generator、Image Searcher、Executor、Visual Reviewer），支持：

- 10+ 画布格式：PPT 16:9、小红书、微信等
- AI 图像生成（Image Generator）
- Web 图像搜索（Image Searcher）
- 模板填充工作流
- SVG→PPTX 导出
- 动画定制、音频生成
- 原生可编辑 .pptx（DrawingML shapes）输出

## 推荐触发

- 创建PPT、做PPT、制作演示文稿
- 生成PPT、make presentation、create PPT
- ppt-master、ppt
- 生成幻灯片

## 调度关系

- 首选场景：将文档/内容转换为专业 PPTX 演示文稿
- 可联动：`nature-paper2ppt`（文字型学术PPT）、`paper-deck`（视觉型AIGC PPT）、`NewsScout`（资讯转简报PPT）
- 不适合：仅需简单排版、无需多角色协作的轻量场景

## 维护记录

- `2026-06-16`：从 hugohe3/ppt-master 下载安装（GitHub API 下载核心文件），创建情况说明。

## 待办与风险

- scripts/ 和 templates/ 目录为空（GitHub API 限制），建议补全
- 需要 Python 环境和依赖（requirements.txt）
- 多角色架构需要 AI 工具能读取完整的 references/
