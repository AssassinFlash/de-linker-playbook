---
name: marketing-positioning
description: >
  Use when the user needs product positioning, ICP, ideal customer
  profile, buyer personas, value proposition, market fit, competitive
  positioning, messaging strategy, target audience, 产品定位, or
  价值主张, including phase 1 foundation work. Read the ledger
  product_context (default ~/Documents/New/CONTEXT.md); collect at
  least fifteen sourced public data points; write the positioning
  statement, segments, differentiators, and messaging pillars to
  deliverables/marketing/01-foundation/. Invent no numbers; never
  paste skill examples into the output. Not for copy polish,
  competitor battle cards, product-archive indexing, or phase
  navigation.
---

# 产品定位

根据已读产品上下文与可验证公开来源，写清服务谁、凭什么信、下游该重复哪些话，落到 `deliverables/marketing/01-foundation/`。不在本仓库另写产品档案。

## 步骤

1. **规则与输入**。读 `skills/marketing-playbook-standards/SKILL.md`。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`）。把 `~` 展开为用户主目录，不要把 `~` 当相对路径。本会话还没读过就现在读。完成：能指出受众、品类、已有差异化各依据哪几条；原文不拷进本仓库。文件不存在则停并写缺口，不编造公司、市场、价格、流量或竞品。
2. **收集**。用网页搜索查证公司站点、目标渠道（以产品上下文为准）店面、职业主页、视频与第三方提及；需要原文则抓取指定 URL。先凑满 15 个带来源的公开数据点，再向用户补缺口；已经能公开核实的不要再问。多源并行时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口，不编造。需要字段级查询或 15 项 tally 时，读 `references/methodology.md`。完成：tally ≥15，每条有 URL 或摘录；不足则再搜一轮。
3. **分析**。只从已收集证据推导：市场层级、价值链排序、价值主张（Generic / Differentiating）、SWOT、ICP 与买家角色、信息支柱。需要量表或表结构时读 `references/methodology.md`。完成：层级有引用数据点；中游客群按「收入潜力 × 现有能力 × 评价证据」排序；每条 Differentiating 有对应证据。对手只写具名与对我们的含义，不写战卡。
4. **落盘**。写入下方两个主文件；用户点名信息矩阵或对比图时再写可选文件。完成：主文件非空；表每行有 `source`；产品线 / 买家角色 / 竞争格局各 ≥3 行；无占位公司名；教学支架原文零出现。禁止写入产品档案正文或证据库副本。
5. **确认**。把定位句、主客群、差异化、信息支柱交给用户过一眼。完成：用户确认、列出要改的条，或交付物标明「待确认、不得当已批准」。

## 默认

- 产品事实只读 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存。
- 默认渠道写「目标渠道（以产品上下文为准）」，不预设某个平台。
- 内部策略用语跟用户本轮语言；面客短句用产品上下文的面客语种；同一段不混用。
- 窄改文案走 `skills/marketing-copywriting/SKILL.md`（存在时也可走 `skills/marketing-copy-editing/SKILL.md`）。对手战卡走 `skills/marketing-competitor-intelligence/SKILL.md`（文件存在时）。
- 十五节档案覆盖由 `skills/marketing-product-profile/SKILL.md` 索引，本 skill 不重复落档。

## 写法

- 先搜后问；缺口一次只确认一节。
- 空泛的 quality / price 标 Generic，改写成可验证能力再进差异化。
- 规格必须数字化：MOQ、交期天数、尺寸或认证里至少两项有数；没有就写「未在上下文出现」或「公开源未找到」。
- 买家角色必须有 role、行业、决策标准、痛点、对该角色的承诺。
- B2B 直说 MOQ、交期、贸易条款，不用注册或免费试用口吻。

## 产出

主文件：

- `deliverables/marketing/01-foundation/product-positioning.md`
- `deliverables/marketing/01-foundation/positioning-data.xlsx`（表头可用 `templates/positioning-data.xlsx`；不能写表时改同目录 `positioning-data.json`）

可选（用户需要时，同目录）：`messaging-matrix.md`、`competitive-positioning-map.md`、`brand-voice-guide.md`。

```markdown
# 产品定位

- source: 台账 product_context（不粘贴原文）
- collected: N/15
- confirmed: 是 / 待确认

## 定位句

## 目标客群

## 价值主张

## 关键差异化

## 信息支柱

## 证据点

## 来源

## 缺口

## 可验证断言
```

表三页（或 JSON 三数组），每行 `source` 非空：Product Lines、Buyer Personas、Competitive Landscape。列名见 `references/methodology.md`。

## 例子

> 仅供理解，禁止引用到输出。

公开页只写 high quality, competitive price。差异化栏写成「未形成可验证差异化，Generic」，不要把这句话写进定位句。有自有产线与指定项目经理的来源时，再写成买家能感到的结果，并附 URL。

## 易错

- 没读产品上下文就写定位句。
- 把教学例子或模型记忆当事实。
- 用 Competitor A/B/C 占位。
- 把内销价直接当出口价。
- 跳过价值链排序。
- 把十五节档案或证据库写入本仓库。
- 把草稿当已批准。
- 用 SaaS 口吻写 B2B 贸易定位。

## 清单

- [ ] 读过共用规则与 `product_context`，原文未拷进本仓库
- [ ] 公开数据点 ≥15，每条有来源；缺搜索已停并写缺口
- [ ] 定位句、客群、差异化、信息支柱、证据点均有；Generic / Differentiating 已标记
- [ ] 表三页各 ≥3 行，`source` 全非空，对手实名
- [ ] 文件在 `deliverables/marketing/01-foundation/`
- [ ] 无产品档案正文；例子原文未进入交付物
- [ ] 用户已确认或交付物标明待确认
