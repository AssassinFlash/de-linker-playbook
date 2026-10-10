---
name: lead-cold-email-gen
description: >
  Use when writing cold email, 开发信, 冷邮件, first-touch email,
  or outreach email not tied to one researched company, including
  phase 6 outreach of this repo's lead run. Read approved ICP and
  USP; run Standard (strong CTA, target five drafts) or Low-Pressure
  (weak CTA, one per persona). Each email is under 200 words, one
  ICP, one USP, with A/B subject lines. Write to
  deliverables/lead/06-outreach/. Send only with a user-configured
  outbound tool; otherwise copy only. Invent no pain points, USPs, or
  statistics. Not for marketing-phase prospect lists or lifecycle
  nurture (marketing-email-outreach), follow-up sequences, warm
  rewrites, sequence strategy, or single-company targeted outreach.
---

# 冷邮件生成（双模式）

根据已批准 ICP 与 USP 写首触冷邮件：标准模式强 CTA，低压模式弱 CTA。落到 `deliverables/lead/06-outreach/`。未配置外发工具或用户未要求发出时，只产文案不发送。痛点、卖点、统计缺证据则标缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。硬依赖：已批准的 `deliverables/lead/01-icp/icp-analysis.md` 与 `deliverables/lead/05-usp/usp-strategy.md`。软依赖存在则读：`deliverables/lead/04-market/competitor-positioning.md`、`deliverables/lead/03-contacts/collection-report.md`、`deliverables/lead/05-usp/product-knowledge.md`。用户本轮直接给出的 ICP / USP / 模式视为本轮输入，来源记「用户本轮」。模式、要用的 ICP 集合或主 USP 仍不清时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不在本文件另写问卷。完成：能指出每封将用的 ICP、痛点、USP 各依据哪几条；原文不拷进本仓库。任一硬依赖文件缺失、用户本轮也未给出该份对应全文、且无 `user_waiver` → 停。

3. **选模式并映射**。用户本轮点名则用：Standard / Low-Pressure / Both。未点名默认 Standard。本 skill 写 ICP 段首触稿，不为名单里每家各写一封（单家定向走 `skills/lead-targeted-outreach/SKILL.md`，文件存在时）。每封只配 **一个 ICP × 一个痛点 × 一个 USP × 一个 CTA**。Standard：目标 5 封、5 组不同组合；组合不足 5 时按实有组合写，用结构或开场变化拉开差异，不编造额外 ICP 或 USP，少的在缺口写明。Low-Pressure：每个画像 1 封，上限 5。Both：同一文件写两节。联系人表只用来标注可替换钩子，不在本步做逐人成稿。完成：映射表列出拟写的每一封：模式、ICP、痛点、USP、结构式、CTA 类型。

4. **查证（按需）**。开场或正文要用统计、趋势、合规时点时，用网页搜索查证该条，记下 URL 与访问日期；需要原文则抓取指定 URL。搜不到或搜索不可用 → 不用数字开场，改用已批准痛点的具体画面，不编造百分比。禁止为凑次数空搜。禁止把搜到的模板原文写入交付物。多 ICP 需隔离时 dispatch a subagent, else do it inline。完成：凡含数字的句子能指回来源；无数字开场则搜索日志写「本轮未检索；开场未使用统计」。

5. **起草**。按「写法」写完整可复制的信。低压或 Both 时读 `references/weak-cta-module.md`。个性化深度读 `references/personalization-layers.md`。面客语种以产品上下文为准（缺省英语）；同一封不中英混排。落款只用上下文已有的人名或公司名，没有则 `[待补充]`。微要约或好奇心 CTA 所承诺的材料，必须是已有交付物或本轮能立刻写出的短件；不能承诺未做的竞品拆解或未持有的数据。完成：映射表每一封都有主题、A/B 主题、正文；正文（不含主题与元数据）<200 词；低压主题 <50 字符。

6. **质检并落盘**。按清单自检后写入 `deliverables/lead/06-outreach/cold-emails.md`。仅当用户本轮要求发出 **且** 已配置外发工具时才发；否则 `send_status: copy_only`，不发送。付费外发须先告知并获准。完成：主文件非空；每封含 Target Persona、Pain Point Focus、USP Applied、Subject、A/B Variant、正文、Performance Notes；教学例子原文零出现。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批、不代替发送。

## 默认

- 产品事实只读台账 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止数字开场并写缺口，不编造。
- 外发工具仅当用户已配置；未配置或未要求发出 → 只产文案不发送。
- 进度只认台账。产出只进 `deliverables/lead/06-outreach/`。
- 分析与缺口用本轮语言（缺省中文）；信体、主题、CTA 用买家语言（缺省英语）。
- 发送须遵守 GDPR、CAN-SPAM 及收件人所在地同类规则。本文件不是法律意见。
- 营销获客阶段的名单研究、角色模板库与生命周期培育走 `marketing-email-outreach`，本文件只写 ICP 段首触成稿。
- 下游（文件存在时再打开，不在本步执行）：`skills/lead-warm-email-transform/SKILL.md`、`skills/lead-followup-sequence/SKILL.md`、`skills/lead-email-sequence-strategy/SKILL.md`。引流素材可嵌入 CTA 时读 `skills/lead-magnet-gen/SKILL.md`。编排闸门见 `skills/lead-generation/SKILL.md`。

## 写法

- 一封一事：不在同一封堆多个痛点或多个 USP。
- 个性化不是插入名字。表层（角色、公司、行业、已核验公开事件）是底线；深层（工作流、KPI 张力、决策卡点、时点风险）必须能回溯 ICP、公司调研或已抓取页。深度下限见 `references/personalization-layers.md`。没有证据的「看到贵司在增长」不写。本文件两层是单封成稿深度（表层身份 vs 深层运转），适用于 lead 首触；`marketing-email-outreach` 的三层（公司 / 角色 / 市场）是模板库覆盖维度，不在本 skill 套用。
- CTA 必须像正文的自然下一步，不另起一套话。
- **Standard（强 CTA）**：共情、短句、收缩词、口语；禁用套话开场。开场优先用已批准痛点画面或已核验公开变化，统计只在有来源时用。结构每封不同。强 CTA 明确请求一个可执行下一步（约短通话、要规格、要样品条件、看对照表），并接到本封痛点。禁用空泛的「感兴趣吗 / 方便聊聊吗」。
- **Low-Pressure（弱 CTA）**：像同行随手写的短讯，不推销。完整自然信，不切成栏目；2–3 句一段，方便手机扫读。主题直接绑痛点或价值，<50 字符。CTA 只用弱 CTA 四式之一（情境微要约、好奇心、买家阶段多选项、破格），见 `references/weak-cta-module.md`；不同低压信不用同一 CTA 格式。结构在四式中轮换：Pain → Fix → CTA；Trigger → Insight → Micro-offer；Stat → Reframe → Specific help（Stat 必须有来源，否则改用 Pain 式）；Micro-story → Takeaway → CTA（故事须来自产品上下文或已抓取案例，不编客户）。
- 空话（leading manufacturer、world-class、hope this finds you well）无证据则删。自夸公司规模或未持有认证不写。
- 主题 A/B：一条洞察或痛点，一条好奇或具体价值；低压两条都 <50 字符。

## 产出

主文件 `deliverables/lead/06-outreach/cold-emails.md`。

```markdown
# Cold Emails

- source: 台账 product_context（不粘贴原文）
- accessed:
- mode: Standard | Low-Pressure | Both
- send_status: copy_only | sent_via_configured_tool
- outbound_tool: not_configured | configured

## 映射
| email_id | mode | icp | pain_point | usp | structure | cta_type |

## Email [N]: [ICP] x [USP]

**Target Persona:**
**Pain Point Focus:**
**USP Applied:**

**Subject Line:**
**A/B Variant:**

[完整信体，可直接复制]

**Performance Notes**
- open_driver: （主题为何值得打开，不预测打开率）
- reply_trigger: （什么会让人回）
- personalization_hooks: （按收件人替换哪几处；无证据的钩子不写）
- send_window: （有来源的时区或工作日习惯，否则「未在来源出现」）
- word_count:

## 来源
| 声明 | URL 或上游文件 | 访问日期 | 摘录 |

## 搜索日志
| 查询或 URL | 日期 | 结论 |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- Standard：按映射写出目标 5 封或实有组合（不足 5 已在缺口写明）；每封结构不同
- Low-Pressure：每个拟用画像 1 封；CTA 格式不重复
- 每封正文 <200 词；低压主题 <50 字符；每封有 A/B 主题
- 痛点能指回 ICP 文件或用户本轮；USP 能指回 USP 文件或用户本轮
- 含数字的句子有来源或已删除
- `send_status` 与是否真正发出一致；未配置外发工具时必为 `copy_only`
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入写「缩短交期、品质可靠」。安装商标准稿应把开场写成该 ICP 已批准的一条摩擦画面（净价要登录才见、当场没法给自家客户报价；或送货日不绑定、班组已排上），中间只嵌一条有证据的 USP（交货后不沉默，而不是目录批发交完就断），结尾接到正文的明确下一步（要交期对照、要规格）。第一单定位是「备线」不是「换掉现有批发商」；不要套话开场或「我们是领先制造商」。低压稿同样一对一，CTA 改成可立刻交付的微要约，不约会议。

EPC 输入若只写价和交期，成稿仍应让技术闸（文件包、兼容证据）与商务闸成对出现；报价有效期按一口价合同的风险工具写，不要写成礼貌过期日。没有来源的百分比不要写进开场。调研里没有冷邮件成稿，本节只借痛点与采购形状。不要把本节句子粘进交付物。

## 易错

- 没读已批准 ICP / USP 就发明痛点或卖点。
- 把教学例子或搜到的冷邮件模板原文写入交付物。
- 一封里堆多个 USP 或痛点。
- 五封同一段落骨架。
- 标准模式用空泛 CTA；低压模式约会议当唯一 CTA。
- 编造统计、客户故事、竞品基准或「看到贵司在增长」。
- 承诺发一份本轮并不存在、也无法立刻写的材料。
- 正文超过 200 词，或低压主题超过 50 字符。
- 未配置外发工具仍发送，或把本文件的成稿当成已发出。
- 做成营销获客阶段的名单研究或生命周期培育体系（那是 `marketing-email-outreach`）。
- 为名单每家各写一封，做成定向外展。
- 终稿残留未解释的 `{{...}}` 或把 `[待补充]` 假装成已核实签名。

## 清单

- [ ] 已读共用规则与 `product_context`；硬依赖已读或已停并写缺口
- [ ] 模式已定；映射表每封为一 ICP × 一痛点 × 一 USP × 一 CTA
- [ ] 数字开场均有来源；无来源则未使用统计
- [ ] 每封 <200 词、结构不重复、有 A/B 主题；低压主题 <50 字符且弱 CTA 四式不重复
- [ ] 痛点与 USP 可回溯上游；个性化钩子无假事件
- [ ] 文件在 `deliverables/lead/06-outreach/cold-emails.md`；未配置或未要求发出时未发送
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
