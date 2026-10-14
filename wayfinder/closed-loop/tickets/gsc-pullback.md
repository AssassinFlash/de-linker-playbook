---
wayfinder: task
status: open
assignee:
step: 1
blocked_by: [gsc-site-access, cloud-service-account, execution-log-flow]
---

# GSC 数据回流

## Question

（AFK，开头一步 HITL）仓内脚本把 GSC 数据写进底表：收录（URL Inspection）→ L1；展示 → L1；点击 → L2。依据「Google 渠道接入路径」全文（`wayfinder/feasibility/research/google-channel-access.md`）。

- HITL 前置：操作者在 GSC 把服务账号加为用户（受限权限即可读）。给一步清单。
- 资源标识 `https://de-linker.com/`（带尾斜线），不是 `sc-domain:`。
- 查哪些 URL：执行登记里的 URL ∪ 站点地图里的 URL（URL Inspection 有每资源每日配额，按官方文档取值，超额时优先执行登记里的）。
- Search Analytics 按页 × 日期取展示 / 点击 / 排名；数据晚 2–3 天，脚本要可重跑、按日期幂等（不重复追加）。
- 定时：本票定一个方案并装好（如操作者 Mac 的 launchd，或服务 VPS 的 cron），写清怎么看它跑没跑、怎么停。断档风险记入 Resolution。

## 站点接入交接（「GSC 站点接入」关票时写入）

- 资源 `https://de-linker.com/`（网址前缀）2026-10-14 已验证：`所有者账号` = 验证所有者（经 Site Kit），`日常账号` = 委托所有者。真实账号见 vault `deliverables/marketing/00-system/gsc-owner-checklist.md`。
- 站点地图 `https://de-linker.com/sitemaps.xml`（SEOPress 索引，4 个子图 post / page / product / product_cat，共 301 条，去重后 297 个 URL，其中德语 149；`/blog/`、`/products/`、`/de/blog/`、`/de/produkte/` 这 4 个地址在不同子图里各出现两次）2026-10-14 提交，状态「成功」。查 URL 时站点地图集合以它为准。
- 加服务账号：GSC → 设置 → 用户和权限 → 添加用户 → 权限「受限」。`所有者账号` 或 `日常账号` 都能加（两者都是所有者）；浏览器里 `所有者账号` 在 GSC 的 URL 段是 `/u/1/`。
- GSC 数据从 2026-10-14 起开始积累（Site Kit 提示约 48 小时内为空）；回流脚本首跑若取不到数，先看日期范围是否早于此。

## 服务账号交接（「Cloud 项目与服务账号」关票时写入）

- 服务账号邮箱、项目 ID 记在 vault `deliverables/marketing/00-system/cloud-service-account.md`（HITL 前置「把服务账号加为 GSC 用户」时从那里抄邮箱）；公开仓库与脚本源码里不写死，脚本从密钥 JSON 的 `client_email` 读。
- 密钥路径约定：`~/.config/de-linker-playbook/service-account.json`（目录 700、文件 600，两个仓库之外）；脚本按「`GOOGLE_APPLICATION_CREDENTIALS` 优先，否则默认路径」读，配置读取方式以「建底表」定下的为准。
- Search Console API 已启用；作用域 `https://www.googleapis.com/auth/webmasters.readonly`。2026-10-14 已用该密钥调通 `sites.list`：HTTP 200、空列表——加进 GSC 之前就是空的，加完后应出现 `https://de-linker.com/`，这可作为加用户这一步的核对。
- 若脚本跑在服务 VPS 上（见「定时任务跑在哪」），密钥要拷到 VPS 的仓库外路径、权限 600，并在 vault 那份记录里补一行「另一份在哪」。

## HITL 前置已完成（2026-10-14）

- 服务账号已加进 GSC 资源 `https://de-linker.com/`。加的人是操作者，权限是**完整（Full）**：操作者宁可给多，免得以后再改。核对结果：用服务账号的密钥调 `sites.list`，返回 `https://de-linker.com/`，权限级别 `siteFullUser`。
- 脚本仍然只用 `webmasters.readonly` 作用域。所以就算 GSC 里给的是完整权限，脚本也只能读。本票开工时这一步不用再做。
- 同一天试调 `searchanalytics.query`（日期 2026-10-01 到 10-14）：0 行。这是正常的，因为数据从 2026-10-14 起才开始积累。

## 底表交接（「建底表」关票时写入，2026-10-14）

- 表结构正典 `schemas/base-table.schema.json`（列顺序、中文表头、下拉选项、翻译对照都在里面）；人读说明 `docs/base-table.md`。要改列先改 schema，再 `uv run scripts/base_table.py build --target main`，然后 `check --target main`。
- 脚本层：`scripts/base_table.py`，用 `uv run` 跑，依赖写在文件头（PEP 723）。新脚本放 `scripts/`，用同样的写法；也可以把函数加进这个文件。
- 配置：凭据读 `GOOGLE_APPLICATION_CREDENTIALS`，否则读 `~/.config/de-linker-playbook/service-account.json`。表格 ID 读 `PLAYBOOK_CONFIG`，否则读 `~/.config/de-linker-playbook/config.toml` 的 `[base_table] spreadsheet_id`。直接复用脚本里的 `load_target("main")` 和 `sheets_service()`。
- 目前脚本只会建表和核对，**还不会追加或更新数据行**；写行的函数由第一张需要它的票补上。正式表的写入要按每张表的不重复键去重，键见 `docs/base-table.md`「表结构」。
- 时刻列一律北京时间，格式「年-月-日 时:分」；网页表现、搜索词两张表的日期按太平洋时间。数据单元格都是纯文本格式，数字列除外。
- 「动作进度」每次回流后用 `action_progress` 整表重算。
- 本票相关：写网页收录、网页表现、搜索词三张表。把 Google 返回的英文值翻成表里的中文，用 `translate_inspection`、`translate_search_row`；「和上次比」用 `compare_with_previous` 算；登记编号用 `latest_registration` 按网址挂回执行登记。英文原值的确切写法以首次真实调用为准，对不上的落到「不在对照表里（看英文原文）」，再补进 schema 的 `x-map`。
- 按日期幂等：网页表现的键是 日期 + 网址 + 搜索类型 + 国家 + 设备，搜索词表的键再加搜索词；网页收录的键是 检查日期 + 网址。搜索词表因隐私会丢行，合计比网页表现少，这是正常的。
- 2026-10-14 `check --target main` 有一次读 Sheets 超时（`TimeoutError: The read operation timed out`），重跑就通过了。定时跑的脚本要设超时并重试，失败要记进日志，不能悄悄断掉。

## 完成标准

- 底表网页反馈表有真实行（至少一个页面的收录状态与近 7 天展示）；重跑一次不产生重复行；定时任务至少自动跑过一次（看日志）。
