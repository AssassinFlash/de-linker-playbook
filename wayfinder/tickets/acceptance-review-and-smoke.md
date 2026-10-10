---
wayfinder: task
status: closed
assignee: kimi-main (acceptance session 2026-10-10)
blocked_by: [overlap-dedup-adjudication, assets-migration, review-fixes]
---

# 验收：对照 review + 抽查 + 冒烟

## Question

三道闸，检查项以「抽取规格定稿」的验收清单为准（清单吸收研究票的 best-practice 结论）：

1. **子代理逐 skill 对照 review**：方法保真（对照源文件）、无不锈钢残留、无 harness 专属字段、例子标注在位、前缀命名正确
2. **主模型抽查 20%**
3. **真实冒烟**：挑一个导入的 skill 对一个真实 de-linker 任务跑一遍（如用 site-architecture 或 content-strategy 跑一个真实页面），产出可用即过
4. **五家兼容验证**（用户定的目标：Kimi / Z Code / DeepSeek / OpenCode / Hermes）：逐家冷启动实测，矩阵与通过标准参照试点薄片（`wayfinder/pilot/`）。先探测各 CLI 的安装与登录状态，缺环境的列出来由用户决定装不装（环境准备不算票内工作）

随本票定稿 `AGENTS.md` / `README.md` 终稿（含跨 harness 交接说明）。全部通过后地图闭环。

## Resolution

验收三道闸 + 五家兼容验证，全部通过（2026-10-10）。

1. **子代理逐 skill 对照 review（80/80）**：77 PASS + 3 FAIL（均为方法保真），当轮修复并独立复读确认：
   - `lead-linkedin-pain-solution`：恢复源方法的「用户选定痛点」闸——点名则用；未点名且能问则只问选哪条、先不写帖；不能问则取证据最强一条并标「痛点未经用户确认」。
   - `lead-service-delivery`：双语要求恢复为所有面客件（四阶段时间线面客文案、一页包装协议、周更、安抚件均 EN + 对照语种）；包装风险协议必含行恢复（纸箱材厚、抗压/耐破、防潮等级、泡沫密度、气泡膜层数、护角，值或 `[待补充]`）。
   - `lead-teach`：`references/stage-templates.md` 与 SKILL.md 的 Stage 3/4 对齐——Stage 3 只留系统执行解说，反馈模板与 coverage 移到 Stage 4，隔离规则不再自相矛盾。
2. **workbook WARN 评估**：17 行全部裁定为误报——lead 系 xlsx 名是方法描述的用户产出物（`deliverables/lead/…`），不是 `templates/` 模板；不补模板、不改文案。若以后要消 WARN，validator 应白名单 `deliverables/lead/` 路径，而不是造空模板。
3. **主模型抽查 20%（16/16 PASS）**：跨编排（orchestrator/lead-generation/init）、阶段包（foundation/content/cro）、营销方法（copywriting/seo-audit/pricing）、lead 研究（company/targeted/data-validation）、外展内容（cold-email-gen/linkedin-pain-solution）、服务（objection）、评估（skill-eval）七族，逐一读目标 + 源对照。
4. **真实冒烟（S4）**：`marketing-site-and-schema` 对 de-linker.com 实跑，产出 `deliverables/marketing/02-seo/site-and-schema.md`（+ xlsx/json），主模型亲读判可用（真实 URL 证据、诚实缺口、无编造、无不锈钢残留、无 harness 工具 ID）。摩擦两条当轮清账：`templates/site-schema-blueprint.xlsx` 的「Shopify Insertion Point」列名平台锁残留 → 改 `Insertion Point`（模板与冒烟产出同步改）；`evals/validate_deliverables.py` 的 Metadata 豁免兼容前导下划线变体。
5. **五家冷启动实测（S1 推进 + S3 寒暄，全 PASS）**：kimi 203s、OpenCode 85s（默认 xai 模型 invalid_grant，显式 `-m deepseek/deepseek-v4-pro` 后过）、DeepSeek `dsh` 107s、Z Code 213s（`zcode -p` 需桌面同步的 provider 配置）、Hermes 122s（宿主 `terminal.cwd` 会桥接覆盖 `--in`，需 `HERMES_HOME` 隔离才真换根）。各家的 flag 矩阵、命令与证据在 `wayfinder/pilot/<harness>.md`。S3 全部只复述 phase 不改文件（逐文件 checksum 验证）。原仓库台账未动，实测全在 /tmp 副本。

随本票定稿 `AGENTS.md`（交接说明补 pilot 矩阵指针）与 `README.md`（当前状态改为验收结论）。地图闭环。
