---
name: marketing-positioning
description: >
  Use when the user needs product positioning, ICP (company types),
  buyer personas (job roles), value proposition, market fit, competitive
  positioning, messaging strategy, target audience, 产品定位, or
  价值主张, including phase 1 foundation work. Read the fact-source entry docs/fact-sources.md; collect at
  least fifteen sourced public data points; write the positioning
  statement, segments, differentiators, and messaging pillars to
  deliverables/marketing/01-foundation/. Invent no numbers; never
  paste skill examples into the output. Not for copy polish,
  competitor battle cards, outreach strategy, 外展策略,
  product-archive indexing, or phase navigation.
---

# 产品定位

根据已读产品上下文与可验证公开来源，写清服务谁、凭什么信、下游该重复哪些话，落到 `deliverables/marketing/01-foundation/`。不在本仓库另写产品档案。

## 步骤

1. **规则与输入**。读 `skills/marketing-playbook-standards/SKILL.md`。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。本会话还没读过就现在读。已存在 `deliverables/lead/01-icp/` 客群分析可作客群输入。完成：能指出受众、品类、已有差异化各依据哪几条；原文不拷进本仓库。文件不存在则停并写缺口，不编造公司、市场、价格、流量或竞品。
2. **收集**。用网页搜索查证公司站点、目标渠道（以产品上下文为准）店面、职业主页、视频与第三方提及；需要原文则抓取指定 URL。先凑满 15 个带来源的公开数据点，再向用户补缺口；已经能公开核实的不要再问。多源并行时 dispatch a subagent, else do it inline。搜索不可用则停止并写缺口，不编造。需要字段级查询或 15 项 tally 时，读 `references/methodology.md`。完成：tally ≥15，每条有 URL 或摘录；不足则再搜一轮。
3. **分析**。只从已收集证据推导：市场层级、价值链排序、价值主张（Generic / Differentiating）、SWOT、ICP（公司类型）与买家角色（职务）、信息支柱。需要量表或表结构时读 `references/methodology.md`。完成：层级有引用数据点；中游客群按「收入潜力 × 现有能力 × 评价证据」排序；每条 Differentiating 有对应证据。对手只写具名与对我们的含义，不写战卡。Competitive Landscape 只写格局一页表；战卡走 `marketing-competitor-intelligence`。
4. **落盘**。写入下方两个主文件；用户点名信息矩阵或对比图时再写可选文件。完成：主文件非空；表每行有 `source`；产品线 / 买家角色 / 竞争格局各 ≥3 行；无占位公司名；教学支架原文零出现。禁止写入产品档案正文或证据库副本。
5. **证据闸**。按 `docs/feedback-rules.md` 第 9 节逐条自查定位句、主客群、差异化、信息支柱：每条能指到 tally 里的来源；查不到的标〔未证实〕，不写成事实。完成：全过则 frontmatter 写 `status: approved` 与 `evidence_gate: <日期>`；没过的条目修一轮，仍不过就留 `status: draft` 并在文内列出卡在哪条。证据闸不请操作者核对事实。
6. **审稿**。定位句和信息支柱会被原样用到网页、邮件和帖子里，算对外文字：按 `docs/feedback-rules.md` 第 10 节拿给操作者看，按意见改、每轮记「## 审稿记录」并重过证据闸，操作者说「可以了」写 `operator_ok: <日期>`。完成：有 `operator_ok`，或台账写明在等操作者看。

## 默认

- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存。
- 默认渠道写「目标渠道（以产品上下文为准）」，不预设某个平台。
- 内部策略用语跟用户本轮语言；面客短句用产品上下文的面客语种；同一段不混用。
- 窄改文案走 `skills/marketing-copywriting/SKILL.md`（存在时也可走 `skills/marketing-copy-editing/SKILL.md`）。对手战卡走 `marketing-competitor-intelligence`（文件存在时）；本 skill 的 Competitive Landscape 只写格局一页表（具名、类型、对我方含义），不写战卡。
- 外发 USP 与证据包走 `lead-usp-extraction`；分行业获客 ICP 策略走 `lead-icp-analysis`。已存在 `deliverables/lead/01-icp/` 客群分析可作输入。
- 十五节档案覆盖由 `skills/marketing-profile/SKILL.md` 索引，本 skill 不重复落档。

## 写法

- 先搜后问；缺口一次只确认一节。
- 空泛的 quality / price 标 Generic，改写成可验证能力再进差异化。
- 规格必须数字化：MOQ、交期天数、尺寸或认证里至少两项有数；没有就写「未在上下文出现」或「公开源未找到」。
- ICP 写公司类型，买家角色写职务角色，二者分列；买家角色必须有 role、行业、决策标准、痛点、对该角色的承诺。
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
- evidence_gate: <日期> / 未过（卡在哪条）

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

表三页（或 JSON 三数组），每行 `source` 非空：Product Lines、Buyer Personas、Competitive Landscape。Competitive Landscape 是格局一页表，不是战卡。列名见 `references/methodology.md`。

## 例子

> 仅供理解，禁止引用到输出。

输入写 high quality, competitive price 或「一站式批发」。差异化栏写成「未形成可验证差异化，Generic」，不要把这句话写进定位句。

输入写「我们是光伏批发商，服务也好」。成稿应按 Kotler 式占位：For [安装商/EPC] who [承担兼容、交付与质保风险]，[公司] is [光储方案伙伴] that [工程 BOM、按厂家矩阵核验逆变器-电池配对、调试支持与厂家质保协调]。Unlike 卖箱子、交货后沉默的目录批发。不要写成 one-stop shop / skip the middleman / we are your bridge，也不要去占公开批发门户已占的 Großhändler/Hersteller 槽。

输入写「自有产线 / 自有质保 / 我们安装 / 我们发证 / 自有监控平台」。成稿应改成身份边界：工程伙伴 + 批发引擎；质保是厂家的、这边协调；调试支持、不派施工队；证书由公告机构签发。不要写成制造商、备件库或承保方。

输入写「所有人都是客户，含分销商和业主」。成稿应按购买行为切：安装商（项目触发，首单是备份线不是换商）与 EPC（规格/招标）。分销商不是客群（自身已是分销层）；终端业主不是客群。不要按年龄或人数切主客群。

输入把占位立在「实时库存 / 24 小时仓」。库存与发货可以当供给事实，占位句不要靠库存轴；没有按件可用性来源就写「未在上下文出现」。不要把库存数量或时效承诺当卖点。

有配对核验、工程 BOM、质保协调的公开来源时，再写成买家能感到的结果，并附 URL。竞品只写结构特征（登录锁价的目录批发 vs 工程伙伴），不抄对方原句。过时站点稿只作「当前公开页 | 拟替换占位」对照，不把证言人名当买家角色。

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
- [ ] 已过证据闸（`status: approved` + `evidence_gate`），或标明卡在哪条
