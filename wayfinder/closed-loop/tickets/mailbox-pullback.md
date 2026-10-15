---
wayfinder: task
status: open
assignee:
step: 4
blocked_by: [execution-log-flow, base-table-build, looker-dashboard]
---

# 邮箱 IMAP 回流

## Question

（HITL 取凭据 + AFK 写脚本）只读 `chester@de-linker.com`（腾讯企业邮 IMAP，依据 `wayfinder/feasibility/research/mailbox-readonly-access.md`）：

- 操作者在腾讯企业邮生成客户端专用密码（给清单），放两个仓库之外；vault 只记位置。
- 只读：`EXAMINE` + `BODY.PEEK`，绝不改标记、不移动、不删除；用 imap_tools 等成熟库。
- **L0 查证**：执行登记里的邮件条目，在「已发送」里找到对应邮件，回填查证列（补「执行登记流程」留下的「待邮箱接入后查证」）。
- **L1 送达**：退信（NDR）识别 → 未送达；无退信视为送达（写明这是推断）。
- **L2 回复**：按 Message-ID 对齐 `In-Reply-To` / `References`，排除自动回复。
- 只写「底表原型」定下的最小字段（不写正文）。共用定时与脚本层。
- 看板补邮件版面，更新 `docs/` 指南。

## 底表交接（「建底表」关票时写入，2026-10-14）

- 表结构正典 `schemas/base-table.schema.json`（列顺序、中文表头、下拉选项、翻译对照都在里面）；人读说明 `docs/base-table.md`。要改列先改 schema，再 `uv run scripts/base_table.py build --target main`，然后 `check --target main`。
- 脚本层：`scripts/base_table.py`，用 `uv run` 跑，依赖写在文件头（PEP 723）。新脚本放 `scripts/`，用同样的写法；也可以把函数加进这个文件。
- 配置：凭据读 `GOOGLE_APPLICATION_CREDENTIALS`，否则读 `~/.config/de-linker-playbook/service-account.json`。表格 ID 读 `PLAYBOOK_CONFIG`，否则读 `~/.config/de-linker-playbook/config.toml` 的 `[base_table] spreadsheet_id`。直接复用脚本里的 `load_target("main")` 和 `sheets_service()`。
- 目前脚本只会建表和核对，**还不会追加或更新数据行**；写行的函数由第一张需要它的票补上。正式表的写入要按每张表的不重复键去重，键见 `docs/base-table.md`「表结构」。
- 时刻列一律北京时间，格式「年-月-日 时:分」；网页表现、搜索词两张表的日期按太平洋时间。数据单元格都是纯文本格式，数字列除外。
- 「动作进度」每次回流后用 `action_progress` 整表重算。
- 本票相关：邮件反馈表的列见 schema `$defs.邮件反馈`，键是 登记编号 + 事件类型 + 回信 Message-ID。L0 查证要回填执行登记的「查证结果」「查证证据」「查证时刻（北京时间）」，把「待邮箱接入后查证」改掉。

## 完成标准

- 用一封真实已发信演练：执行登记 → 已发送里查到 → 底表 L0 查证为真；若有回复，L2 有行；脚本运行前后邮箱未读状态不变（抽查）。

## 每日提醒交接（「每日提醒」票写入，2026-10-15）

- 每天早上约 09:10，每日提醒会发一封信到 `chester@de-linker.com`（工作留痕）。发件人是日常账号的 QQ 邮箱，主题以「de-linker 下一步」开头，不带 `In-Reply-To`，`Message-ID` 的域名是 `de-linker-playbook.local`。
- 按归因规则，它对不上任何执行登记，本来就不会进邮件反馈表。脚本里还是明确跳过这类信，不要把它当成未归因来信去统计或报警。


## 执行登记交接（「执行登记流程」关票时写入，2026-10-15）

- **要回填的行**：执行登记里 渠道 = 邮件、查证结果 = 「待邮箱接入后查证」的行。它们的「邮件 Message-ID」「查证证据」「查证时刻（北京时间）」都是空的。登记由 `scripts/execution_log.py add`（流程 `skills/marketing-execution-log/SKILL.md`）写入，邮件查证一律交给本票，那个脚本不碰 IMAP。
- **能用来对上「已发送」的字段**：执行日期、收件公司（只有公司名，按设计不存收件人地址）、外展序列（`S-公司名`）、第几封、对应交付物（vault 里外展交付物的相对路径）。表里没有收件地址，要从对应交付物或 vault 的联系人交付物取地址、再到「已发送」里找；对不上的写「查证失败」并在证据里说明，不要猜。
- **怎么写回**：`base_table.read_table` 读「执行登记」，按 登记编号 改这几列后 `upsert_rows`（键是登记编号，其余列原样带回），写完 `refresh_progress`。查证结果：找到 → 「已查证」，证据一句话（如「在「已发送」里找到这封信」，不写正文和地址），查证时刻为北京时间「年-月-日 时:分」，并填 Message-ID。
- **编号格式**：`E-YYYYMMDD-NN`（如 `E-20261015-12`）；邮件反馈表按这个编号挂回。
- 现在正式表里还没有邮件行（67 条补登都是网站）。
