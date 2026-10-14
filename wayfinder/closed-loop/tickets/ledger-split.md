---
wayfinder: task
status: closed
assignee: claude-code-fact-source-entry (同会话续) 2026-10-14
step: 0
blocked_by: [fact-source-entry]
---

# 台账拆两线

## Question

（AFK）把共用的 `state/status.md` 拆成营销、获客两张台账，各管自己的冷启动阶段与下一步（裁定 Q3），消除「跑一次获客就覆盖营销进度」（审计 #4）。

- 两张台账的文件名与键自定；获客台账补全 phase 0–10 与审批 / 过期状态（现只存在于交付物 frontmatter，见 `skills/lead-generation/references/write-protocol.md`、`orchestration-protocol.md`）。
- 改读写方：`AGENTS.md`「台账」节、`skills/marketing-orchestrator/**`、`skills/lead-generation/**`、`skills/marketing-init/SKILL.md`、`docs/`、`evals/` 中引用台账路径处。
- **只拆不改流程**：瀑布 → 运营循环、证据闸 / 反馈闸是「营销编排改循环」「获客编排改循环」的事；本票不加循环字段，免得两次改形。执行登记与反馈数据也不进台账——它们在底表（Google 表格），台账只记阶段与下一步。
- 迁移现有进度（营销 phase 0 未开始；获客无进度）。

- 依赖已清（2026-10-14）：「事实源入口」已关，本票可以动两个编排 skill 与 `state/status.md` 了。那张票只改了 `product_context` 的值（现为 `docs/fact-sources.md`）和 `next` 的措辞，键名与台账结构没动；拆台账时两张新台账都保留 `product_context: docs/fact-sources.md`（`evals/validate_project.py` 会检查这个键）。

## 完成标准

- `grep -rn "state/status.md"` 在 `skills/ AGENTS.md docs evals` 里只剩指向新文件的引用（或旧文件已删除、引用为 0）。
- 冷启动演练：分别对两条线说「下一步」（本会话内联模拟即可），各自只读写自己的台账，另一张不变。

## 交接

- 新台账文件名与键名，关票时写进「营销编排改循环」「获客编排改循环」「执行登记流程」三张票正文。

## Resolution

（2026-10-14）两张台账：营销 `state/marketing-status.md`（由 `state/status.md` 改名，内容不变，只加「本文件只管营销」两句）、获客 `state/lead-status.md`（新建：phase 0–10、「审批与过期」表、「豁免（user_waiver）」表，回写规则）。旧的 `state/status.md` 已删除。进度迁移：营销 phase 0 未开始，原样迁过来；获客没有进度，从 phase 0 开始。vault `deliverables/lead/` 下只有空目录，没有可迁的审批记录。

改的文件：`AGENTS.md`（「台账」节两条线各指一张；交接说明「状态真源」）、`CONTEXT.md`（「台账」词条）、`README.md`、`docs/getting-started.md`、`docs/legacy-command-migration.md`、`evals/validate_project.py`（检查两张都在、都有 `product_context`，旧文件仍在就报错）、`evals/run_eval.py`（两张都在才算通过）。skill 这边：两个编排 skill 和它们的 `references/`（写入协议、编排协议步骤 0 与 7、依赖图的 `progress` 与豁免说法、发现状态）；`marketing-init`（核两张台账、报告分两行）、`marketing-playbook-standards`、`marketing-evolve` 手改；其余 76 个文件只是机械替换路径，marketing-* 换成营销台账，lead-* 换成获客台账。`~/Documents/New` 的指针句没动，留给「101 个 skill 改指新事实源」。

核验：
- 完成标准里的 grep（`skills/ AGENTS.md docs evals` 里查 `state/status.md`）结果为 0。
- `evals/validate_project.py`、`validate_deliverables.py`、`run_eval.py` 全绿；两份依赖图的 JSON 能解析，`progress` 各指自己那张台账。
- marketing-* 里提到获客台账的只有 `marketing-orchestrator`（一句「不读不写」）、`marketing-init`、`marketing-playbook-standards`（两条线共用）；lead-* 里提到营销台账的只有 `lead-generation`（一句「不读不写」）。
- 冷启动演练（本会话内联模拟）：营销说「下一步」：AGENTS → `state/marketing-status.md` → 营销编排步骤 1，宣布 phase 0、`marketing-profile`、`deliverables/marketing/`；回写只写营销台账。获客说「下一步」：AGENTS → `state/lead-status.md` → 获客编排步骤 1 与协议步骤 0，宣布获客 phase 0、`marketing-profile`、`deliverables/lead/`；回写和审批表只写获客台账。演练只走到宣布这一步，没有改任何台账（前后 md5 一致）。

附带：跑 `evals/run_eval.py` 时，它把两份报告写进了 vault 的 `marketing/00-system/eval-reports/`（脚本自带行为）。这两份是过程产物，删除被本机权限拦下，留给操作者处理。
