---
wayfinder: task
status: open
assignee: claude-opus-5 (1m) 会话 2026-10-27（重跑）
step: 1
blocked_by: [gsc-site-access, cloud-service-account, base-table-build]
---

# GSC 数据回流

> **2026-10-27 用户裁定：上一轮执行不算数。本票按「从未执行」重跑。**
>
> 上一轮（2026-10-14 至 10-19）的全部进展与结论已移到文末「作废的上一轮」，只作参考；
> 其中的**交接事实**（服务账号、站点地图、底表结构、执行登记挂回）仍有效，因为它们来自别的票，
> 但凡是「跑通了 / 已验证 / 可以关票」这类结论一律不采信，本票重新取证。

## Question

（AFK，开头一步 HITL）仓内脚本把 GSC 数据写进底表：收录（URL Inspection）→ L1；展示 → L1；点击 → L2。依据「Google 渠道接入路径」全文（`wayfinder/feasibility/research/google-channel-access.md`）。

- HITL 前置：操作者在 GSC 把服务账号加为用户（受限权限即可读）。给一步清单。
- 资源标识 `https://de-linker.com/`（带尾斜线），不是 `sc-domain:`。
- 查哪些 URL：执行登记里的 URL ∪ 站点地图里的 URL（URL Inspection 有每资源每日配额，按官方文档取值，超额时优先执行登记里的）。
- Search Analytics 按页 × 日期取展示 / 点击 / 排名；数据晚 2–3 天，脚本要可重跑、按日期幂等（不重复追加）。
- 定时：本票定一个方案并装好（如操作者 Mac 的 launchd，或服务 VPS 的 cron），写清怎么看它跑没跑、怎么停。断档风险记入 Resolution。

## 重跑怎么做（2026-10-27 起，本票的唯一执行顺序）

1. **从零复核前置**：凭据可用、服务账号在资源里的权限、站点地图现状、底表结构与 schema 一致。四项都当场取证，不引用旧进展。
2. **建今天的全量基线**：对「执行登记 ∪ 当前站点地图」的每个网址强制查一次收录，写进今天这一天的行；已有的旧行按 `检查日期 + 网址` 覆盖，不新增重复。
3. **取搜索表现**：最近 10 天（太平洋时间）的展示 / 点击 / 排名 / 搜索词，按日期幂等写表。
4. **验链路**：数字能挂回执行登记编号 → 动作进度重算 → `next_step.py` 能据此给出下一步。挂不回去的要写明原因。
5. **验定时**：定时任务实际按点运行，日志无缺日，失败会留痕。
6. 六步都过、且下面五条验收标准全中，才允许关票。

## 验收标准（2026-10-27 收紧，取代上一轮的口径）

1. **网页收录**：当前站点地图 ∪ 执行登记的每个网址，都有**今天**这一天的检查行；`(检查日期, 网址)` 重复键 = 0。
2. **网页表现**：近 7 天里，至少一个**内容页**有展示，**且该行挂得到登记编号**（空编号的展示行不算数）。
   内容页 = 法律页以外的页面，首页（`/`、`/de/`）、博客、产品、方案、分类都算；Impressum、Datenschutz、条款这类法律页被搜到不算「内容开始有流量」。判定用 `scripts/base_table.py` 的 `is_content_page()`，`next_step.py` 的 `site.content_impressions_7d` 就是这个数。
3. **点击（L2）**：至少有一行真实点击数据；若确实还没有，要给出可核对的证据（GSC 侧无点击记录），不能只写「0 行」。
4. **幂等**：紧接重跑一次，不产生新行、不产生重复。
5. **定时**：连续 7 天按点运行，日志无缺日。缺一天即不通过，先修定时再重算。

> 上一轮之所以被判不算数：唯一一行展示来自 `/de/impressum/` 的查询词 `linker`，点击 0、登记编号为空，挂不回任何动作；收录 13 天基本没涨；定时链 10-22、10-23 两天整条没跑。这些都不满足上面的第 2、3、5 条。

## 重跑进展

### 2026-10-27

- 复核 1／4 凭据与资源：服务账号密钥 `~/.config/de-linker-playbook/service-account.json`（600）。`searchconsole.sites.list` 返回 `https://de-linker.com/`，权限 `siteFullUser`。**通过。**
- 复核 2／4 站点地图：`https://de-linker.com/sitemaps.xml` 4 个子图，`post 22 + page 49 + product 172 + product_cat 20 = 263` 个网址。上一轮记录是 297 个，**少了 34 个**，原因待查（产品下架或地图重建）。
- 复核 3／4 底表结构：`uv run scripts/base_table.py check --target main` → `OK structure matches schema`。**通过。**
- 复核 4／4 数据归属：见下条。

### 重跑过程中查到的四件事

1. **检查集比表里小得多**：底表有 370 个网址，当前该查的是 274 个（站点地图 259 ∪ 执行登记 68）。差的 96 个是已下架的旧网址（如 `/de/produkt/ecoflow-…-einphasiger-hybridwechselrichter/`），不再检查，历史行保留。
2. **4 个 category 归档页是口径冲突，不是故障**：它们不在站点地图里，线上也确实是 `follow, noindex`——站点有意不收录。但它们在执行登记里（`E-20261015-34/35/36/38`），所以规则引擎按 W-04 判成 P2「应被收录」。要么站点改为收录，要么在执行登记里标注「不要求收录」让 W-04 不再报。**需要操作者裁定。**
3. **3 个德语页才是真问题**：`/de/`、`/de/produkte/`、`/de/fuer-epc/` 都在站点地图内，线上是 `index, follow`，但 Google 上次抓取停在 7 月（那时是 noindex）。需要在 GSC 各请求编入索引一次。
4. **定时链断过两天**：10-22、10-23 日志里没有任何记录，整条链没跑（不是失败，是没触发）。原因未定，先记为断档。
5. **那 96 个旧网址不是都干净退场**：77 个 301、**19 个 404**。404 的全是旧德语产品 slug（如 `/de/produkt/ecoflow-ocean-2-batterie-5-02-kwh-ef-bd-5-s2/`），而对应的英文 slug 反而 301 到 `/?post_type=product&p=NNNN` 再跳一次。这属于站点侧问题，本票只记录，不改站。

### 收录与展示现状（重跑前）

- 登记过的 68 个网址里：已收录 24、Google 还不知道 16、已发现未抓 16、被 noindex 挡 7、已抓未收 4、跳转 1。
- 近 7 天展示 1 行：`/de/impressum/`，查询词 `linker`，点击 0，登记编号为空——**不满足验收第 2 条**。
- 点击从未出现过任何一行——**不满足第 3 条**。

### 2026-10-27 操作者裁定：4 个分类归档不要求收录

- 决定：保持 noindex，在执行登记里标成「不要求收录」，W-04 不再报。
- 已写进表：`E-20261015-34/35/36/38` 四行的备注追加「不要求收录（操作者 2026-10-27 定）」。
- 已改脚本：`next_step.py` 判「应被收录」时读这条备注，命中的页进台账「被 noindex 挡住（执行登记标了不要求收录）」而不是排队；`execution_log.py` 新增 `note --id … --note …`，只追加备注、不查证。
- 已同步文档：`docs/feedback-rules.md`（「应被收录」的判断加例外）、`docs/base-table.md`（备注固定标记）。
- 效果核对（同日 `next_step.py --format json`）：W-04 的「4 个登记过的页」消失，台账里 4 个网址归入不要求收录；W-04 现在只剩「在 GSC 给 3 个登记过的页各请求编入索引一次」——`/de/`、`/de/fuer-epc/`、`/de/produkte/`。

### 2026-10-27 三个德语页已在 GSC 请求编入索引（操作者授权 AI 代点）

- 环境：opencli 浏览器桥（用户在 Chrome 里已登录 GSC，`857558227@qq.com`），先跑 `opencli daemon restart` 把扩展连上。
- 过程：网址检查 → 实际测试 → 请求编入索引。三个页面的实际测试都通过（`/de/` 显示「网址可编入 Google 索引」）；提交后 GSC 都显示「已请求编入索引 · 已将网址添加到优先抓取队列中」。
  - `https://de-linker.com/de/`：之前已有一次请求，这次是再次提交。
  - `https://de-linker.com/de/fuer-epc/`：上次抓取停在 2026-07-26，站点地图一栏显示「临时处理错误」。
  - `https://de-linker.com/de/produkte/`：上次抓取停在 2026-07-28。
- 登记：`E-20261027-01`（`/de/`）、`E-20261027-02`（`/de/fuer-epc/`）、`E-20261027-03`（`/de/produkte/`），内容说明都含「在 GSC 请求编入索引」，查证结果「已查证」，证据写明代点与页面提示。
- 核对：`next_step.py` 重跑后，这三页不再出现在 W-04；W-04 只剩 3 个**未登记**页面的 P3 提醒（`/de/loesung/heimspeicher/`、`/de/produkt/saj-hs3-12k-t2-w-p/`、`/de/verkaufsbedingungen/`）。
- 另外发现：GSC「网页」报告里「被 noindex 标记排除」的有 **1,470** 个网址，抽样看全是商品筛选/搜索参数页（`?s&post_type=product&brand=…`），属有意不收录，不是故障。

### 2026-10-27 另外三个未登记页（操作者：先核存在，存在就请求）

- 核存在：三页都是 HTTP 200、`index, follow`、canonical 指向自己、标题正常。
  - `/de/loesung/heimspeicher/`「Heimspeichersysteme für Installateure | Linker」
  - `/de/produkt/saj-hs3-12k-t2-w-p/`「SAJ HS3-12K-T2-W/G-PX | Linker」
  - `/de/verkaufsbedingungen/`「Verkaufsbedingungen (B2B) | Linker」
- GSC 逐页请求编入索引，三页都出现「已请求编入索引 · 已将网址添加到优先抓取队列中」。
- 登记：`E-20261027-04`、`E-20261027-05`、`E-20261027-06`。
- 核对：`next_step.py` 重跑后 **W-04 完全清零**——6 个页面都已有待重抓请求。

### 2026-10-27 强制全量重查（完成）

- 11:04–11:37，对 274 个网址强制重查（`--recheck`）。
- 取到：网页收录 274 行；网页表现 2 行、搜索词 2 行（太平洋时间 2026-10-17 至 10-26）。
- 写入：网页收录 新增 0 / 覆盖 82；网页表现 新增 1；搜索词 新增 1；动作进度重算 75 行；无错误。
- 幂等复跑（11:39，不带 `--recheck`）：三张表都是新增 0 / 覆盖 0，今天已查 274、待查 0。
- 复核：今天有检查行的网址 274/274；`(检查日期, 网址)` 重复键 **0**。

### 验收五条现状（2026-10-27 11:40）

| # | 标准 | 现状 |
| --- | --- | --- |
| 1 | 今天每页有检查行、重复键 0 | **通过**：274/274，重复 0 |
| 2 | 近 7 天至少一个**内容页**有展示且挂得到登记编号 | **未通过**：`content_impressions_7d = 0`。10-26 `/de/datenschutz/` 展示 1、点击 0、有登记编号 `E-20261019-04`，但它是法律页，按操作者 2026-10-27 的口径不算；10-25 `/de/impressum/` 同样不算 |
| 3 | 点击（L2）至少一行真实数据 | **未通过**：仍为 0 |
| 4 | 紧接重跑不产生新行、不重复 | **通过** |
| 5 | 定时连续 7 天按点运行、日志无缺日 | **未通过**：10-22、10-23 断档，且从今天起才重新计数 |

**结论：票不关。** 卡在 2、3、5。第 2 条按操作者 2026-10-27 的口径改成「内容页出数才算」——只有法律页不算，首页（`/`、`/de/`）算内容页；当前 `content_impressions_7d = 0`。

### 2026-10-27 排查：20 个「已抓取、尚未收录」的页

逐页查了 URL Inspection API、抓了线上正文、算了同族相似度：

- **14 个产品页**：核心正文 689–1,509 词，HTTP 200、canonical 指向自己。同族页面彼此 5-gram Jaccard 相似度 0.60–0.75（HS3-6K/8K/10K 0.71–0.75；H2-20K/25K/30K 0.60–0.69）。Google 抓过，判断为近似重复，只留家族代表页。**这不是故障**，是变体页的正常命运。另：产品页全部没有 meta description。
- **3 篇博客清单文**（780–830 词）：英德两版都没进索引，德文版连抓取记录都没有。属内容深度与站点权重不足，不是技术故障。
- **3 个工具页**：`/de/genie/`（Genie 工作区入口，未登录看到登录墙）、`/contact/`、`/about/capability/`，三个都在站点地图里。英文 `/genie/` 已被 Google 收录。**2026-10-27 操作者裁定：Genie 是产品入口，允许被收录**——不做 noindex、不从站点地图移除；为此开的 PR #685 已关闭。德文版「已抓取、未收录」是内容薄 + 站点权重低的**排名**问题，不是「不该被收录」，正路是把页面内容做厚。
- **一处不一致**：`/de/produkt/saj-hs3-8k-t2-w-p/` 等 3 个德语产品页在站点地图里，URL Inspection API 报「URL is unknown to Google」，而 GSC 站点地图报告是「10-26 读取成功、263 个网页被发现」。两个口径对不上，待再核。后经核查：这三个 URL 是 #254 德语地址迁移的旧地址，301 到当前 slug，当前 slug 本来就在站点地图里——不是缺陷，是比对时跟了跳转。

### 2026-10-27 分类归档进站点地图（操作者要求）

- 根因在生产设置，不在仓库代码：`seopress_titles_option_name.tax_titles.category.noindex = "1"`（所有分类归档 noindex）、`seopress_xml_sitemap_option_name.taxonomies_list.category.include = ""`（分类整类不进 sitemap）。
- 修复：新站仓库 PR #687（可重复执行的迁移工具 + 10 个单测）合并后，对生产执行 11 项写入（9 个 term 设 `_seopress_robots_index=yes`：4 组旧归档英德各一 + uncategorized；2 个开关：tax.noindex 清空、sitemap.include 置 1）。备份 `~/de-linker-data/backups/category-sitemap-20261027.json`，读回全部一致。
- 结果：`sitemaps.xml` 新增 `category-sitemap1.xml`，只含 `/category/monitoring-energy-management/` 与 `/de/kategorie/ueberwachung-energiemanagement/`，两页 `index, follow`；其余 4 组保持 `follow, noindex`、不进地图。重跑迁移为 `nothing to do`。

### 2026-10-27 全量「请求编入索引」：配额与队列（操作者要求全站都点）

- **实测配额约 10 个/资源/天**：当天第 11 个开始，GSC 直接提示「超出了配额」。
- 今天成功 10 个：早上 6 个（`/de/`、`/de/fuer-epc/`、`/de/produkte/`、`/de/loesung/heimspeicher/`、`/de/produkt/saj-hs3-12k-t2-w-p/`、`/de/verkaufsbedingungen/`）+ 下午 4 个（`/`、`/product/saj-hs3-8k-t2-w-p/`、`/product/saj-h2-25k-t3/`、`/category/monitoring-energy-management/`），登记 `E-20261027-01` 至 `-11`。
- 队列按操作者 2026-10-27 定的优先级排：① Google 还不知道的 32 个 → ② 已抓取、尚未收录的 18 个 → ③ 其余 203 个，共 253 个。名单在仓外 `~/.config/de-linker-playbook/gsc-request-queue.txt`（600）。
- 排除：4 组不要求收录的分类归档（含德语 twin）、购物车、旧址 301、今天已请求的。
- 按每天约 10 个推进，约 26 天跑完；每批完成后把新请求的 URL 与登记编号追加到本节。

## 数据怎么处理（重跑时定的口径）

底表里已有的行（网页收录约 2900 行、网页表现 1 行、搜索词 1 行）**不清空**：它们是 Google 侧的真实观察记录，URL Inspection 查不了过去，删了补不回来。重跑的含义是**不采信上一轮的结论、重新取证并覆盖今天的行**，不是销毁历史。今天的强制全量检查按 `检查日期 + 网址` 覆盖同一行，不会新增重复。

## 交接（来自其他票，仍然有效）

### 站点接入交接（「GSC 站点接入」关票时写入）

- 资源 `https://de-linker.com/`（网址前缀）2026-10-14 已验证：`所有者账号` = 验证所有者（经 Site Kit），`日常账号` = 委托所有者。真实账号见 vault `deliverables/marketing/00-system/gsc-owner-checklist.md`。
- 站点地图 `https://de-linker.com/sitemaps.xml`（SEOPress 索引，4 个子图 post / page / product / product_cat）2026-10-14 提交，状态「成功」。查 URL 时以它为准。
- 加服务账号：GSC → 设置 → 用户和权限 → 添加用户 → 权限「受限」。`所有者账号` 或 `日常账号` 都能加（两者都是所有者）；浏览器里 `所有者账号` 在 GSC 的 URL 段是 `/u/1/`。
- GSC 数据从 2026-10-14 起开始积累（Site Kit 提示约 48 小时内为空）；回流脚本首跑若取不到数，先看日期范围是否早于此。

### 服务账号交接（「Cloud 项目与服务账号」关票时写入）

- 服务账号邮箱、项目 ID 记在 vault `deliverables/marketing/00-system/cloud-service-account.md`（HITL 前置「把服务账号加为 GSC 用户」时从那里抄邮箱）；公开仓库与脚本源码里不写死，脚本从密钥 JSON 的 `client_email` 读。
- 密钥路径约定：`~/.config/de-linker-playbook/service-account.json`（目录 700、文件 600，两个仓库之外）；脚本按「`GOOGLE_APPLICATION_CREDENTIALS` 优先，否则默认路径」读。
- Search Console API 已启用；作用域 `https://www.googleapis.com/auth/webmasters.readonly`。2026-10-14 已用该密钥调通 `sites.list`。

### 底表交接（「建底表」关票时写入）

- 表结构正典 `schemas/base-table.schema.json`；人读说明 `docs/base-table.md`。要改列先改 schema，再 `uv run scripts/base_table.py build --target main`，然后 `check --target main`。
- 脚本层：`scripts/base_table.py`，用 `uv run` 跑，依赖写在文件头（PEP 723）。
- 配置：凭据读 `GOOGLE_APPLICATION_CREDENTIALS`，否则读 `~/.config/de-linker-playbook/service-account.json`。表格 ID 读 `PLAYBOOK_CONFIG`，否则读 `~/.config/de-linker-playbook/config.toml` 的 `[base_table] spreadsheet_id`。复用 `load_target("main")` 和 `sheets_service()`。
- 时刻列一律北京时间，格式「年-月-日 时:分」；网页表现、搜索词两张表的日期按太平洋时间。数据单元格都是纯文本格式，数字列除外。
- 「动作进度」每次回流后用 `action_progress` 整表重算。
- 本票相关：写网页收录、网页表现、搜索词三张表。翻译用 `translate_inspection`、`translate_search_row`；「和上次比」用 `compare_with_previous`；登记编号用 `latest_registration` 按网址挂回执行登记。
- 幂等键：网页表现 = 日期 + 网址 + 搜索类型 + 国家 + 设备；搜索词再加搜索词；网页收录 = 检查日期 + 网址。搜索词表因隐私会丢行，合计比网页表现少，属正常。

### 执行登记交接（「执行登记流程」关票时写入）

- 正式表已有执行登记（`E-YYYYMMDD-NN`）。回流按网址挂回登记编号；没登记的网址编号留空。
- 新登记由 `scripts/execution_log.py`（流程 `skills/marketing-execution-log/SKILL.md`）写。

## 作废的上一轮（2026-10-14 至 10-19，用户 2026-10-27 裁定不算数）

<details>
<summary>展开：上一轮写了什么（只作参考，不当结论）</summary>

- 2026-10-14：服务账号已加进 GSC 资源，权限完整（Full）；`sites.list` 返回 `siteFullUser`。试调 `searchanalytics.query`：0 行。
- 2026-10-14 23:25–10-15 00:04 首跑：网页收录 297 行；已收录 62、未收录 148、未知 87；网页表现与搜索词 0 行。
- 2026-10-15：重跑限查 3 个网址，299 行、299 个不重复键；1 个网址 Google 500 重试仍失败，记日志。
- 2026-10-15：launchd 装好，每天 08:30，与询盘、邮箱、看板、每日提醒串成一条链。
- 2026-10-19：10-17 至 10-19 连续三天失败——「网页收录」写到第 1001 行被 Sheets 拒绝（grid limits）。修复：`base_table.py` 加 `ensure_grid` 自动扩行；手动重跑新增 312 行。
- 当时结论：网页表现、搜索词仍 0 行，票不能关，等 GSC 出数。

**用户 2026-10-27 判定这些不算数的理由**：唯一一行展示来自 `/de/impressum/` 的 `linker`（点击 0、登记编号为空、挂不回动作）；收录 13 天从 62 到 62 基本没动；4 个登记页线上仍是 noindex、3 个页面待请求编入索引；定时链 10-22、10-23 两天整条没跑，日志无记录。

</details>
