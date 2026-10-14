---
name: marketing-pricing-strategy
description: >
  Use when the user says pricing strategy, quotation, cost structure,
  margin, MOQ pricing, FOB/CIF price, competitor pricing, export
  pricing, price tiers, 定价策略, 报价, 成本结构, 毛利, 出口定价, or
  定价层级; when B2B manufacturing or foreign-trade work needs a sourced
  price ladder, landed cost, distributor MAP, MOQ grid, or quote
  calculator, including foundation-phase pricing in this repo. Read
  the ledger product_context; collect verified public listing and
  competitor prices; write the strategy document and
  pricing-benchmark workbook under deliverables/marketing/01-foundation/.
  Invent no numbers. Not for conversion copy, SEO audits, campaign
  plans, or phase navigation.
---

# 定价策略

根据已读产品上下文与可核验的公开报价，写出分层定价策略与基准表，落到 `deliverables/marketing/01-foundation/`。数字必须带来源；缺则写缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。若已有则只读 `deliverables/marketing/01-foundation/` 下的竞品档案与定位文档。完成：能指出品类、计价单位、目标市场、现行作价方式、产地（影响运费）各依据哪几条；原文不拷进本仓库。缺的标「未在上下文出现」。
3. **收集**。用网页搜索查证公开报价、行业报告、运价指数、对应品类的原料现货；需要原文则抓取指定 URL。报价页以产品上下文的目标渠道为准。需要隔离深挖某一竞品或某一品类报价时 dispatch a subagent, else do it inline。用户已配置网页采集服务时，才用它抓取公开页。搜索不可用则停止并写缺口。完成：满足下方数据门，或已把缺口与已收集点一并记下；每条有 `source` 与访问日期。
4. **分析**。只用已收集数据套「默认」框架。无来源的数字打缺口旗，不填。完成：成本栈、市场带、价值区间、客户类型层级、MOQ、区域落地成本、经销结构均有结论或缺口说明。
5. **落盘**。按「产出」写文件。生成表格时运行 shell 命令，或填 `templates/pricing-benchmark.xlsx`（若在）。需要隔离时 dispatch a subagent, else do it inline。完成：主文档与基准表非空；占位价未留在推荐位；教学支架原文零出现。

## 默认

**数据门**（进分析前核对）

- ≥30 条价格点，覆盖产品 × 材质或规格 × 表面或配置
- ≥5 条运费锚点，覆盖 ≥3 个目标市场区域
- ≥3 条行业价格趋势来源
- ≥10 条目标渠道公开标价（含 URL）
- 当期原料现货价，带日期与来源

达不到则停：把已收集点与缺口写入交付物，不编造凑数。

**成本加成**。按产品上下文的标准单位拆：原料、加工、表面处理、包装、工厂负担；加目标毛利率得建议价。原料必须对应当日现货来源。

**市场对照**。每类产品 ≥10 条可比公开标价，划低 / 中 / 高。标准线对中位，精品线对高位，定制或项目线高于高位。写下可辩护点（交期、设计、质量、认证），须有来源。

**价值定价**。地板 = 目标市场次优替代品价格；天花板 = 买家可感知节省或功能溢价；报价落在两者之间。溢价锚到买家项目价值，不只锚自己的料费。

**客户类型层级**（用收集数据校验，勿把起点区间当事实）

| 层级 | 供给 | 典型买家 | 毛利起点（待校验） |
| --- | --- | --- | --- |
| 标准线 | 目录规格、常见表面 | 承包商、经销商、渠道买家 | 15–25% |
| 精品线 | 更宽表面、有限定制 | 设计师、酒店或商业开发 | 30–45% |
| 定制 / 项目线 | 全定制、项目报价 | 建筑师、大型商业开发 | 40–60% |

**MOQ**。按 ICP 客户类型 × 三条产品线填最低起订；项目类可为 1 个项目。覆盖上下文中出现的类型，目标 ≥5 类；不足则写缺口。可配套可退样品以筛选认真买家。

**区域调整**。用运费数据算落地成本：市场、定位、运费、关税、毛利加减。≥3 个目标市场。有认证门槛或贸易救济风险的市场，先核净利再报价。

**报价心理**。先出示精品线再出示标准线；项目打包可微折；B2B 用整齐、可比较的整数；数量阶梯写清楚；FOB 与 CIF 都给（CIF 方便买家比价，FOB 降低己方风险）。

**经销**。出厂价 → 经销商（成本 + 毛利）；经销价 → 当地（出厂约 +10–15%，用数据校验）；终端价看当地能承受的水平。保护：最低广告价、销量返点、排他与销量承诺绑定。

**提价信号**。市场：原料上涨、对手已提、报价几乎不砍。业务：转化偏高、积压增加、上次提价后复购仍稳。做法：只对新单、按指数传导原料、加选项、开精品线同时保留标准线。

## 写法

- 每条建议：具体数字或区间 + 收集阶段来源 + P0 / P1 / P2。
- 禁止「有竞争力的价格」这类空话。
- 禁止只做成本加成；禁止无成本理解地抄对手价。
- 策略主文档用简体中文；面客字段（FOB、CIF、MOQ、Unit Price）用英文。用户本轮指定语种时从其语种。
- 单位、币种、条款与产品上下文一致；混用时在表头写明。

## 产出

路径均在 `deliverables/marketing/01-foundation/`。

**策略主文档** `pricing-strategy.md`

```markdown
# 定价策略

- source: 台账 product_context（不粘贴原文）
- collected: N 条价格点 / 缺口
- accessed: YYYY-MM-DD

## 执行摘要

（3 条，含具体单价）

## 市场数据汇总

## 成本结构分析

## 定价层级建议

## MOQ 策略

## 市场差异化定价

## 经销商定价结构

## 提价时机判断

## 执行清单
```

**基准表** `pricing-benchmark.xlsx`

工作表：`Pricing Benchmarks`、`Cost Stack`、`Market Pricing`。`Pricing Benchmarks` ≥10 行，每行 `source` 为已抓或已标明未验证原因的 URL。零值不得当推荐价留下。若仓库有 `templates/pricing-benchmark.xlsx`，按其列填。

生成用 JSON 形状：

```json
{
  "data_points": [
    {
      "product_type": "",
      "material": "",
      "spec": "",
      "finish": "",
      "unit": "",
      "our_price": null,
      "competitor_low": null,
      "competitor_high": null,
      "marketplace_price": null,
      "margin_pct": null,
      "moq": null,
      "lead_time_days": null,
      "source": ""
    }
  ],
  "costs": [
    {
      "component": "",
      "variant_a": null,
      "variant_b": null,
      "pct_of_total": "",
      "notes": "",
      "source": ""
    }
  ],
  "market_pricing": [
    {
      "market": "",
      "product_type": "",
      "our_price": null,
      "competitor_avg": null,
      "margin_pct": null,
      "notes": "",
      "source": ""
    }
  ]
}
```

**执行附件**（同目录）

- `price-tiers.md` — 产品线 × 规格 × 表面 × FOB 区间 × MOQ × 数量折扣
- `quote-calculator.md` — 输入规格 / 数量 / 表面 → 推荐报价及毛利注释
- `competitor-price-benchmarks.md` — 对手价位点与差异化理由（带来源）
- `discount-policy.md` — 数量折扣、首单、样品、运费
- `negotiation-playbook.md` — 异议类型、应答要点、底线（不编造未出现的买家原话）

## 例子

> 仅供理解，禁止引用到输出。

输入是三条已抓公开报价（低 / 中 / 高）且单位一致。层级写成「标准线落在中位附近并引这三条来源」，不写「具有竞争力的价格」。

输入渠道页是「目录公开、净价登录后可见」或「目录与价都在门户内、页上只留询价」。基准表按通道分列：客态无净价不填目录价；批后净价与询价制分栏，各带 URL。不要把缺价页编成公开标价，也不把门户制写成唯一正确形态。

输入已确认安装商与经销商走不同批后价格组、个案净价叠在组上。`price-tiers.md` 写组键与待校验毛利起点，不把标准 / 精品 / 定制当店面公开档名，也不公布组间差额。市场只声明「有数量阶梯、不标数字」时标缺口，不填百分比。

输入买家是一口价转包（对业主锁总价）。有效期写成买方把上游价锁进自己标书的窗口，过期须重核，不是客套；目录净价可变动，能进标书的是带窗口的报价，不要写成同一条价格保证，也不要写「长期有效」或编具体天数。预算询价与可下单报价分开：前者非约束、只给模型；后者才进推荐位。

输入 RFQ 价表含行项目、币种、单位、贸易术语、有效期。执行附件把这些列为必填，不只给一个 FOB 整数。目标市场标书用到的术语按收集证据写，不默认 FOB/CIF。商务闸过了、技术闸因文件包卡住时标缺口，不以「有竞争力」收束。

输入支付是预付默认、账期须批后授信。`discount-policy.md` 按轨分写，不把消费级卡支付当批发默认，不编授信额或折扣点。欧盟市场不把最低广告价写成「我们定市场价」；可写已批伙伴可见净价加己方报价窗口，转售限制交法务。

不要把本节句子拷进交付物。

## 易错

- 编造报价或现货价来凑满 30 条。
- 只用成本加成，或无来源地抄对手价。
- 忽略不同目标市场的运费、关税与认证成本。
- 推荐价位留下空单元格、`null` 或未替换占位。
- 未读产品上下文就定计价单位或客户类型。
- 把本节或例子原文写进交付物。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 价格点各有来源；达不到数据门时已写缺口并停止凑数
- [ ] 成本栈使用带日期的原料现货来源
- [ ] 标准 / 精品 / 定制（或项目）三层均有具体单价区间或已标缺口
- [ ] MOQ 覆盖上下文中的客户类型（目标 ≥5 类）
- [ ] ≥3 个目标市场列出运费、关税、毛利加减
- [ ] `pricing-strategy.md` 含执行摘要、定价层级建议、MOQ 策略、提价时机判断
- [ ] `pricing-benchmark.xlsx` 在 `deliverables/marketing/01-foundation/`，Benchmarks ≥10 行且 `source` 非空
- [ ] 五份执行附件均在同目录并指向其数据来源
- [ ] 主文档为简体中文（或用户指定语种）；面客字段用英文
- [ ] 教学支架原文未进入交付物
