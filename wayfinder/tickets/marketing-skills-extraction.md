---
wayfinder: task
status: open
assignee:
blocked_by: [extraction-spec, repo-skeleton]
---

# 38 个 marketing skill 抽取改写

## Question

从 `~/Documents/marketing-playbook-v3/.claude/skills/`（canonical，38 个；root `skills/` 是 legacy 不用）按抽取规格迁入本仓库 `skills/`，保持 `marketing-*` 命名。

执行方式：子代理 swarm，每 skill 一个子代理；按主题分批出 review checkpoint（编排系/基础/SEO/内容/获客/CRO/增长度量）；主模型按验收清单 review，不亲自改写。

注意：跳过 `.claude/product-profile.md`（不锈钢草稿）与任何数据文件；references/ 随各 skill 一并按规格处理。
