---
wayfinder: task
status: open
assignee:
step: 1
blocked_by: []
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
