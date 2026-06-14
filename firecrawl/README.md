# firecrawl — Web 数据提取 AI 工具箱

> 来源：[firecrawl/skills](https://github.com/firecrawl/skills) + [firecrawl/cli](https://github.com/firecrawl/cli)
> 组织：firecrawl
> 协议：见 LICENSE

15 个 AI skill，覆盖 web scraping、网站爬取、数据提取、交互、文件解析、搜索、监控、构建集成的完整 web 数据工作流。

---

## 架构

```
firecrawl/
├── README.md                # 本文件
│
│   # 来自 firecrawl/cli（10 skill）— CLI 运行时操作
├── firecrawl-cli/           # ① 入口：Firecrawl CLI 总 skill
├── firecrawl-search/        # ② Web 搜索+全文提取
├── firecrawl-scrape/        # ③ 单页抓取→markdown
├── firecrawl-crawl/         # ④ 整站爬取
├── firecrawl-map/           # ⑤ 站点 URL 发现
├── firecrawl-interact/      # ⑥ 浏览器交互（点击/填表/登录）
├── firecrawl-agent/         # ⑦ AI 自主数据提取（schema→JSON）
├── firecrawl-parse/         # ⑧ 本地文件→markdown（PDF/DOCX/XLSX）
├── firecrawl-download/      # ⑨ 整站下载为本地文件
├── firecrawl-monitor/       # ⑩ 页面变更监控+通知
│
│   # 来自 firecrawl/skills（5 skill）— SDK 代码集成
├── firecrawl-build/         # ⑪ 集成向导（总入口）
├── firecrawl-build-onboarding/ # ⑫ SDK 凭证与安装
├── firecrawl-build-scrape/  # ⑬ `/scrape` 端点集成
├── firecrawl-build-search/  # ⑭ `/search` 端点集成
└── firecrawl-build-interact/ # ⑮ `/interact` 端点集成
```

---

## Skill 一览

### CLI 运行技能（firecrawl/cli）

| Skill | 主要用途 | 触发场景 |
|---|---|---|
| `firecrawl-cli` | 总入口：搜索/抓取/交互 web | 搜索网页、查找文章、抓取 URL |
| `firecrawl-search` | Web 搜索+全文提取 | 搜索、找资料、发现来源 |
| `firecrawl-scrape` | 单页→clean markdown（含 JS 渲染 SPA） | scrape、grab、fetch、pull、读网页 |
| `firecrawl-crawl` | 整站/站点区域批量提取 | crawl、获取所有页面、批量提取 |
| `firecrawl-map` | 发现并列出站点所有 URL | map the site、找某个页面、列出所有页面 |
| `firecrawl-interact` | 浏览器自动化：点击/填表/登录 | click、fill form、login、分页/无限滚动 |
| `firecrawl-agent` | AI 自主结构化数据提取（schema→JSON） | extract structured data、提取为 JSON |
| `firecrawl-parse` | 本地文件→markdown（PDF/DOCX/XLSX/HTML） | parse this PDF、convert document、读文件 |
| `firecrawl-download` | 整站下载为本地文件（md+截图） | download the site、离线保存 |
| `firecrawl-monitor` | 页面变更监控（webhook/email 通知） | monitor、watch、track、alert me when |

### SDK 构建技能（firecrawl/skills）

| Skill | 主要用途 | 触发场景 |
|---|---|---|
| `firecrawl-build` | 集成向导：将 Firecrawl 集成到应用代码 | 需要 web data 到应用中 |
| `firecrawl-build-onboarding` | 获取凭证+SDK 安装 | 需要 API key、安装 SDK |
| `firecrawl-build-scrape` | `/scrape` 端点：单页提取 | app 已有 URL，需要提取内容 |
| `firecrawl-build-search` | `/search` 端点：发现+提取 | app 需要发现后再提取 |
| `firecrawl-build-interact` | `/interact` 端点：动态页面+浏览器动作 | 动态页面交互抓取 |

---

## 典型工作流

```
                    入口
                     ↓
            firecrawl-cli（总 skill）
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
     search →    scrape     interact
        │            │            │
        ↓            ↓            ↓
      map →       crawl →   download
        │
        ↓
    agent（schema→JSON）
        │
        ↓
    parse（本地文件）
        │
        ↓
    monitor（变更监控）
```

SDK 构建技能独立使用：

```
firecrawl-build → onboarding → scrape/search/interact
```

---

## 与其他分类的关系

firecrawl 专注于 **web 数据提取**，与其他分类互补：

| 分类 | 领域 |
|---|---|
| `nature/` | 学术写作、润色、审稿 |
| `paper-craft/` | 论文可视化、PPT |
| `academic-research/` | 深度研究、论文管道 |
| `superpowers/` | 软件开发全流程 |
| **`firecrawl/`** | **web 数据提取** |

---

## 更新方式

```bash
# CLI skills
cd /path/to/firecrawl-cli && git pull
for d in skills/*; do cp -R "$d" /Users/ganxuanzhi/skills/firecrawl/; done

# SDK skills
cd /path/to/firecrawl-skills && git pull
for d in skills/*; do cp -R "$d" /Users/ganxuanzhi/skills/firecrawl/; done
```
