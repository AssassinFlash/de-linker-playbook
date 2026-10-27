# Apify 研究入口

Apify 是本仓库所有搜索、外部信息验证、竞品研究、行业规则确认和资料获取的强制主入口。普通搜索不是默认替代品；替代工具只有在 Apify 路径已诊断、修复并记录后使用。

## 凭据与环境

- Token 文件：`~/.config/de-linker-playbook/apify.env`，权限必须是 `600`。
- 环境变量：`APIFY_TOKEN`。
- 备选变量：`APIFY_TOKEN_PRIMARY`、`APIFY_TOKEN_ROTATION_2`、`APIFY_TOKEN_ROTATION_3`。
- 交互式 zsh 从该文件加载；非交互脚本和 Codex 命令必须显式加载：

```sh
set -a
source "$HOME/.config/de-linker-playbook/apify.env"
set +a
```

- Token 每月可能轮换。只替换仓外配置文件，不改仓库；绝不把 token 写进代码、日志、交付物、PR 或对话输出。

## 额度与质量策略

操作者 2026-10-21 明确：Apify Token 属于预付费、按月轮换的资源，未用完也会过期。外部研究以证据质量和效率优先，不因剩余额度减少查询深度，也不需要每次运行前单独审批费用。

仍保留两项工程纪律：

- 新 Actor 或新查询先用小批量确认 schema、噪声率和结果字段，再扩大日期范围或结果数。
- 同一查询不要无理由重复；扩大覆盖应换关键词、页面、数据源、语言、地区或 Actors。

其他未预付费的数据服务仍按各自授权边界处理，不把这条 Apify 规则外推。

## 连通性检查

```sh
set -a
source "$HOME/.config/de-linker-playbook/apify.env"
set +a
curl -sS -o /dev/null -w '%{http_code}\n' \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  https://api.apify.com/v2/users/me
```

预期 `200`。失败时先区分凭证过期、网络、代理、Apify 服务状态和 token 配额，不能直接改用普通搜索。

## 默认搜索 Actor

`apify/rag-web-browser` 是默认搜索入口：

```sh
set -a
source "$HOME/.config/de-linker-playbook/apify.env"
set +a
apify call apify/rag-web-browser \
  --input '{"query":"target query","maxResults":5,"outputFormats":["markdown"],"scrapingTool":"raw-http","requestTimeoutSecs":90}' \
  --output-dataset --silent
```

抓取指定 URL 时，把完整 URL 放进 `query`。动态页优先把 `scrapingTool` 改成 `browser-playwright`。

大批量公开页用 `apify/website-content-crawler`，按其当前 input schema 配置起始 URL、链接范围和页数上限。

## 失败修复顺序

首次失败后按以下顺序排查，并在交付物的搜索日志或阻塞日志写明每一步：

1. `APIFY_TOKEN` 是否存在、是否过期、是否来自当前月配置。
2. `users/me` 是否返回 200；检查账号、预算和配额。
3. Actor slug、build 和 input schema 是否仍有效。
4. `query`、URL、`maxResults`、输出格式、超时和并发参数是否正确。
5. 是否被 Google SERP、目标站反爬、登录墙或验证码挡住。
6. 换关键词、页面、数据源、Actor、抓取工具和请求参数。
7. 检查 run 状态、日志、Dataset 是否为空以及输出解析。
8. 处理 network、proxy、timeout、rate limit 与并发上限。

不同路径至少尝试到足以证明目标确实不可得，才能写缺口。不能用一次失败、一个空 Dataset 或一个被封的页面推出“没有数据”。

## 允许的配合能力

Apify 仍是主入口。目标站限制某种 crawler 时，可按证据需要使用：

- Scrapling、Scrapy、Crawl4AI、Firecrawl；
- Computer Use、网站自身 API、WordPress REST、WooCommerce API；
- sitemap、feed、页面源码、structured data。

这些路径的产出同样写 URL、访问日期、Actor/run/dataset 或替代方法，并进入 `## 搜索日志`。

## Evidence reference

搜索日志的能力名写 `apify_search`、`apify_fetch` 或实际 Actor 名，并尽量附：

- Actor slug；
- run ID；
- dataset ID；
- 查询或 URL；
- 返回条数与有用条数；
- 修复或替代路径。
