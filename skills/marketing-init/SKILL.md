---
name: marketing-init
description: >
  Use when starting this marketing playbook for the first time,
  re-initializing the project, 初始化, 第一次跑, 重新初始化, or when
  asked to set up folders, config, or a product profile. Confirm
  both ledgers in state/ exist; ensure deliverables/marketing/ and
  deliverables/lead/ trees exist in this repo; keep product_context
  pointing at docs/fact-sources.md. Do not create an extra-repo
  output root, do not write a project-root config file, and do not use
  slash commands. If the product context is unreadable, open
  skills/marketing-profile/SKILL.md next; if ready, open
  skills/marketing-orchestrator/SKILL.md. Not for drafting copy, SEO
  audits, or running a campaign phase.
---

# 营销初始化

确认台账与本仓库交付目录就绪，并把产品指针指到事实所在。不在仓外建产出根，不另写公司档案。

## 步骤

1. **台账**。读两张台账：营销 `state/marketing-status.md`、获客 `state/lead-status.md`。完成：每张能报出存在或缺失，以及现有 `product_context`（若有）。缺失则记下缺口，不编造阶段表，不新建台账。
2. **交付目录**。确认下列目录在本仓库内存在，缺则创建，已有文件不删不改。完成：两棵树每个子目录都在。
   - `deliverables/marketing/`：`00-system`、`00-research`、`01-foundation`、`02-seo`、`03-content`、`04-acquisition`、`05-cro`、`06-growth`、`07-measurement`
   - `deliverables/lead/`：`00-system`、`01-icp`、`02-companies`、`03-contacts`、`04-market`、`05-usp`、`06-outreach`、`07-targeted`、`08-linkedin`、`09-seo`、`10-sales`、`99-archive`
3. **产品指针**。两张台账各自处理，仅当该台账存在时改键：`product_context` 缺失、为空或不是 `docs/fact-sources.md` 时写成 `docs/fact-sources.md`。检查该文件在本仓库内存在；需要隔离时 dispatch a subagent, else do it inline。完成：检查结果是「可读」或「不可读」；原文不写入本仓库。
4. **报告**。写入 `deliverables/marketing/00-system/init-report.md`，回复含「初始化完成」与下一步路径。完成：报告非空。任一台账缺失或上下文不可读 → `skills/marketing-profile/SKILL.md`；否则 → `skills/marketing-orchestrator/SKILL.md`。

## 默认

- 进度只认台账：营销 `state/marketing-status.md`，获客 `state/lead-status.md`，各管各的。
- 产出只进 `deliverables/`。
- 产品事实只指路、不复制。
- 下一步打开对应 `skills/<name>/SKILL.md`，不发明平行入口。

## 产出

```markdown
# 初始化报告

- marketing_ledger: 存在 / 缺失
- lead_ledger: 存在 / 缺失
- product_context:
- context_readable: 是 / 否
- marketing_dirs: 齐 / 列出缺口
- lead_dirs: 齐 / 列出缺口
- next: skills/.../SKILL.md

初始化完成。
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是仓库初始化，例子教目录与台账形状不教营销内容，无对应事实源材料可借，保留通用支架。

台账已在、获客树缺 `08-linkedin`。只补建该空目录，不改台账其它键，报告写「初始化完成」，下一步打开 `skills/marketing-orchestrator/SKILL.md`。

## 易错

- 在仓外建产出目录，或改写已有交付物。
- 把产品原文拷进本仓库，或另写一份公司档案。
- 用斜杠命令名当入口，而不打开 `skills/<name>/SKILL.md`。
- 覆盖已有台账的阶段表。
- 只建营销树、不建获客树，或只建当前会用到的子目录。

## 清单

- [ ] 已读或已报告缺失 `state/marketing-status.md` 与 `state/lead-status.md`
- [ ] `deliverables/marketing/` 与 `deliverables/lead/` 子目录齐全
- [ ] 两张台账的 `product_context` 都是 `docs/fact-sources.md`
- [ ] 未把产品原文写入本仓库
- [ ] `deliverables/marketing/00-system/init-report.md` 含「初始化完成」与下一步路径
- [ ] 例子原文未进入交付物
