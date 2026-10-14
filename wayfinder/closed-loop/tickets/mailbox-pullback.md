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

## 完成标准

- 用一封真实已发信演练：执行登记 → 已发送里查到 → 底表 L0 查证为真；若有回复，L2 有行；脚本运行前后邮箱未读状态不变（抽查）。
