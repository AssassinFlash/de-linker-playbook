---
wayfinder: task
status: closed
assignee: claude-opus-5-5 会话 2026-10-14（用户要求与「底表原型」一并做）
step: 1
blocked_by: [base-table-prototype, cloud-service-account]
---

# 建底表

## Question

（HITL + AFK）按「底表原型」定稿建出真实的 Google 表格。

- 操作者用 `所有者账号` 新建空表格（服务账号建文件可能受 Drive 存储配额限制〔未证实，本票先查官方文档〕；默认由人建），共享给 `日常账号`（编辑者）与服务账号（编辑者）。
- agent 用服务账号按定稿建各工作表、表头、说明页、数据验证（下拉选项）、冻结首行；写一个仓内脚本完成这一步，可重跑、不清已有数据。
- 表格 ID 与链接记 vault（`deliverables/marketing/00-system/`）；脚本从仓库外的配置读表格 ID（配置位置与密钥同处，或环境变量），公开仓库不出现 ID。
- 本票是第一张写脚本的票：**定下脚本放哪、用什么运行**（建议 Python + uv，与新站服务一致；须任何 harness 一条命令能跑），写进 `README.md` 或 `docs/`，后续脚本票照用。

## 服务账号交接（「Cloud 项目与服务账号」关票时写入）

- 服务账号邮箱、项目 ID 记在 vault `deliverables/marketing/00-system/cloud-service-account.md`；公开仓库与脚本源码里不写死，脚本从密钥 JSON 的 `client_email` 字段读即可。
- 密钥路径约定：`~/.config/de-linker-playbook/service-account.json`（目录 700、文件 600，两个仓库之外）。脚本按「环境变量 `GOOGLE_APPLICATION_CREDENTIALS` 优先，否则用这条默认路径」读；表格 ID 等配置放同一目录（如 `~/.config/de-linker-playbook/config.toml`）。
- 已启用 Sheets API、Drive API（项目里没有别的业务 API，不开结算）；作用域用 `https://www.googleapis.com/auth/spreadsheets`（必要时加 `drive`）。2026-10-14 已用该密钥调通 Drive `files.list`（空列表）。
- 共享表格时在「共享」里填服务账号邮箱，给**编辑者**。服务账号在项目里没有任何 IAM 角色，也不需要。

## 完成标准

- 表格存在、三方可编辑；说明页能让初学者独立读懂每列。
- `<脚本> --check`（或等价）报告表结构与 `schemas/` 定稿一致。

## 交接

- 脚本目录、运行命令、配置读取方式，关票时写进「执行登记流程」「GSC 数据回流」「询盘回流 L3」「邮箱 IMAP 回流」四票正文。

## Resolution（2026-10-14）

- 两本 Google 表格，都由 `所有者账号` 建，并以编辑者共享给 `日常账号` 和服务账号：「底表」（正式）和「底表（样例）」（假数据）。链接和 ID 记在 vault `deliverables/marketing/00-system/base-table.md`。服务账号建文件这条路没试；按默认由人建。
- 脚本 `scripts/base_table.py`，用 Python + uv 跑，依赖写在文件头（PEP 723），任何 harness 一条命令能跑。运行说明在 `docs/base-table.md`，`README.md` 和 `AGENTS.md` 都指向 `scripts/`。
  - `uv run scripts/base_table.py build --target main|sample`：建或补结构，包括首页、每张表后的说明页、表头、下拉、冻结行列、换行、纯文本格式。可重跑，正式表的数据行不动；表头与 schema 不符且已有数据时停下报错。
  - `uv run scripts/base_table.py check --target main|sample`：核对结构与 `schemas/base-table.schema.json`，不一致退出码 1。2026-10-14 两本都是「OK structure matches schema」。
- 配置：凭据先看 `GOOGLE_APPLICATION_CREDENTIALS`，否则读 `~/.config/de-linker-playbook/service-account.json`。表格 ID 先看 `PLAYBOOK_CONFIG`，否则读 `~/.config/de-linker-playbook/config.toml`（600）的 `[base_table] spreadsheet_id` / `sample_spreadsheet_id`。公开仓库不出现 ID。
- 验证：build 跑两遍结果一样；在正式表写一行测试数据，重跑 build 后仍在，之后删掉。操作者 2026-10-14 确认说明页看得懂。
- 正式表目前只有结构，没有数据。真实数据由各回流票写入。
