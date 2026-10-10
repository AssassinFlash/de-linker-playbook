---
name: marketing-email-outreach
description: >
  Use when the user asks for marketing-phase prospect list research,
  role-based email template library, lifecycle nurture sequence, drip
  campaign, 营销获客邮件, 潜客名单研究, 角色模板库, 生命周期培育,
  培育序列, or phase 4 acquisition work. Research real prospects,
  write sourced role templates and nurture sequences under
  deliverables/marketing/04-acquisition/. Read the ledger product_context
  first; invent no open rates or prospect URLs. Contact or email finder
  only if configured, else mark 联系人待补. Send only with a
  user-configured outbound tool; otherwise produce copy and do not send.
  Not for one-off cold emails, follow-up drafts, social posts, paid ads,
  转化文案库/首页成稿 (`marketing-copywriting`), or phase navigation.
---

# 邮件外展

根据已读产品上下文与可核验公开来源，做潜客研究、角色模板库与生命周期培育序列，落到 `deliverables/marketing/04-acquisition/email-outreach/`。未配置外发工具则只产出文案不发送。不做社媒帖、付费投放或阶段导航。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/` 的定位与竞品稿。已有 `deliverables/marketing/03-content/` 的 copy-library 或 snippets 对应 channel 行则复用其语气与 CTA，不另起价值主张。用户本轮给出的打开率、回复率、样品申请率、转化率或现用外发/CRM 一并列入。完成：能指出品类、目标市场、买家角色、差异化、样品与交期政策各依据哪几条；原文不拷进本仓库。品类或市场缺到无法圈定收件人则停并写缺口，不编造公司、指标或潜客。
3. **采集**。用网页搜索查证公开职业页、公司页、购买信号、冷邮件做法、培育基准与区域合规；需要原文时抓取指定 URL 的正文。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多公司并行时 dispatch a subagent, else do it inline。联系人/邮箱发现服务仅当用户已配置；否则邮箱与直拨字段标「联系人待补」，不编造。字段、查询意图与最低条数见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；潜客与公司达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据做角色切分、三层个性化、框架匹配、五条生命周期序列、时序与合规。角色从产品上下文取；上下文没有则在采购、指定人、承包、经销、项目方、进口商里选最贴近的一档，并标明「角色未在上下文出现，暂用」。量表与序列规格见 `references/methodology.md`。完成：每个角色有独立角度与一条主 CTA；每条序列有 trigger、goal、timing、exit，且每条 ≥4 触点、价值角度不重复（触点规则适用全部五条，不是另写跟进）；每个目标区域有合规说明或显式缺口。
5. **落盘**。写入下方路径。外发：用用户已配置的外发工具发信；未配置则只产出文案不发送。完成：主文档与两份工作簿非空；表每行 `source` 非空且含 URL 或「联系人待补」；终稿无未替换 `{{...}}`；教学支架原文零出现；文末 5–10 条可验证断言。用户明确收窄范围时，未做附件列入缺口，不算全量完成。

## 默认

- 本文件做营销获客阶段的名单研究、角色模板库与生命周期培育序列。单封成稿走 `lead-cold-email-gen`；无回复跟进走 `lead-followup-sequence`；已有成稿的发送编排走 `lead-email-sequence-strategy`。
- 策略与分析用简体中文；URL、字段名、subject line、CTA、文件名用英文。面客邮件跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。未列出的频道记缺口，不编造询盘或打开率。
- 打开率、回复率、点击率、转化率只写观察到的值；没有就写「公开源未找到」，禁止估计后写成事实。
- 禁止编造姓名、职位、公司或职业页 URL。搜不到的行标缺口或「联系人待补」。
- 查证用网页搜索；需要原文时抓取指定 URL。用户已配置网页采集服务时，可用它抓公开页。不写工具 ID。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 主题行：默认建议 2–4 词、小写、无标点技巧、无 emoji、无促销口吻、不塞收件人名；内部备忘录感优于推销感。A/B 变体可突破词数与大小写，仍须无促销口吻、无 emoji、不塞收件人名。
- 一封邮件一条主 CTA（要规格 / 要样品 / 要报价），不把多条行动叠在同一封。
- 不用 Dear Sir/Madam、I hope this email finds you well。开头接已核验的公司或项目信号。
- 每个角色单独一套角度与钩子，禁止一套模板打所有人。
- 个性化三层都要落到已采集证据：公司（项目、招聘、扩张）、角色（该职位痛点）、市场（目标市场的语气与合规）。这三层是模板库覆盖维度；单封成稿的深度下限（表层 / 深层）走 `lead-cold-email-gen`，本文件不按那套两层写首触成稿。
- 序列必须先写 trigger 与 exit，再写步数；询盘自动回复标为 1 小时内的第 1 步。
- 即时通讯入口（如 WhatsApp / WeChat）是否写入备选，以目标市场为准，不默认只走邮件。

## 产出

目录 `deliverables/marketing/04-acquisition/email-outreach/`（与 `marketing-acquisition`、编排依赖图对齐；主文件与工作簿同目录）：

- 主文件 `index.md`
- `prospect-research.xlsx`（从 `templates/prospect-research.xlsx` 复制后填；不能写表时改同目录 `prospect-research.json`）
- `sequence-builder.xlsx`（从 `templates/sequence-builder.xlsx` 复制后填；不能写表时改同目录 `sequence-builder.json`）
- 按需同目录：`email-templates.md`、`subject-line-variations.md`、`outreach-sequence.md`、`sequence-flows.md`、`trigger-events.md`、`automation-setup.md`、`personalization-guide.md`、`prospect-criteria.md`

章节、表列与最低行数见 `references/methodology.md`。

```markdown
# 邮件外展

- source: 台账 product_context（不粘贴原文）
- accessed:
- outbound_tool: configured | not_configured
- finder_service: configured | not_configured

## 目标买家

## 外展策略

## 冷邮件模板库

## 自动序列

## 合规

## 发送基础设施

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿：Prospects（≥50 行）、Target Companies（≥20 行）、Sequences（≥5 行）、Email Steps（≥25 行）、Variants（≥3 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

竞品调研与 New 均无冷邮件成稿语料，本节只借摩擦表一行的买家损失、「备线不是换商」定位与双闸形状，不借成稿原文。

用户要「给采购经理写冷邮件」。输入若写「我们是领先制造商，交期快、价格好，Dear Sir」。成稿应写成 2–4 词小写主题行、单一 CTA（要规格 / 要样品 / 要报价）、开场接已抓取公开页的公司或项目信号。痛点钩子只取摩擦表一行对应的作业损失：净价登录后才见 → 没法给自家客户报价；交期不绑定 → 班组与脚手架空转；库存只显示色点不是日期 → 不敢对客户承诺到货日；RMA 甩厂家 → 安装商自己当投诉窗口。不要把论坛里「卖家可不可信 / 交期改口 / 到货损谁认」的原句或用户名写进信，也不把主题簇安到未核验的这家公司头上。

第一单定位是备线开口，不写成换掉现有批发商；目录批发交货后沉默 vs 工程伙伴跟到调试，可作角色角度，禁止把库存或时效承诺当卖点，禁止自称制造商或备件库。安装商与 EPC 分模板：EPC 商务闸（价、交期、报价有效期是一口价风险工具）与技术闸（文件包、认证、兼容证据）成对，技术闸可否决商务闸，不要一套模板打所有人。序列先写 trigger 与 exit；询盘自动回复是 1 小时内第 1 步；样品后、订单后、再激活、展会不得省略。不写无来源的打开率。未配置外发则只产文案不发送。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文就套通用供应商开发信。
- 编造潜客、职业页 URL、打开率或回复率。
- 一套模板覆盖所有角色。
- 只写正文，不写主题行与 CTA。
- 序列无 trigger / exit，或连续天天发、不分层间隔。
- 目标市场未写合规（EU/UK 的 legitimate interest 与 opt-out、US 的物理地址、加拿大的同意期限）。
- 把未核验可用性的外发或核验工具写成已就绪。
- 未配置外发工具却写成已发送。
- 终稿留下未替换占位符。
- 用户只要一封可发送冷邮件、跟进稿或战役日历时，改走 `lead-cold-email-gen` / `lead-followup-sequence` / `lead-email-sequence-strategy`，不在本文件写首触成稿。
- 只做冷邮件，不做样品后、订单后、再激活或展会序列。
- 把教学例子或无来源假设当事实。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 潜客 ≥50、目标公司 ≥20，每条有可访问公开 URL 或已标「联系人待补」/缺口；`source` 无空值
- [ ] 5 套按角色区分的冷邮件模板（主题行 + 正文 + 单一 CTA）
- [ ] 5 条序列均有 trigger、goal、timing、exit；询盘自动回复为 1 小时内第 1 步
- [ ] 五条生命周期序列每条 ≥4 触点且价值角度不重复（触点规则适用全部序列，不是另写一条跟进）
- [ ] 每个目标区域有合规说明；基准数字有 URL 或「公开源未找到」
- [ ] 未配置发现服务的联系人已标「联系人待补」；未配置外发则未发送
- [ ] 主文档与工作簿在 `deliverables/marketing/04-acquisition/email-outreach/`；终稿无 `{{...}}`
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
