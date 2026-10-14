---
wayfinder: task
status: open
assignee:
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

## 完成标准

- 表格存在、三方可编辑；说明页能让初学者独立读懂每列。
- `<脚本> --check`（或等价）报告表结构与 `schemas/` 定稿一致。

## 交接

- 脚本目录、运行命令、配置读取方式，关票时写进「执行登记流程」「GSC 数据回流」「询盘回流 L3」「邮箱 IMAP 回流」四票正文。
