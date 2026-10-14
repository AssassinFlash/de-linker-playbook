---
wayfinder: task
status: closed
assignee: claude-code opus-5.5 (2026-10-14)
step: 1
blocked_by: []
resolved: 2026-10-14
---

# Cloud 项目与服务账号

## Question

（HITL：操作者在 Google 后台点，agent 给逐步清单并核对结果）在 `所有者账号` 下建 Google Cloud 项目与一个服务账号，供仓内脚本读 GSC、写底表（后续 GA4 Data API 也用它）。路径依据「Google 渠道接入路径」与「Google 账号现状清点」。

清单要覆盖（可用 `wizard` skill 生成交互式脚本，给初学者每步说明「这一步在干什么」）：

1. 本机 gcloud 当前登的是另一个账号（见现状清点），先切到 `所有者账号`，或全程在网页控制台操作。
2. 建项目（无组织）；启用 Search Console API、Google Sheets API、Google Drive API（共享表格时用）；GA4 Data API 等到「GA4 进看板」再启用。不需要结算。
3. 建服务账号；建一把 JSON 密钥，**放两个仓库之外**（如 `~/.config/de-linker-playbook/`，权限 600）。
4. 给 `日常账号` 加 IAM Owner。
5. 记录：项目 ID、服务账号邮箱、密钥文件路径、创建日期 → vault `deliverables/marketing/00-system/`（与现状清点同目录）；公开仓库只写「服务账号」。

## 完成标准

- 用密钥在本机跑通一次最小调用（如列出该服务账号可见的 Sheets / 调 Search Console `sites.list` 返回空列表不报鉴权错）。
- vault 有记录；两个仓库 `git status` 里无密钥文件。

## 交接

- 服务账号邮箱存放位置与密钥路径的约定，关票时写进「建底表」「GSC 数据回流」两票正文。服务账号加进 GSC 资源这一步在「GSC 数据回流」里做（那时资源已验证）。

## Resolution

> 真实值（项目 ID、服务账号邮箱、Key ID、账号）在私有 vault：`deliverables/marketing/00-system/cloud-service-account.md`。本文件只写角色名，不含密钥。

2026-10-14 完成。用户改为让 agent 代做：agent 用**独立的 gcloud 配置目录**（仓库外，`所有者账号` 登录，用户只在浏览器点一次「允许」）跑命令，本机全局 gcloud（`本机 gcloud 当前账号`）未动；用完撤销该登录并删除配置目录。

- **项目**：在 `所有者账号` 下新建（无组织、未开结算）。该账号下另有一个 Google 自动建的「My First Project」（2025-08-27），未动。
- **API**：Search Console、Sheets、Drive 三个已启用；另有 `iam` / `iamcredentials`（建服务账号与密钥必需）与 `serviceusage` / `servicemanagement`（平台自带的 API 开关）。坑：`gcloud projects create` 会自动启用 `cloudapis` 套件（BigQuery、Cloud Storage 等 21 个），已全部停用。GA4 Data API 未启用。
- **服务账号**：一个，项目里不给任何 IAM 角色（权限挂在 GSC 资源与表格上）。JSON 密钥由 `gcloud iam service-accounts keys create` 直接写到 `~/.config/de-linker-playbook/service-account.json`（目录 700、文件 600），没经过下载文件夹，内容未显示在任何输出里。
- **日常账号 IAM Owner**：命令行被拒（`SOLO_MUST_INVITE_OWNERS`：无组织项目授 Owner 只能走控制台邀请），改在控制台授予，日常账号已在邮件里接受（已进 IAM 策略）。接受后控制台提示「需要额外权限」，用户点了授予，日常账号因此另有「项目迁移者」角色（只管把项目移进组织，无组织时不起作用），用户裁定保留。
- **验证**：用该密钥直接调 Search Console `sites.list` → HTTP 200、空列表；Drive `files.list` → HTTP 200、空列表。两个仓库 `git status` 无密钥文件（密钥在仓库之外）。
- **交接**：邮箱存放位置与密钥路径约定已写进「建底表」「GSC 数据回流」两票正文。

顺带发现（未处理，不在本票范围）：Cloud 控制台顶部提示该账号下「有项目启用了 Gemini API 且 API 密钥未加限制」，不是本项目（本项目未启用 Gemini API），应是「My First Project」。
