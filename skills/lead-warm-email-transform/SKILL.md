---
name: lead-warm-email-transform
description: >
  Use when rewriting existing cold emails into warmer buyer-centric
  outreach, reducing sales tone, transforming drafted emails, or when
  the user mentions warm email, rewrite email, soften email, 暖邮件,
  邮件改写, 邮件转化, 改写成暖邮件, 太冷了, 去掉自我推销, or warm
  outreach, including phase 6 of this repo's lead run. Scan forbidden
  phrases, replace generic quality-and-price claims with operational
  value from product context, add a verifiable buyer-context hook, and
  close with low-friction A/B/C CTAs. Read ledger product_context and
  deliverables/lead/06-outreach/cold-emails.md when present; invent no
  market events or numbers. Not for writing cold emails from scratch,
  follow-up sequences, or sending mail.
---

# 暖邮件改写

把已有冷邮件改写成买家视角、可核验钩子、低摩擦 CTA 的暖外展，写入 `deliverables/lead/06-outreach/warm-emails.md`。禁用语与替换逻辑见 `references/forbidden-phrases.md`。缺证据标缺口，不编造。

## 步骤

1. **输入**。读 `skills/marketing-playbook-standards/SKILL.md`（存在则读）。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：已批准的 `deliverables/lead/06-outreach/cold-emails.md`，或用户本轮粘贴的原文冷邮件。二者都没有、且无 `user_waiver` → 停并写缺口。软依赖存在则读：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/04-market/competitor-positioning.md`、`deliverables/lead/05-usp/product-knowledge.md`。买家、原文、品类仍缺到无法下笔时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则本轮最多问两问，不另写问卷。完成：能指出每封原文、品类、买家角色各依据哪份文件或本轮消息；原文不拷进本仓库。

2. **收齐改写字段**。对每封待改写邮件记下四项：原文；品类（产品上下文）；买家角色（职位 + 行业 + 区域，优先 ICP）；一条买家情境线索（扩张 / 新品 / 旺季 / 合规压力 / 其他已核验公开事实）。品类与角色已在上游出现则不重问。用户收窄范围则只改指定的；否则上游每封冷邮件一则。完成：每封四项都有来源；线索来源已标为产品上下文、本轮消息、拟查证，或「suggested context — verify before sending」。

3. **扫描禁用语**。读 `references/forbidden-phrases.md`，按精确 / 语义 / 部分匹配扫描原文（含译文套话）。开场公司自我介绍、空泛「质量+价格」、催更、正式敬语一并列入替换表。完成：每封有替换记录（命中语 → 失败原因 → 拟替换方向）；无命中也写「无禁用语，仍按五段结构改写」。

4. **查证钩子**。凡改写里写成「对方公司刚发生 X」或引用行业事件、统计、交期/不良率/证书：用网页搜索查证；需要原文则抓取指定 URL。数字、证书、案例只来自产品上下文、用户本轮或已抓取页。搜不到的公司新闻不得写进正文，改标「suggested context — verify before sending」或删掉该钩子、改用已核验的角色/行业观察。搜索不可用：不编造事件；钩子改为已有上游事实，或停止该封并写缺口。多封且需隔离查证时 dispatch a subagent, else do it inline；单封 inline。完成：每封钩子有 URL、产品上下文字段、或缺口标记。

5. **改写**。按「写法」五段重写；叙事从「我想卖给你」转到「我了解到一件可能帮你在市场上赢的事」。用上下文里的运营事实替换空泛质量/价格；没有数字写「未在上下文出现」，禁止填未核验百分比。CTA 用 A/B/C 或等价低摩擦三选一。每封 <200 词。面客语用买家语言（缺省英语），同一封不混用。完成：每封含五段；禁用语表零命中；含数字的句子有来源或已标缺口。

6. **落盘**。写入下方模板。每则含 Warm Email Rewrite、Why These Changes Work（至少三条：删了什么、加了什么、预期作用，作用只写本文件机制：作业信号 / 降低决策成本 / 可选价值 / 运营具体性，不发明心理学名词）、禁用语替换记录、需按收件人再定制的部分。可加一句冷版本 vs 暖版本的 A/B 备注。只产文案，不发送。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批。完成：主文件非空；输入几封就几则；教学支架原文零出现。

## 默认

- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止并写缺口，不编造。
- 外发工具仅当用户已配置；未配置则只产文案不发送。本 skill 默认不发送。
- 进度只认台账。产出只进 `deliverables/lead/06-outreach/`。
- 下游跟进应继续遵守本文件暖化原则：`skills/lead-followup-sequence/SKILL.md`、`skills/lead-email-sequence-strategy/SKILL.md`（文件存在时）。暖化稿在发送序列中的优先级以 `lead-email-sequence-strategy` 为准（有暖化则暖化作默认 Day 0，冷稿作 A/B 或回退）；本文件不另排战役日历。从零写冷邮件走 `skills/lead-cold-email-gen/SKILL.md`，不走本文件。
- 买家心理背景可读 `skills/lead-buyer-psychology/SKILL.md`（文件存在时）；不存在则只用本文件四条机制，不编造理论名。

## 写法

- 每句用这面镜子：这是在帮对方赢，还是在介绍自己。
- 五段结构（每封都要，顺序固定）：
  1. **买家情境钩子** — 对方业务、市场事件或品类动作；必须可核验。
  2. **为何找到他们** — 与职位/行业挂钩的观察，证明相关。
  3. **一条小而有用的洞察** — 变化、风险、基准、合规或成本因素。
  4. **轻量有用提议** — 样品 / 规格 / 案例 / 低风险试单；自称只出现在本段，且必须接可核验运营事实。
  5. **低摩擦 CTA** — 「If helpful, I can send A focused on ___, B focused on ___, or C ___ — which fits better?」三选项降低决策成本。
- 五段是结构，不是套话。禁止邮件合并口吻、禁止堆功能清单。
- 开场不写公司简介。空话（leading、high quality、competitive price、best-in-class）无证据则删。
- 不催促（limited time、act now、don't miss out）；不乞求（I'd really appreciate、It would mean a lot）；不问高承诺（先要约电话/会议）除非已经给了可带走的东西。
- 正式敬语（Dear Sir/Madam、To Whom It May Concern、尊敬的先生/女士）改为有名则直呼，无名则 Hi + 角色/团队。
- 面客语种以产品上下文为准；用户点名双语再出对照。

## 产出

目录：`deliverables/lead/06-outreach/`

主文件 `warm-emails.md`：

```markdown
# Warm Email Transforms: {品类} × {目标市场}

- source: 台账 product_context（不粘贴原文）
- accessed:
- upstream: deliverables/lead/06-outreach/cold-emails.md | 本轮粘贴
- send: 未发送

## 摘要

## Transform {N}: {ICP 名}

**Original:** （节选或指向上游编号，不把教学例子当原文）
**Buyer Persona:** 职位 + 行业 + 区域
**Context Clue:**
**Clue source:** URL | 产品上下文 | 本轮消息 | suggested context — verify before sending

### Warm Email Rewrite

（可直接复制的正文）

### Why These Changes Work

- （删除了什么、为什么）
- （加入了什么、预期作用：作业信号 / 降低决策成本 / 可选价值 / 运营具体性）
- （仍需按收件人定制的部分）

### Forbidden-phrase replacements

| original_span | match_type | replacement |
| --- | --- | --- |

### Per-recipient customization

### A/B note

## 来源

| 声明 | URL 或字段 | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 输入几封就几则 transform
- 每则含五段结构与 A/B/C（或等价三选一）CTA
- `references/forbidden-phrases.md` 的禁用语在改写稿中为零
- 每封 <200 词
- 含数字的声明有来源、`[待补充]` 或「未在上下文出现」
- 未发送
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

竞品调研与 New 均无冷邮件成稿语料，改写教学借买家损失语言与采购摩擦形状，不借成稿原文。输入写「I'm reaching out. We are a leading manufacturer with competitive prices and fast delivery. Can you share your requirements?」。成稿应把自我推销换成一条可核验的作业损失观察（净价登录后才见 → 没法给自家客户报价；下单后价可变 → 已出的下游报价作废；交期不绑定 → 班组、脚手架、工期槽空转；库存只显示色点不是日期 → 不敢对客户承诺到货日；RMA 甩厂家 → 安装商自己当投诉窗口），钩子只写角色相关观察，自称只出现在轻量提议段并接可核验运营事实，结尾 A/B/C 轻 CTA（例如按日期而非色点询可用性、RMA 路径说明、备线试单材料），而不是公司简介、催要需求清单、或未核验的「缩短 21%」。第一单按「备线不是换商」写，不写成换掉现有批发商。目录批发交货后沉默 vs 工程伙伴跟到调试，可作洞察形状。禁止把库存或时效承诺当卖点，禁止自称制造商或备件库。没有交期数字就写「未在上下文出现」。不要把本节句子粘进交付物。

## 易错

- 没读原文、没读产品上下文就改写。
- 上游冷邮件文件缺失时既不读本轮粘贴、也不停。
- 为凑钩子编造公司新闻、统计或交期百分比。
- 把教学例子或「cut lead time by 21%」支架当事实。
- 只做词面替换，叙事仍是自我介绍。
- 禁用语语义变体漏扫（I wanted to touch base、我们是领先制造商）。
- CTA 要对方先开会或先交需求清单，自己不提供可带走的选项。
- 终稿残留正式敬语、催更或 Best Price。
- 把本文件当成冷邮件生成器或跟进序列。
- 自行决定暖化稿 vs 冷稿谁当序列首封；优先级以 `lead-email-sequence-strategy` 为准。
- 未配置外发仍去发信。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 每封有原文 + 品类 + 买家角色 + 情境线索来源
- [ ] 已按 `references/forbidden-phrases.md` 扫描；改写稿零命中
- [ ] 公司事件与数字已查证或已标缺口；未编造
- [ ] 每封五段结构、低摩擦 CTA、<200 词
- [ ] Why These Changes Work 至少三条，机制不发明名词
- [ ] 文件在 `deliverables/lead/06-outreach/warm-emails.md`；未发送
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
