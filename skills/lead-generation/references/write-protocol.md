# 获客写入约定

产出只进 `deliverables/lead/`。进度只写 `state/lead-status.md`。不建仓外产出根。

## 目录

```
deliverables/lead/
├── 00-system/
├── 01-icp/
├── 02-companies/
├── 03-contacts/
├── 04-market/
├── 05-usp/
├── 06-outreach/
├── 07-targeted/
├── 08-linkedin/
├── 09-seo/
├── 10-sales/
└── 99-archive/
```

阶段目录一律小写。表文件与策略文档同目录。禁止保留 `deliverables/lead/lead-generation/` 这种套娃路径。

## 写入流程

1. 确认目标阶段目录在本仓库内存在；缺则创建空目录，不删已有文件。
2. 若目标文件已存在且 frontmatter `status` 为 `approved`（已过证据闸）或 `stale`（过闸后过期）：先移到 `deliverables/lead/99-archive/<原阶段目录>/<filename>_YYYY-MM-DD.{md,xlsx}`，再写新文件。
3. 写入 Markdown（frontmatter 见 `orchestration-protocol.md` 写入节）。
4. 需要表时在同目录写 xlsx 或 csv；列名 English snake_case；公司名保持原文。
5. 按编排协议做下游过期检测，并回写台账。

## 归档命名

`deliverables/lead/99-archive/<原阶段目录>/<filename>_YYYY-MM-DD.{md,xlsx}`

模板：`deliverables/lead/99-archive/02-companies/target-companies_YYYY-MM-DD.md`
