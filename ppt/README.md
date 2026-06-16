# ppt — PPT 生成与演示文稿制作

> 来源：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (v2.10.0)
> 作者：hugohe3
> 协议：MIT

1 个 AI skill，AI 驱动的多格式 SVG 内容生成系统，将源文档转换为高质量 PPTX 演示文稿。

---

## 架构

```
ppt/
├── README.md
└── ppt-master/          # ① PPT 大师（多角色协作PPT生成）
    ├── SKILL.md         # 核心工作流
    ├── references/      # 画布格式、图像生成/搜索、模板设计、SVG嵌入等参考
    ├── workflows/       # 工作流：模板创建、规格精炼、动画定制、音频生成
    ├── scripts/         # Python 脚本（image_gen, image_search, update_repo）
    └── templates/       # 模板文件
```

---

## Skill 一览

### ppt-master — AI 多角色 PPT 生成系统

| 属性 | 值 |
|---|---|
| 版本 | v2.10.0 |
| 核心功能 | 多格式源文档（PDF/DOCX/URL/MD）→ 高质量 SVG 页面 → PPTX，支持 10+ 画布格式，多角色协作（Strategist/Template Designer/Image Generator/Image Searcher/Executor/Visual Reviewer），原生可编辑 .pptx 输出 |
| 触发词 | 创建PPT、做PPT、制作演示文稿、生成PPT、ppt-master |
| 输入 | PDF/DOCX/URL/Markdown 源文档 |
| 输出 | 原生可编辑 .pptx 文件（DrawingML shapes） |

---

## 多角色架构

| 角色 | 职责 |
|---|---|
| Strategist | 分析源文档，规划内容结构和页面布局策略 |
| Template Designer | 设计模板样式、配色方案、排版规则 |
| Image Generator | AI 图像生成（Image Generator） |
| Image Searcher | Web 图像搜索（Image Searcher） |
| Executor | 按照参考规范执行 SVG 生成和 PPTX 导出 |
| Visual Reviewer | 视觉审查：检查排版、颜色、对齐等 |

---

## 与已有 PPT 相关 skill 的区别

| 场景 | ppt-master | nature-paper2ppt | paper-deck |
|---|---|---|---|
| **通用 PPT** | ✅ 任意内容 → PPT | ❌ 仅论文 | ❌ 仅论文/知识内容 |
| **学术论文 PPT** | ✅ 可用 | ✅ 最佳（文字排版型） | ✅（视觉型，生图模型） |
| **输出格式** | 原生 .pptx | .pptx | .pptx + .pdf |
| **生成方式** | SVG→PPTX（代码生成） | python-pptx 文字排版 | 生图模型逐页生成 |
| **图像支持** | AI生成 + Web搜索 | 论文原图嵌入 | AI 生图 |
| **多格式源** | PDF/DOCX/URL/MD | 论文集 | 论文集/笔记 |
| **画布格式** | PPT 16:9 + 小红书 + 微信等 10+ | 仅 PPT | 仅 PPT |

---

## 更新方式

```bash
cd /path/to/ppt-master && git pull
cp -R skills/ppt-master /Users/ganxuanzhi/skills/ppt/
```

---

## 注意事项

- MIT 协议，可自由使用、修改、分发
- 需要 Python 环境和依赖（requirements.txt）
- 版本 v2.10.0，社区活跃（746 次提交）
