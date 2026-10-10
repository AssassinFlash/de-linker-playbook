---
name: lead-linkedin-mythbust
description: >
  Use when the user asks to debunk a myth, bust a misconception, write a
  comparison post, challenge a common belief, or mentions myth-busting,
  industry myths, common misconceptions, comparison post, debunk, 揭秘内幕,
  误区纠正, 行业迷思, 辟谣, 对比帖, myth vs reality, true cost, hidden cost,
  X vs Y, or which lasts longer, including phase 8 LinkedIn of this repo's
  lead run. Verify the misconception exists, then write a Structure 7 post
  (Hook, Myth or Comparison, Reality, Buyer Benefit, CTA) under
  deliverables/lead/08-linkedin/. Distinct from lead-linkedin-buyer-concern
  (real worries) and lead-linkedin-faq (factual questions). Invent no
  evidence. Not for authority posts, education explainers, or phase
  navigation.
---

# LinkedIn 辟谣与对比帖（Structure 7）

验证买家真实持有的误区、或 sourcing 里真实存在的对比，按 Structure 7 写成可复制的 LinkedIn 英文帖，落到 `deliverables/lead/08-linkedin/`。缺证据标缺口，不编造。本 skill 只产帖稿，不发布。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。硬依赖：已批准的 `deliverables/lead/01-icp/icp-analysis.md`。软依赖存在则读：`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/05-usp/product-knowledge.md`、`deliverables/lead/08-linkedin/topic-research.md`。用户本轮给出的品类/利基、目标买家（行业与区域）、误区或对比主题、证据、CTA 一并记，来源记「用户本轮」。品类或目标买家仍不清：打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则停并只要这两项，不在本文件另写问卷。硬依赖文件缺失、用户本轮也未给出对应买家全文、且无 `user_waiver` → 停。原文不拷进本仓库。完成：能指出品类、买家、已有误区线索各依据哪几条。

3. **查证**。用网页搜索查证该品类买家确实持有该误区，或该对比在公开 sourcing 讨论中真实出现；再为 Reality 搜至少一条可引用证据（标准、规格、公开报告、已抓取页）。需要原文则抓取指定 URL 的正文。查询模板见 `references/structure-7.md`。搜索日志格式见 `skills/lead-generation/references/search-protocol.md`。搜不到「市场上有人这么认为或这么比」→ 该候选作废，不揭穿。搜索不可用 → 停止并写缺口，不编造误区或证据。禁止为凑次数空搜。多候选需隔离时 dispatch a subagent, else do it inline。完成：进入候选的每条有摘录证明市场存在；将写入 Reality 的每条事实有 URL 或产品上下文出处。

4. **选定**。用户已点名主题 → 用该条（仍须步骤 3 验证通过）。用户未点名：在交付物写 1–2 个已验证候选（陈述、Reality 要点、证据类型、Buyer Benefit 一句）。本轮能问则只问选哪条；用户说直接做或不能问 → 取证据最硬的一条，标「未经用户确认」。`mode` 只取 `myth`（揭穿错误信念）或 `comparison`（两个真实选项的利弊）。禁止无人持有的误区、禁止一方明显荒谬的稻草人对比、禁止把卖点伪装成误区。骨架与分帧见 `references/structure-7.md`。完成：mode、选定句、Reality 要点、至少一条证据、Buyer Benefit 一句都有。

5. **成稿**。按 Structure 7 写英文帖：Hook → Myth / Comparison → Reality / Expert Analysis（含证据）→ Buyer Benefit → CTA。篇幅、钩子、CTA、标签、软广、四种风格只读 `skills/lead-generation/references/linkedin-post-guidelines.md`，不在本文件复述。用户点名一种风格则成稿后只改语气与结构，不改事实。CTA：用户指定且符合该规范则用；否则用一条可回答的经验问题，不承诺未有材料。产品句最多 1–2 句，删掉后帖子仍独立有用。数字、证书、案例、成本：产品上下文或已抓取页里有才写。完成：五段齐全；过共用规范清单；含数字的句子能指回来源。

6. **落盘**。写入 `deliverables/lead/08-linkedin/mythbust-post.md`。`publish_status: copy_only`。用户自行发布，或经用户已配置的工具发布；本 skill 不发帖。付费发布须先告知并获准。完成：主文件非空；含候选、选定、可复制帖、中文策略、搜索日志、来源表、缺口；教学例子原文零出现。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批、不代替发布。

## 默认

- 产品事实只读台账 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 硬依赖是 ICP；USP、产品知识、话题研究有则读，不阻塞。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止并写缺口，不编造。
- 单帖 inline 做完；多候选隔离时 dispatch a subagent, else do it inline。
- 帖子正文缺省英语；策略与缺口跟本轮语言（缺省中文）；标签英语。用户本轮指定其他面客语种则改帖，同一段不混用。
- 真实买家顾虑走 `skills/lead-linkedin-buyer-concern/SKILL.md`（文件存在时）。事实问答走 `skills/lead-linkedin-faq/SKILL.md`（文件存在时）。权威趋势走 `skills/lead-linkedin-authority/SKILL.md`（文件存在时）。教育讲解走 `skills/lead-linkedin-education/SKILL.md`（文件存在时）。选题卡走 `skills/lead-linkedin-topic-research/SKILL.md`（文件存在时）。多平台日历或战役走 `skills/marketing-social-content/SKILL.md`（文件存在时）。本文件不写那几类。
- 产出只进 `deliverables/lead/08-linkedin/`。本 skill 只产帖稿。

## 写法

- `myth`：先点出错误信念，再用证据拆穿。能量是纠正，不是嘲讽持有该信念的买家。
- `comparison`：两个都写真实利弊，接到该 ICP 的决策条件（交期、规格、总成本、风险），不写成「正确选项 vs 笑话选项」。
- Hook 只做一件事：把误区说得刺耳，或把对比说成一个正在做的决定。
- Reality 至少绑一条证据。没有证据的 Reality 不算完成，标缺口，不把观点写成事实。
- Buyer Benefit 必须落到该 ICP 可感到的结果（少一次来料不合格、少付一次不该付的运费、规格一次写对）。只写「现在你知道真相了」不算完成。
- 揭穿的是说法，不是点名的公司。
- 技术细节停在该 ICP 用得上的那一层；采购经理不读工艺论文。
- 软广：产品只作为经验来源出现，不把帖子写成功能清单。

## 产出

目录：`deliverables/lead/08-linkedin/`

主文件 `mythbust-post.md`：

```markdown
# Mythbust Post

- source: 台账 product_context（不粘贴原文）
- accessed:
- mode: myth | comparison
- icp:
- confirm_status: 用户指定 | 本轮确认 | 未经用户确认
- publish_status: copy_only
- publish_tool: not_configured | configured

## 搜索日志

| # | Capability | Query/URL | Results | Useful | Notes |
|---|------------|-----------|---------|--------|-------|

## 候选

| id | mode | statement | reality_point | evidence_type | buyer_benefit | verified |
| --- | --- | --- | --- | --- | --- | --- |

## 选定

- statement:
- reality:
- evidence:
- buyer_benefit:

## 帖子（可复制）

[Hook]

[Myth / Comparison]

[Reality / Expert Analysis]

[Buyer Benefit]

[CTA]

[3-5 hashtags]

## 策略说明

## 来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- `mode` 为 `myth` 或 `comparison`
- 选定句已验证为市场真实存在的误区或对比
- Reality 至少一条证据有 URL 或产品上下文出处
- 帖子五段按 Structure 7 齐全，并可单独复制
- 过 `skills/lead-generation/references/linkedin-post-guidelines.md` 清单
- `publish_status` 为 `copy_only`，除非用户本轮要求发布且已配置工具
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

形状与正反对照见 `references/examples.md`。不要把该文件或本节句子写入交付物。误区必须能在搜索摘录里看到有人持有；对比必须两边都有真实代价。

输入写「买家把规划工具当成一类软件」。成稿应先写出该信念在询盘里怎么出现（把仿真、排布、技术经济、下单四格混成一格），再用可核验出处拆穿，落到一次分清这一单要哪一格的交付物；不要写成「我们的工具更专业」。形状借自规划工具四格（交易格 vs 仿真格互不替代）和术语图的 NEVER-SAY（自造品类名、借工厂形容词、假朋友词、尺度膨胀），不写产品广告。

## 易错

- 没搜到市场上有人持有，仍写揭穿帖。
- 编造标准、证书、客户案例、成本数字或「行业都知道」。
- 一边明显荒谬的稻草人对比。
- 点名攻击竞品，而不是拆穿说法。
- 把本厂卖点改写成「误区」。
- 真实顾虑写成误区（那是 buyer-concern）；事实问答写成揭穿（那是 FAQ）。
- Buyer Benefit 只停在「你知道了」。
- 技术细节超过该 ICP 的决策层。
- 把帖子发出去，或承诺未有的资料。
- 把教学例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] ICP 已读，或用户本轮已给买家，或已记录 `user_waiver`
- [ ] 每个候选有搜索摘录证明市场存在；Reality 每条事实有来源
- [ ] `mode` 已定；不是稻草人、不是伪装卖点
- [ ] 帖子按 Structure 7 五段齐全，过 LinkedIn 共用规范清单
- [ ] 文件在 `deliverables/lead/08-linkedin/mythbust-post.md`；只产稿不发布
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
