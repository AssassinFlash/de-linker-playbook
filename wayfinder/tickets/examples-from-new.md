---
wayfinder: task
status: closed
assignee: kimi（2026-10-06 认领，先调研后执行）
resolved: 2026-10-06
blocked_by: []
---

# 例子 New 化

## Question

规格 §2：skill 内例子**优先取自 `~/Documents/New` 的真实材料**（CONTEXT.md、repair-drafts/、fact-base/、根目录文案草稿），且必须标注「仅供理解，禁止引用到输出」。复核发现：当前 81 个 skill 的例子全是通用支架（抽样 8/8 无一取自 New）——标注规矩全对，但材料来源不合规格。

按规格逐 skill 把例子改写为 New 真实材料的教学支架：

- 材料**只读**自 `~/Documents/New`，不得修改该仓库任何文件
- 改写成**通用形状**：借鉴真实材料的结构与语气，但不得带入 SKU 具体参数/型号/价格等事实（避免第二真相源）
- 标注规矩不变：「仅供理解，禁止引用到输出」
- 没有合适 New 材料的 skill，保留通用支架并在 SKILL.md 注明原因

执行：子代理 swarm（按主题分批），主模型 review。**本票不阻塞 ⑦⑧**，可与后续票并行窗口执行。干完关票、地图记账、git 提交。

## 材料源修正（用户定 2026-10-06，优先级高于上文「取自 New」）

用户裁定：New 的站点文案形状部分已过时/有偏差（实证：de-linker.com 线上 10-06 与 New 09-21 替换稿已不一致，New ≠ live）。例子形状改为**按竞品调研映射**：

- **主源**：`~/Documents/de-linker-project/.scratch/encyclopedia-research/`（2026-09-20 竞品百科 32 份成稿：09–12 批发竞品画像、13–18 买家 ICP、19–22 摩擦、23 论坛语言、24 FAQ、25 关税买家语言、26 工具四格、27 OEM 案例结构、28 RFQ 采购、31 术语图、32 跨境）+ `~/Documents/de-linker-project/docs/research/2026-08-28-*`（EU B2B 平台/账户模型/支付/规划工具对标）+ `~/Documents/de-linker-project/contracts/brand-voice-copy-doctrine.md`（定位句）。
- **New 仍是产品事实源**（指路不复制），但站点页面形状不再当例子锚点。
- 三个仓全部**只读**。禁入例子的不变：SKU 参数/型号/价格、PII（论坛用户名、证言人名、地址电话）、竞品原句照抄（百科文件自带此禁令）、内部运维/上线工艺、过时数字（如 08-28 的「74 SKU」、BayWa 待售进度）。
- 没有合适材料的 skill 仍保留通用支架并注明原因。

## Resolution（2026-10-06 关票）

81/81 处理完：约 59 个 skill 的例子锚定到竞品调研形状（encyclopedia-research 09–32 + docs/research 08-28 批次 + brand-voice 定位句），LinkedIn 批先按 New 形状试点后经用户裁定重锚竞品；22 个保留通用支架并在 `## 例子` 注明原因（11 个元 skill 教流程形状；personal-story 无亲身经历语料；contact-discovery/retailer-research/paid-advertising 等部分保留）。主模型逐批验收：规格 §8 第 1/5/6/8 条全绿（name 正则、产品词零命中、标注齐全、行数 <500）；git diff 全程只触及 `## 例子` 与 5 份 references/examples.md。三个外部仓全程只读。
