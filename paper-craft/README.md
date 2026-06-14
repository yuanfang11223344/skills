# paper-craft — 论文可视化与呈现

> 来源：[paper-craft-skills](https://github.com/zsyggg/paper-craft-skills)
> 作者：zsyggg
> 协议：MIT

3 个 AI skill，覆盖从论文深度 HTML 解读、方法图解法，到高质感 AIGC 幻灯片的论文可视化全流程。

---

## 架构

```
paper-craft/
├── README.md          # 本文件
├── paper-analyzer/    # 论文 → 深度 HTML 长文
├── paper-comic/       # 论文 → 方法图解（生图模型）
└── paper-deck/        # 论文 → AIGC 高质感幻灯片
```

与 `nature/` 分类互补：nature 侧重写作/润色/检索/审稿等文本工作流，paper-craft 侧重论文的视觉呈现。

---

## Skill 一览

### paper-analyzer — 论文 → 深度 HTML 长文

| 属性 | 值 |
|---|---|
| 版本 | - |
| 核心功能 | 6 轮强制工作流：论文解析→代码仓库搜索→KaTeX 公式渲染→Mermaid 图表→写作风格→HTML 输出。3 种风格：storytelling（爆款科普）、academic（深度学术）、concise（速查表） |
| 触发词 | 论文解读、论文深度分析、解析论文、HTML 论文报告、论文科普 |
| 输入 | arXiv 链接 / PDF / 粘贴文本 |
| 输出 | 可分享的精美 HTML 页面（含公式、代码对照、架构图） |

> 与 `nature-reader` 的区别：reader 做中英对照全文翻译+图表定位；analyzer 做深度解读+代码搜索+公式拆解+HTML 输出。

### paper-comic — 论文方法图解（生图模型）

| 属性 | 值 |
|---|---|
| 版本 | - |
| 核心功能 | 分析论文核心方法→推荐封面/概述图/机制细节图方案→用户确认范围/张数/语言/风格→生图模型生成。2 种风格：paper-figure（论文框架图风）、sketchnote（温暖笔记风） |
| 触发词 | 论文图解、方法图解、论文方法图、概念图、画论文架构图 |
| 输入 | 论文 PDF/链接 |
| 输出 | 视觉图解图片 |

> 与 `nature-figure` 的区别：figure 用 Python/R 代码生成数据驱动图表；comic 用生图模型生成概念图解。数据图→figure，概念图→comic。

### paper-deck — 高质感 AIGC 幻灯片（逐页生图）

| 属性 | 值 |
|---|---|
| 版本 | - |
| 核心功能 | 论文→内容分析→逐页叙事导演→生图模型生成 16:9 slide image→合成 PPTX/PDF。4 种风格：journal-minimal（Nature/IEEE）、business-research（战略报告）、warm-notes（学习笔记）、liquid-glass（Apple 风） |
| 触发词 | 论文PPT、高质感幻灯片、逐页生图PPT、不像AI的PPT、AIGC幻灯片 |
| 输入 | 论文 PDF/链接/笔记.md |
| 输出 | .pptx + .pdf |

> 与 `nature-paper2ppt` 的区别：paper2ppt 用 python-pptx 生成文字排版式 PPTX（快速）；deck 用生图模型逐页生成视觉 slide image（设计感强、耗时较长）。

---

## 与 nature/ 分类的关系

| 用户想做什么 | 用哪个 skill | 分类 |
|---|---|---|
| 中英对照读懂论文 | `nature-reader` | nature |
| 深度解读+HTML文章 | `paper-analyzer` | paper-craft |
| 数据驱动科研图表 | `nature-figure` | nature |
| 概念图/方法图解 | `paper-comic` | paper-craft |
| 文字排版PPTX | `nature-paper2ppt` | nature |
| 高质感视觉幻灯片 | `paper-deck` | paper-craft |

---

## 更新方式

```bash
cd /path/to/paper-craft-skills && git pull
cp -R skills/paper-analyzer /Users/ganxuanzhi/skills/paper-craft/
cp -R skills/paper-comic /Users/ganxuanzhi/skills/paper-craft/
cp -R skills/paper-deck /Users/ganxuanzhi/skills/paper-craft/
```

## 注意事项

- MIT 协议，可自由使用、修改、分发
- 部分 skill 依赖生图模型，输出质量受模型能力影响
