# Pilot run: codex

- **harness:** Codex CLI (`codex`)
- **version:** `codex-cli 0.139.0` (npm `@openai/codex`, bin `/Users/chesterjohn/.local/bin/codex`)
- **date:** 2026-10-06 13:18–13:20 CST
- **driver:** subagent, harness = codex
- **copy:** `/tmp/de-linker-pilot-codex/` (rsync `-a --exclude .git` from `/Users/chesterjohn/Documents/de-linker-playbook/`; symlinks preserved)
- **original repo:** not mutated except this log and `wayfinder/pilot/codex/` copies
- **git:** not run
- **auth:** ChatGPT account (`~/.codex/auth.json` present; `codex doctor` reachability ChatGPT HTTP 403 on unauthenticated probe — session itself authenticated)

## Verdict

**PASS** — after CLI flags that actually start a ChatGPT-auth session, a cold `codex exec` with only the next-step prompt completed the thin-slice loop unassisted: injected/read `AGENTS.md`, matched `marketing-orchestrator`, read the ledger, expanded `~` to `$HOME` for `product_context`, read `marketing-copywriting/SKILL.md`, wrote a non-empty `deliverables/value-proposition.md` (not the skill example; 224-SKU is in `CONTEXT.md`), rewrote the ledger to `phase: 2` / `next: stop`, and stopped. No extra user prompt. No web search.

Not a FAIL on auth. Attempt 1 never entered the agent loop (default model rejected). Attempt 2 is the scored run.

## Headless / permission flags (portability)

Discovered from `codex --help` / `codex exec --help` (0.139.0):

| Need | Flag |
| --- | --- |
| Non-interactive / batch | `codex exec` (alias `codex e`). Top-level `codex [PROMPT]` is TUI and refuses `TERM=dumb`. |
| Write inside the copy | `--sandbox workspace-write` (lowest write-capable of `read-only` / `workspace-write` / `danger-full-access`) |
| Read `~/Documents/New/CONTEXT.md` outside the copy | `-c 'sandbox_permissions=["disk-full-read-access"]'` (help example). Observed sandbox still `network_access: false`. |
| Never hang on approvals | `-c approval_policy=never` (`codex exec` has **no** `-a/--ask-for-approval`; that flag is top-level TUI only) |
| Nuclear unattended | `--dangerously-bypass-approvals-and-sandbox` — **not used** |
| No Claude-style names | no `--permission-mode`, `--full-auto`, `--yolo`, `acceptEdits` |
| Copy has no `.git` | **`--skip-git-repo-check` required** or exec refuses |
| Cold start | omit `exec resume` / `--last`; default exec is a new thread |
| Trace tools | `--json` (JSONL events); `-o/--output-last-message FILE` |
| Working root | `-C/--cd DIR` |
| Stdin | non-TTY exec prints `Reading additional input from stdin...` and will append piped stdin to the prompt. Use `</dev/null`. |

User `~/.codex/config.toml` **does not load** on 0.139.0: `features.context_management` is a table, CLI expects a boolean (`invalid type: map, expected a boolean`). `--ignore-user-config` is required on this machine (auth still uses `CODEX_HOME`). That also dropped the user’s MCP web tools / `danger-full-access`, which is closer to a portable cold start.

`--ignore-user-config` default model is **`gpt-5.4`**, which ChatGPT login rejects (see attempt 1). Need `-m` to a ChatGPT-allowed slug. Local `models_cache.json` listed `gpt-5.5`.

## Headless command

Attempt 1 (default model, failed before tools):

```bash
cd /tmp/de-linker-pilot-codex
codex exec \
  --ignore-user-config \
  --skip-git-repo-check \
  --sandbox workspace-write \
  -c 'sandbox_permissions=["disk-full-read-access"]' \
  -c approval_policy=never \
  -C /tmp/de-linker-pilot-codex \
  --color never \
  --json \
  -o /tmp/codex-pilot-run/last-message.txt \
  "Do the next step this repo is set up to do. Do not ask me to explain the repo."
```

Attempt 2 (scored; stdin closed):

```bash
cd /tmp/de-linker-pilot-codex
codex exec \
  --ignore-user-config \
  --skip-git-repo-check \
  --sandbox workspace-write \
  -c 'sandbox_permissions=["disk-full-read-access"]' \
  -c approval_policy=never \
  -m gpt-5.5 \
  -C /tmp/de-linker-pilot-codex \
  --color never \
  --json \
  -o /tmp/codex-pilot-run/last-message.txt \
  "Do the next step this repo is set up to do. Do not ask me to explain the repo." \
  < /dev/null
```

No `--search`. Prompt was exactly that one sentence.

## Attempts

1. 2026-10-06 13:18:23–13:18:40. Exit 1. JSONL: `The 'gpt-5.4' model is not supported when using Codex with a ChatGPT account.` Also: `failed to load models cache: missing field base_instructions`. No workspace writes.
2. 2026-10-06 13:19:27–13:20:51. Exit 0. Model `gpt-5.5`. Session `01a10fa7-2676-7c11-9ac6-bd99d9ee331f`. `duration_ms: 75548`. Usage: `input_tokens 221759` (cached 190848), `output_tokens 2859`. Under the 10-minute cap; not killed.

## Checklist

| # | Item | Result |
| --- | --- | --- |
| ① | Actively read `AGENTS.md` | **Yes (harness inject).** Session rec 4: `# AGENTS.md instructions for /tmp/de-linker-pilot-codex` concatenates `~/.codex/AGENTS.md` + repo `AGENTS.md` (`# 本仓库` … `~` expansion note). No later `sed` of `AGENTS.md`. |
| ② | Found skill dir / orchestrator | **Yes.** Auto skill list included repo skills at `/private/tmp/de-linker-pilot-codex/skills/marketing-orchestrator/SKILL.md` and `marketing-copywriting` (`.agents/skills/` symlinks present; scanner resolved to `skills/`). Also listed global `~/.codex/skills/.system/*`. First agent line: use `marketing-orchestrator` because “next step” is routed there. |
| ③ | Called orchestrator before writing | **Yes.** First tools: `sed` `state/status.md` and `skills/marketing-orchestrator/SKILL.md` in parallel. Announced `phase 0` / `marketing-copywriting` / `deliverables/` **before** any `apply_patch`. No Skill() tool — Codex has none; it follows `skills_instructions` then reads `SKILL.md` via `exec_command`. |
| ④ | Read `state/status.md` | **Yes.** First `exec_command`. |
| ⑤ | Actually read `marketing-copywriting/SKILL.md` | **Yes.** `sed -n '1,260p' skills/marketing-copywriting/SKILL.md` before drafting. Later `rg` against the teaching-example strings (`一次上门|行业领先|现场工程师|隔天再来`). |
| ⑥ | Non-empty deliverable; not example paste; no invented numbers | **Yes.** `/tmp/de-linker-pilot-codex/deliverables/value-proposition.md` (616 bytes). Template fields present. Body 62 words, `word_count: 62` (corrected from 65). Example phrases absent. `224-SKU` is in `~/Documents/New/CONTEXT.md` (`224 个`). Missing proof named as missing. CONTEXT not copied into the playbook copy. |
| ⑦ | Wrote ledger | **Yes.** `state/status.md` → `phase: 2`, `phase_name: 试点完成`, `next: stop`; 已完成 has phase 0 (three statements, 产物路径：无) and phase 1 (`deliverables/value-proposition.md`). YAML + 「当前」 table match. **Minor:** one `apply_patch` wrote VP + ledger together — no on-disk `phase: 1` intermediate, though orchestrator asked to rewrite at each phase boundary. |
| ⑧ | Subagent behavior | **No subagent.** Tools: `exec_command` ×13, `apply_patch` ×2. Inline, as the orchestrator allows. |
| ⑨ | Idled waiting for a slash command | **No.** No `/skill` wait. Codex skills are description-matched in the system list, not slash. |
| ⑩ | Other anomalies | See below. `~` expansion **correct:** `sed … /Users/chesterjohn/Documents/New/CONTEXT.md`. |

Copy tree after rsync (symlinks intact):

- `.agents/skills/marketing-orchestrator` → `../../skills/marketing-orchestrator`
- `.agents/skills/marketing-copywriting` → `../../skills/marketing-copywriting`

### ⑩ other

- **Phase 0+1+2 in one turn.** Orchestrator text allows “从当前 phase 做到交付物落地”. Driver cap was “一小步 / 大任务则终止”: 76s, offline, no crawl. Extra `find /Users/chesterjohn/Documents/New -maxdepth 2` (beyond 只读 `product_context`) and `git status --short` on a non-git copy.
- **Stdin:** still logged `Reading additional input from stdin...` with `</dev/null`.
- **Global skill noise:** system skills (imagegen, openai-docs, plugin-creator, …) injected alongside repo skills; agent still picked orchestrator.
- **Sandbox:** attempt 2 `network_access: false`; write limited to the copy (+ tmp). `disk-full-read-access` was enough to read `CONTEXT.md`.
- **Did not enable `--search`.** No `web_search` in the session.

## Key output excerpt

Attempt 1 error:

```json
{"type":"error","message":"{\"type\":\"error\",\"status\":400,\"error\":{\"type\":\"invalid_request_error\",\"message\":\"The 'gpt-5.4' model is not supported when using Codex with a ChatGPT account.\"}}"}
```

Attempt 2 last message (`-o`):

```
Done. I advanced the repo through its configured next step and stopped at `phase: 2`.

Created [value-proposition.md](/tmp/de-linker-pilot-codex/deliverables/value-proposition.md) and updated the ledger at [state/status.md](/tmp/de-linker-pilot-codex/state/status.md) to `next: stop`.

Verification: draft body is 62 words, matches `word_count: 62`, and the skill’s teaching example text did not appear in the deliverable.
```

Deliverable body:

```
De-linker gives buyers a cleaner path from product page to order across a 224-SKU energy-storage catalog: each PDP is rebuilt from verified SKU records, keeps machine-readable parameters intact, and answers only the pre-purchase blockers that can stop checkout. The result is product copy that stays practical without adding comparison detours, upgrade anxiety, or unsupported claims. Missing proof: conversion lift, case studies, certifications.
```

## Deliverables

Copied from the copy into `wayfinder/pilot/codex/`:

- `value-proposition.md`
- `status.md` (ledger after the run)

## Follow-up

Portable unattended Codex needs, on this host: `--ignore-user-config` (or a loadable `config.toml`), `--skip-git-repo-check` if no git, `--sandbox workspace-write` plus read permission for `~` product context, `-c approval_policy=never`, and **an explicit `-m` ChatGPT allows**. Default `gpt-5.4` under `--ignore-user-config` is not that model.
