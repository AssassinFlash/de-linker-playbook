# 推荐与合作伙伴计划方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、矩阵、起点费率与表结构以本文为准。

## 目录

- [输入](#输入)
- [采集](#采集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

## 输入

先读事实源入口 `docs/fact-sources.md`（台账 `product_context` 即指向它），按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若已存在则读：

- `deliverables/marketing/01-foundation/` 定位、买家角色、定价与毛利
- 用户本轮提供的历史订单/CRM 导出、现行伙伴/代理协议、口头佣金安排

产品事实不写进 skill，不另写公司档案。品类、目标市场、产地只引用产品上下文对应字段，不在本文填值。

最小上下文：

- 品类与目标市场（产品上下文对应字段）
- 毛利结构与折扣权限（无则佣金节写缺口，不编造费率）
- 既有客户、指定人、承包、经销等可触达名单来源
- 现行协议条款与区域（若有）

缺项列缺口后停。

## 采集

默认一条能力：用 Apify 搜索查证。需要原文时抓取指定 URL 的正文。Apify 修复与替代取证后仍不可得则停止并写缺口，不编造、不并列多引擎菜单。

把产品上下文的品类与目标市场代入下列意图，每条记下 URL、摘录、访问日期：

1. B2B 制造供应商推荐计划与佣金率
2. 出口制造的经销/代理佣金结构
3. 指定人/设计师转介绍费（对该品类）
4. 承包商向制造商转介绍的激励
5. B2B 伙伴计划做法（外贸制造商）
6. 出口工厂代理招募与佣金协议
7. B2B 推荐激励设计（当前或下一自然年）
8. B2B 制造推荐计划案例

结果不够时再补：该品类佣金基准、目标市场代理惯例、公开伙伴 FAQ。仍用同一条搜索能力，不换工具品牌。

### 抓取

- 至少 2 个竞品伙伴/代理页
- 搜索中出现的公开佣金表或伙伴 FAQ

多站点抓取需要隔离时 dispatch a subagent, else do it inline。

### 最低数据量

进入分析前至少备齐；达不到的写入缺口，不降低后项装成已完成。

- **5** 套 B2B 推荐/伙伴结构，含佣金率与 `source`
- **3** 条制造或外贸向的推荐案例，含 `source`
- 四类推荐人各有佣金基准：指定人/设计师、承包/施工、经销/代理、既有客户
- **2** 个已分析的竞品伙伴页，含 `source` 与摘录
- **1** 份协议/合同结构，含 `source`

### 校验

- 每条基准必须有 `source`，否则标「行业参考值，需按产品上下文毛利调整」
- 不把 SaaS 推荐链接或自动看板当成默认机制
- 佣金建议必须能对照已读毛利；对不齐则下调或写缺口
- 跟踪须能在现有沟通与表格里完成，不强制新软件

## 分析

### 推荐人类型矩阵

用采集数据校验，勿把起点区间当事实。每行补 `source` 或行业参考值说明。

| 计划类型 | 主角色 | 奖励模型 | 正式程度 |
| --- | --- | --- | --- |
| Specifier / Designer | 建筑师、室内设计师、顾问 | 成交订单额约 3–5% 佣金 | 意向函或非正式 |
| Contractor / Executor | 项目承包、安装方 | 数量折扣或现金奖励 | 非正式或意向函 |
| Distributor / Agent | 区域进口商、代理、贸易公司 | 分层尾随佣金或奖金 | 书面协议 |
| Existing Client | 目标市场既有买家 | 订单折扣、样品额度、礼遇 | 非正式致谢 |

角色以产品上下文为准；上下文没有则选最贴近一档并标明「角色未在上下文出现，暂用」。

### 偶发推荐人 vs 当地代理

| 维度 | Occasional Referrer | Local Agent |
| --- | --- | --- |
| 关系 | 一次性或临时 | 持续、有合同 |
| 协议 | 非正式或意向函 | 已签佣金/代理协议 |
| 佣金 | 按核实介绍或成交单 | 按成交单，常为尾随 |
| 排他 | 无 | 可选，按区域或细分 |
| 支持 | 目录 + 样品政策 | 完整赋能包 + 培训 |

### 佣金结构起点

下列为待校验框架，须按产品上下文毛利改写；写入交付物时每条标 `source` 或行业参考值。

| 订单档 | 佣金率 | 条件 |
| --- | --- | --- |
| 低于 USD 10,000 | 3% | 客户回款后支付 |
| USD 10,000–50,000 | 4% | 客户回款后支付 |
| 高于 USD 50,000 | 5% | 客户回款后支付 |
| 新市场 / 新细分 | 前 3 单 +1% | 此前未覆盖的区域或垂直 |
| 排他溢价 | 可议 +1–2% | 绑定年度最低销量 |

支付规则：

- 在被推荐客户回款后支付，不在发货后支付
- 按整单计提，不按分期
- 同一终端客户复购不计佣，除非代理主动再次促成

### 跟踪与归因

外贸推荐多为线下。用低摩擦方法，具体渠道以产品上下文为准：

1. **询盘来源问句** — 每个新线索问 How did you hear about us? 并记录
2. **介绍留存** — 保存推荐人介绍潜客的邮件或消息记录
3. **推荐日志** — 列：`date`、`referrer_name`、`referrer_type`、`referred_client`、`project_summary`、`order_value`、`commission_rate`、`commission_due`、`paid_date`、`source`
4. **CRM 标记** — 在来源字段记 Referred by [Name]（仅当团队已有 CRM；否则用表格）
5. **归属规则** — first verified introduction wins；争议按首次书面介绍日期裁定

### 激活序列

| 步 | 时机 | 动作 | 责任人 |
| --- | --- | --- | --- |
| 1 | Week 1 | 列出近 2–3 年客户、指定人、承包、经销；按关系热度与影响力打分；优先 10–20 人 | 销售负责人 |
| 2 | Week 2–3 | 按产品上下文目标渠道外展；先非正式说明佣金，再书面确认 | 销售负责人 |
| 3 | Week 3–4 | 向已确认伙伴发送赋能包；建立共享资料夹 | 市场 + 销售 |
| 4 | Month 2 | 按月跟进在谈项目；介绍立即入日志；佣金 7 日内支付 | 销售负责人 |
| 5 | Month 3+ | 复核哪类推荐人与市场产出合格线索；再扩计划 | 销售负责人 |

时机写成日历日或上表相对周次，并在交付物对齐产品上下文的展会或采购周期；禁止只写「某月启动」。

### 赋能包清单

- 产品目录（电子版；印刷版仅当物流与预算可执行）
- 样品政策与申请表
- 价目或报价指引
- 佣金表与支付条款
- 介绍邮件/消息模板
- 已签伙伴/代理协议模板
- 项目资格核对表

每项写分发方式与成本约束。做不到的标 P2 或缺口，不标成必须做。

## 交付

主文档 `deliverables/marketing/06-growth/referral-program.md` 八节，每节建议不少于 150 字；每条建议有采集来源或行业参考值标注：

1. Program objectives — 该品类在目标市场要达成什么
2. Referrer type prioritization — 先推哪类、为何，带来源
3. Commission structure — 分类型费率、支付、资格、毛利调和结论
4. Activation sequence — 五步，含时机、责任人、产出物
5. Tracking & attribution — 工具/字段/规则须匹配团队现有栈
6. Partner enablement — 物料清单与分发
7. First target list framework — 打分标准与候选类别（不编造人名）
8. Action plan — P0 / P1 / P2，各有责任人与到期日

工作簿 `deliverables/marketing/06-growth/referral-program-design.xlsx`（有模板则从 `templates/referral-program-design.xlsx` 复制）：

**Program Design**（≥4 行）

| 列 | 必填 |
| --- | --- |
| referrer_type | 是 |
| persona | 是 |
| reward_model | 是 |
| commission_rate | 是，可解析为百分比或区间，禁止 TBD |
| payment_terms | 是 |
| formality | 是 |
| enablement_items | 是 |
| source | 是，URL 或「行业参考值」 |

**Implementation Plan**（≥5 行）

| 列 | 必填 |
| --- | --- |
| step | 是 |
| timing | 是 |
| action | 是 |
| owner | 是 |
| deliverable | 是 |
| status | 是 |
| source | 是 |

**Referral Log Template** 表头必须含：`date`、`referrer_name`、`referrer_type`、`referred_client`、`project_summary`、`order_value`、`commission_rate`、`commission_due`、`paid_date`、`source`。

按需附件（同目录）：

- `referral-program-design.md` — 资格、奖励、跟踪、支付流程
- `partner-outreach-templates.md` — 指定人、承包、经销、既有客户四类面客稿
- `partner-agreement-template.md` — territory、rate、payment terms、exclusivity、termination
- `referral-tracking-guide.md` — 介绍记录、归属、佣金核对 SOP

终稿禁止留下未替换的品类/市场/产地占位符。面客稿与协议用产品上下文的面客语种；内部策略用简体中文。

## 反模式

- 把推荐链接、病毒循环、自动看板当成外贸默认
- 无来源佣金率，或把行业参考值写成已核实事实
- 忽略样品、印刷目录、物流成本与交期
- 只给激励、不写持续触点与信任动作
- 推荐未核验的软件或频道（团队未使用的 CRM、未在产品上下文出现的即时通讯）
- 协议不写区域、费率、付款、排他、终止
- 交付物留空占位符
- 复购自动计佣

## 质量闸门

- 四类推荐人已映射到产品上下文角色或已标明暂用
- 每条佣金率有 `source` 或行业参考值
- 跟踪不依赖专用推荐软件即可执行
- 激活序列含时机、责任人、产出物
- 赋能包有物料与理由
- 归因规则已定义
- 无 SaaS 裂变战术充当主机制
- 终稿无空占位符
- 主文档与工作簿均有来源栏
- 佣金与已读毛利可调和

## 可验证断言

交付物须能被下列句子检查（写入主文档文末 5–10 条，用本轮事实改写，不抄教学例子）：

1. 主文档含上述八节
2. Program Design ≥4 行且 `source` 非空
3. `commission_rate` 可解析为百分比或区间，无 TBD
4. Implementation Plan ≥5 步，timing / action / owner / deliverable / status 非空
5. Referral Log Template 表头含全部 10 列
6. 佣金建议均有 source 或行业参考值
7. 无未替换的品类/市场/产地占位符
8. 协议大纲含 territory、commission rate、payment terms、exclusivity、termination
9. outreach 含四类模板或已映射并标明暂用
10. 同一文档写明与定价/毛利的调和结论
