import type { Inquiry } from "./types"

export const LEVEL: Record<string, [string, string]> = {
  L0: ["已执行", "做了，搜索还没看到这一页。"],
  "未到 L1": ["还没被看到", "检查过，但还没进搜索结果。"],
  L1: ["已被看到", "已收录，或搜索结果里已经有展示。"],
  L2: ["有互动", "有人从搜索点进来，或邮件有了回复。"],
  L3: ["有转化", "有询盘归因到这次动作。"],
}

export function levelName(level?: string) {
  if (!level) return "—"
  const pair = LEVEL[level]
  return pair ? `${pair[0]} · ${level}` : level
}

export function money(row: Pick<Inquiry, "currency" | "total">) {
  if (!row.total) return "—"
  return `${row.currency || ""} ${row.total}`.trim()
}

export function askOf(row: Inquiry) {
  if (row.items?.length) {
    return row.items.map((item) => item.name + (item.quantity != null && item.quantity !== "" ? ` × ${item.quantity}` : "")).join("；")
  }
  return row.note || row.project || row.topic || "这单没有行项目，也没有备注"
}

export function shortUrl(url?: string) {
  if (!url) return "—"
  try {
    const parsed = new URL(url)
    return parsed.pathname && parsed.pathname !== "/" ? parsed.pathname : parsed.host
  } catch {
    return url
  }
}

export function fieldLabel(label: string) {
  return label.replace(/_/g, " ")
}

export function pct(part: number, total: number) {
  return total ? Math.round((part / total) * 100) : 0
}

export function countBy<T>(rows: T[], key: (row: T) => string) {
  const out = new Map<string, number>()
  rows.forEach((row) => {
    const name = key(row) || "未标"
    out.set(name, (out.get(name) || 0) + 1)
  })
  return [...out.entries()].map(([label, value]) => ({ label, value })).sort((a, b) => b.value - a.value)
}

export function byDate(rows: { date?: string }[]) {
  const out = new Map<string, number>()
  rows.forEach((row) => {
    if (row.date) out.set(row.date, (out.get(row.date) || 0) + 1)
  })
  return [...out.entries()].sort().map(([date, value]) => ({ date, label: date.slice(5), value }))
}

export function matches(query: string, text: string) {
  const q = query.trim().toLowerCase()
  return !q || text.toLowerCase().includes(q)
}

export function show(value: unknown) {
  return value == null || value === "" ? "—" : String(value)
}
