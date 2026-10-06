---
wayfinder: task
status: open
assignee:
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
