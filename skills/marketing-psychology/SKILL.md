---
name: marketing-psychology
description: >
  Use when the user says marketing psychology, buyer psychology, persuasion,
  decision triggers, cognitive biases, behavioral economics, procurement
  psychology, 营销心理学, 买家心理, or 行为设计, or needs B2B decision
  psychology applied to copy, a funnel, quotation, sample kit, or sales call.
  Diagnose the failing stage and persona from the product context; verify
  principles with web search; pick three to five that match the obstacle;
  write cited tactics into the caller stage directory under
  deliverables/marketing/. Invent no scarcity, social proof, or credentials.
  Not for SEO audits, campaign calendars, phase navigation, or consumer-app
  growth hacks.
---

# 买家心理与行为设计

针对已点名的漏斗障碍，选出 3–5 条可引用的行为原则，写成带触点、角色与来源的执行说明。本方法横切各阶段，产出跟调用方目录，不锁品类。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出只进 `deliverables/`、工具写能力。
2. **输入**。读台账 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。若已有 `deliverables/marketing/01-foundation/product-positioning.md`，或调用方阶段目录里已有漏斗/落地页说明，一并读。完成：能指出受众、角色、差异化各依据哪几条；原文不拷进本仓库。上下文不存在则停并写缺口。
3. **诊断**。写清四项再选原则，禁止先堆模型：
   - 失速阶段：访问 → 询盘 → 样品 → 报价 → 订单 → 复购
   - 目标角色：用产品上下文或定位文档里的买家，不发明角色
   - 可观察障碍（报价后沉默、样品未转订单、价格卡死、跨境信任缺口等，必须能指到行为）
   - 已试过的动作与结果
   完成：四项都有依据；选原则的范围已收窄。
4. **采集**。用网页搜索查证，至少覆盖：工业采购决策心理、跨境选供应商的信任信号、损失厌恶或锚定在 B2B 报价中的用法。需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造。需要隔离时 dispatch a subagent, else do it inline。完成：≥5 条带来源的原则、≥3 个带 URL 的行业案例、角色到原则的映射、每条原则对应的漏斗阶段。
5. **选择与落地**。只保留与步骤 3 最相关的 3–5 条原则（禁止罗列全部模型）。每条用「产出」里的原则块填写；对照「默认」伦理栏；冲突的原则写清取舍。完成：每条都有触点、角色、阶段、预期行为变化、来源。
6. **落盘**。产出目录见「默认」。写入下方四个文件（xlsx 从 `templates/psychology-playbook.xlsx` 复制再填）。完成：四文件非空；表行有 `source`；教学支架原文零出现；宣称完成前无未核验占位符。

## 默认

**产出目录（横切）**

- 优先用调用方本轮给出的阶段目录，否则用台账 `output_dir`，再否则按台账 `phase` 对照 `skills/marketing-orchestrator/SKILL.md` 阶段表。
- 路径必须落在 `deliverables/marketing/` 下某阶段小写目录。无法判定则停并写缺口，不写到仓外。
- 调研摘录可另存 `deliverables/marketing/00-research/`，不替代本方法四件套。

**数据**

- 数字、认证、项目数、产能窗口、客户名：只用来自产品上下文、用户本轮、或已抓取 URL 的陈述。
- 缺则在交付物「缺口」节标明并停用该条主张，不编造、不写假稀缺。
- 每条原则必须能回溯采集来源（URL + 访问日期，或上下文指针）。

**伦理**

- 稀缺：仅真实产能或档期。
- 社会证明：仅真实项目数与允许具名的客户。
- 权威：仅公司实际持有的认证与可核实履历。
- 损失厌恶：围绕真实后果，不制造恐惧。
- 互惠：样品与咨询必须是真给的，禁止诱饵。

**工具**

- 查证用网页搜索；需要原文时抓取指定 URL。不写工具 ID。
- 后续要改页面打开 `skills/marketing-landing-page/SKILL.md`，改文案打开 `skills/marketing-copywriting/SKILL.md`，改漏斗打开 `skills/marketing-funnel-optimization/SKILL.md`；文件不存在则只完成本方法交付物。

**渠道**

- 触点写到目标渠道（以产品上下文为准），以及邮件、报价、样品包、销售通话、目录。不默认某一电商平台。

## 写法

先诊断再选原则。消费侧套路不能原样套进多决策人采购。权威、风险、关系信号按产品上下文的目标市场调整。

**原则（B2B 采购常用）**

| 原则 | 用法 | 触发 |
| --- | --- | --- |
| 社会证明 Social Proof | 已核实客户、项目组合、同行买家持有的认证 | 只用上下文里的项目数与市场 |
| 锚定 Anchoring | 先出示高配或全包，再给预算方案 | 报价顺序，不先丢低价 |
| 损失厌恶 Loss Aversion | 把切换成本写成可避免的风险（交期、质量波动、项目罚则） | 指向真实风险 |
| 权威 Authority | 认证、工厂规模、年限、展会出席 | 先凭证再谈价；未出现的履历不写 |
| 互惠 Reciprocity | 样品、技术咨询、规格指南 | 先给真价值 |
| 稀缺 Scarcity | 真实产能窗口、旺季档期、有限咨询时段 | 约束必须可核实 |
| 宜家效应 IKEA Effect | 让买家参与配置（材质、尺寸、包装） | 参与提高感知所有权 |
| 目标梯度 Goal-Gradient | 把订单进度可视化：样品通过 → 报价确认 → 生产 → 出运 → 交付 | 进度可见才催承诺 |
| 禀赋效应 Endowment | 实物样品会提高归还的心理成本 | 样品包促进转化 |
| 当下偏差 Present Bias | 下一步必须可立即做 | 只与真实档期配对 |

**角色 → 原则**

| 角色 | 主原则 | 原因 |
| --- | --- | --- |
| 采购经理 | 锚定、损失厌恶、权威 | 对成本负责，要降风险与供应商可信度 |
| 项目承包方 | 损失厌恶、目标梯度、权威 | 怕延误，跟节点，认已核实凭证 |
| 经销商 / 转售 | 禀赋、转换成本 Switching Costs、互惠 | 要供货稳定，关系投入才动 |
| 建筑师 / 设计师 | 宜家效应、社会证明（同行项目）、具体性 Specificity | 共创规格，跟同行参照，信精确数据 |
| 质量 / 合规 | 权威、出丑效应 Pratfall、具体性 | 认认证，也信诚实披露的限制 |
| 电商转售 | 锚定、默认效应 Default、零价效应 Zero-Price | 浏览选项，接受默认，免费样品促转 |

角色名以产品上下文为准；上表是选型提示，上下文没有的角色不要编进去。

**障碍 → 原则**

| 障碍 | 阶段 | 用这些 |
| --- | --- | --- |
| 询盘转化低 | 访问 → 询盘 | 锚定（价格）、希克定律 Hick's Law（减少选项）、互惠（资料） |
| 价格异议 | 询盘 → 报价 | 锚定、损失厌恶、心理账户 Mental Accounting |
| 跨境信任 | 全程 | 权威、社会证明、互惠、出丑效应 |
| 要制造紧迫 | 报价 → 订单 | 真实稀缺、损失厌恶、目标梯度 |
| 复购弱 | 订单 → 复购 | 禀赋、转换成本、现状偏差 Status-Quo |
| 报价后沉默 | 询盘 → 报价 | 蔡格尼克 Zeigarnik、当下偏差、跟进节奏 |
| 样品未转订单 | 样品 → 订单 | 目标梯度、宜家效应、承诺一致 Commitment |

## 产出

四个文件都写在步骤 6 判定的目录下。

**`marketing-psychology.md`**

```markdown
# 买家心理策略

- source: 台账 product_context（不粘贴原文）
- output_dir:
- challenge:
- persona:
- funnel_stage:
- retrieved: YYYY-MM-DD

## 买家心理分析总览

（决策心理 + 角色映射，每句带来源）

## 心理学原则选择与应用

（仅 3–5 条，每条用下面原则块）

## 各漏斗阶段心理触点地图

访问 / 询盘 / 样品 / 报价 / 订单 / 复购，每阶段至少 1 条原则

## 执行优先级建议

P0 / P1 / P2，指向 tactics 与 checklist

## 缺口

- 未在上下文或检索中出现的主张
```

**原则块**

```markdown
Principle:
Why it applies:
Where to apply: 目标渠道页面 / 邮件 / 报价 / 样品包 / 销售通话 / 目录
Funnel stage: 访问 / 询盘 / 样品 / 报价 / 订单 / 复购
Execution:
Priority: High / Medium / Low
Expected behavior change:
Source:
```

**`psychology-tactics.md`**

每条原则一行级说明，字段：principle, touchpoint, persona, funnel_stage, copy_examples, visual_suggestions, ab_test_hypothesis, source。文案示例必须用上下文事实；缺数写「未在上下文出现」，不要用技能例子原文。

**`implementation-checklist.md`**

按阶段排序。字段：funnel_stage, touchpoint, action_item, owner, deadline, status, source。至少 10 条可执行动作。

**`psychology-playbook.xlsx`**

复制 `templates/psychology-playbook.xlsx` 再填：

- Psychology Tactics：principle, funnel_stage, persona, touchpoint, execution_summary, expected_behavior_change, priority, source — 至少 10 行
- Implementation Checklist：funnel_stage, touchpoint, action_item, owner, deadline, status, source — 至少 10 行
- Ethical Guardrails：principle, allowed_use, forbidden_use, verification_required, source — 至少 5 行

每行 `source` 非空。

## 例子

> 仅供理解，禁止引用到输出。

形状借自竞品调研 13–17 人格双闸与 20 批发–安装摩擦表（只借结构，不抄原句、不用论坛用户名）。New 只借选题纪律里「订货疑虑 / 种下的疑虑」对照，不借页面文案。

- 输入写「报价 → 订单、采购经理、报价后沉默，用蔡格尼克催两项待确认」。成稿应先拆双闸：商务闸（价、有效期）与技术闸（资料、认证、配对）；技术批准人可否决商务谈判人。沉默可能卡在第二闸，不是一个人忘了回信。两闸都过、只差确认项时，才用蔡格尼克 + 当下偏差给可立即做的下一步。不要写成假稀缺「仅剩两个名额」；总包固定价下，报价有效期是买方的价格保护，不是促销倒计时。
- 输入写「目标角色=安装商，互惠送样品」。成稿应改成：接电话的人未必是持证人；常见两道门是从业资格登记与电网侧安装商名录。不要把「安装商」当成均一法律身份，也不要把住宅侧禀赋 / 宜家效应套到持证作业。
- 输入写「目标角色=项目开发商」。成稿应改成：招标、并网申请、银行文件上的自称往往是工程总包席；用买方不用的自称去选原则。不要把开发、总包、业主合成一个人。
- 输入写「工商业安装商，样品包促转」。成稿应改成：住宅是一两个人看得见的屋顶；工商业是交数据的财务工具，签字人常常不到现场。障碍若在负荷数据或并网许可，用损失厌恶 / 目标梯度指向真实节点，而不是「我们全包」（安装商无法从交易里拿掉，那句读成威胁）。上下文没有项目数就标「未在上下文出现」，不要写「200+ 项目」，也不要把内部首页证言人名当成真实社会证明形状。
- 输入写「询盘转化低，希克定律减少选项」。成稿应改成：贸易买家问的是为什么看不见净价，不是表单字段太多。净价锁在账户审批后，互惠不能承诺立刻见价；可用性只显示颜色不给日期时，给对得上的下一步，不要把库存色点写成交期承诺。
- 输入写「跨境信任，权威=我们承保厂家质保」。成稿应改成：批发常见把退换货指向厂家，安装商自己变成投诉通道。权威只写实际持有的认证与可核实履历；限制可诚实披露，自有质保承保 / 制造商口吻不行。交货日不具约束力时，档期承诺不当卖点。
- 输入写「损失厌恶：提醒退款、理赔、金额」。成稿应改成：只拆已经挡住下单的订货疑虑；看完反而多出来的决策负担不写。原则仍只留 3–5 条，对得上本轮障碍。

以上句子不得进入交付物。

## 易错

- 把消费心理学直接套进多决策人采购。
- 一次推荐 8–10 条原则，而不是针对障碍选 3–5 条。
- 只写 high quality / best service，没有对应触发机制。
- 编造稀缺、项目数、认证或案例。
- 不按目标市场调整权威、风险、关系信号。
- 把原则当一次性花招，而不是贯穿漏斗的行为设计。
- 不写预期行为变化（询盘率、样品转订单率等可观察量）。
- 因为「大家都知道」而省来源。
- 用与产品上下文品类不符的行业例子。
- 未判定调用方目录就把文件写死到某一阶段。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 诊断写清阶段、角色、障碍、已试动作
- [ ] ≥5 条原则有检索或报告来源；策略正文只落地 3–5 条
- [ ] 访问→询盘、询盘→报价、报价→订单、订单→复购各至少 1 条原则
- [ ] ≥3 条有针对特定角色的用法；每条含触点、阶段、执行、预期行为变化、来源
- [ ] 稀缺 / 社会证明 / 权威均可被上下文或已抓取 URL 核实，否则列入缺口
- [ ] 四文件在调用方阶段目录；xlsx 三表行数达标且 `source` 非空
- [ ] 无编造统计或案例；宣称完成前无未核验占位符
- [ ] 例子原文未进入交付物
