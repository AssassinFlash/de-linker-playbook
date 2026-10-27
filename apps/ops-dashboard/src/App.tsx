import { useEffect, useMemo, useState, type ReactNode } from "react"
import { BarChart, DonutChart, LineChart } from "./components/Chart"
import { ActionDetail, InquiryDetail, PageDetail } from "./components/Detail"
import { askOf, byDate, countBy, levelName, LEVEL, matches, money, pct, shortUrl } from "./format"
import type { ActionRow, Dashboard, Inquiry, MailEvent } from "./types"

const NAV = [
  ["overview", "总览"],
  ["quality", "质量"],
  ["pace", "节奏"],
  ["inquiries", "询盘"],
  ["actions", "动作"],
  ["trend", "趋势"],
  ["pages", "收录"],
  ["mail", "邮件"],
  ["visits", "访问"],
  ["later", "还没接上"],
] as const

type Screen = (typeof NAV)[number][0]
type Detail = { kind: "inq" | "act" | "page" | "day-inq" | "day-act" | "mail"; id: string } | null

export default function App() {
  const [data, setData] = useState<Dashboard | null>(null)
  const [error, setError] = useState("")
  const [screen, setScreen] = useState<Screen>("overview")
  const [query, setQuery] = useState("")
  const [status, setStatus] = useState("")
  const [detail, setDetail] = useState<Detail>(null)

  useEffect(() => {
    fetch("/data.json", { cache: "no-store" })
      .then((response) => { if (!response.ok) throw new Error("还没有导出") ; return response.json() })
      .then(setData)
      .catch((err: Error) => setError(err.message))
  }, [])

  if (error) return <p className="p-8 text-foreground">读不到本地导出。先运行 uv run scripts/dashboard.py export。{error}</p>
  if (!data) return <p className="p-8 text-muted-foreground-1">正在读本地导出…</p>

  return (
    <div className="min-h-screen bg-background-1 text-foreground">
      <aside className="fixed inset-y-0 start-0 z-20 flex w-64 flex-col border-e border-sidebar-divider bg-sidebar">
        <div className="px-5 py-5">
          <strong className="block text-sm">运营看板</strong>
          <span className="text-xs text-muted-foreground-1">本机，含申请正文</span>
        </div>
        <nav className="flex flex-1 flex-col gap-1 px-3">
          {NAV.map(([id, label]) => (
            <button key={id} type="button" onClick={() => { setScreen(id); setDetail(null) }} className={`rounded-lg px-3 py-2 text-start text-sm text-sidebar-nav-foreground hover:bg-sidebar-nav-hover ${screen === id ? "bg-sidebar-nav-active" : ""}`}>{label}</button>
          ))}
        </nav>
        <footer className="border-t border-sidebar-divider px-5 py-4 text-xs leading-5 text-muted-foreground-1">导出 {data.exportedAt}<br />点开一行看全文<br />正文不写回底表</footer>
      </aside>
      <main className="min-h-screen ps-64">
        <div className="flex flex-col gap-5 px-5 py-6">
          {screen === "overview" && <Overview data={data} open={setDetail} />}
          {screen === "quality" && <Quality data={data} />}
          {screen === "pace" && <Pace data={data} open={setDetail} />}
          {screen === "inquiries" && <Inquiries data={data} query={query} setQuery={setQuery} status={status} setStatus={setStatus} open={setDetail} />}
          {screen === "actions" && <Actions data={data} query={query} setQuery={setQuery} open={setDetail} />}
          {screen === "trend" && <Trend data={data} />}
          {screen === "pages" && <Pages data={data} query={query} setQuery={setQuery} open={setDetail} />}
          {screen === "mail" && <Mail data={data} open={setDetail} />}
          {screen === "visits" && <Visits data={data} />}
          {screen === "later" && <Later data={data} />}
        </div>
      </main>
      {detail ? <Drawer data={data} detail={detail} onClose={() => setDetail(null)} open={setDetail} /> : null}
    </div>
  )
}

const L3_INQUIRY_LIMIT = "L3 只含形式发票申请，联系表单和直接来信不可计。"

function Header({ title, lede, asof, note }: { title: string; lede: string; asof: string; note?: string }) {
  return (
    <div className="flex flex-wrap items-end justify-between gap-3">
      <div>
        <h1 className="text-lg font-semibold">{title}</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted-foreground-1">{lede}</p>
        {note ? <p className="mt-1 max-w-3xl text-sm text-muted-foreground-1">{note}</p> : null}
      </div>
      <span className="rounded-lg border border-layer-line bg-layer px-2.5 py-1.5 text-xs text-muted-foreground-1">导出 {asof}</span>
    </div>
  )
}

function Card({ title, note, children }: { title: string; note?: string; children: ReactNode }) {
  return (
    <section className="flex flex-col rounded-xl border border-card-line bg-card shadow-xs">
      <div className="px-5 pt-5">
        <h2 className="font-semibold">{title}</h2>
        {note ? <p className="mt-1 text-xs text-muted-foreground-1">{note}</p> : null}
      </div>
      <div className="p-5 pt-3">{children}</div>
    </section>
  )
}

function Table({ headers, children }: { headers: string[]; children: ReactNode }) {
  return (
    <div className="max-h-[640px] overflow-auto">
      <table className="w-full text-sm">
        <thead className="sticky top-0 bg-card text-left text-xs text-muted-foreground-1"><tr>{headers.map((header) => <th key={header} className="px-3 py-2 font-medium">{header}</th>)}</tr></thead>
        <tbody>{children}</tbody>
      </table>
    </div>
  )
}

function Search({ value, set, placeholder }: { value: string; set: (value: string) => void; placeholder: string }) {
  return <input value={value} onChange={(event) => set(event.target.value)} placeholder={placeholder} className="mb-3 w-full max-w-sm rounded-lg border border-layer-line bg-layer px-3 py-2 text-sm outline-none" />
}

function Overview({ data, open }: { data: Dashboard; open: (detail: Detail) => void }) {
  const days = byDate(data.actions)
  const reached = data.ladder.L1
  const missed = Math.max(0, data.ladder.L0 - reached)
  const openCount = data.inquiries.items.filter((row) => row.status === "询盘已收到").length
  return (
    <>
      <Header title="总览" asof={data.exportedAt} lede={`${data.ladder.L0} 次已经做了，${pct(reached, data.ladder.L0)}% 被看到。有互动 ${data.ladder.L2}，有转化 ${data.ladder.L3}。申请 ${data.inquiries.items.length} 笔，仍在流程的 ${openCount} 笔。点进询盘看申请了什么。`} />
      <div className="grid gap-3 sm:grid-cols-5">
        {[["已执行", data.ladder.L0], ["已被看到", data.ladder.L1], ["有互动", data.ladder.L2], ["有转化", data.ladder.L3], ["申请", data.inquiries.items.length]].map(([label, value]) => (
          <article key={String(label)} className="rounded-xl border border-card-line bg-card p-4 shadow-xs"><p className="text-sm text-muted-foreground-1">{label}</p><p className="mt-1 text-3xl font-semibold">{value}</p></article>
        ))}
      </div>
      <p className="max-w-3xl text-sm text-muted-foreground-1">{L3_INQUIRY_LIMIT}</p>
      <div className="grid gap-4 xl:grid-cols-[1.3fr_.7fr]">
        <Card title="每天做了多少" note="柱高是当天新登记的动作。悬停看具体数字。"><BarChart points={days.map((day) => ({ label: day.label, full: day.date, value: day.value }))} onPick={(index) => open({ kind: "day-act", id: days[index].date })} /></Card>
        <Card title="做到了没有" note="只分两块：已被看到，和还停在已执行。"><DonutChart center={`${pct(reached, data.ladder.L0)}%`} slices={[{ label: "已被看到", value: reached }, { label: "还没被看到", value: missed }]} /></Card>
      </div>
      <Card title="最近做了什么" note="点一行看查证证据和页面后来怎样。">
        <Table headers={["日期", "动作", "内容说明", "现在怎样"]}>{data.actions.slice(0, 8).map((row) => <ActionLine key={row.id} row={row} open={open} />)}</Table>
      </Card>
    </>
  )
}

function Quality({ data }: { data: Dashboard }) {
  const indexed = data.pages.filter((row) => row.status === "已收录").length
  const levels = ["L0", "L1", "L2", "L3"].map((key) => ({ label: LEVEL[key][0], full: `${LEVEL[key][0]} · ${key}`, value: data.actions.filter((row) => row.level === key).length }))
  const statuses = countBy(data.pages, (row) => row.status).map((item) => ({ ...item, label: shortStatus(item.label), full: item.label }))
  return (
    <>
      <Header title="质量" asof={data.exportedAt} lede="左边是动作有没有被看到。右边是网址现在卡在哪一种收录状态。" />
      <Glossary />
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="动作" note={`${data.ladder.L1} / ${data.ladder.L0} 到了已被看到。`}><BarChart points={levels} /></Card>
        <Card title="收录" note={`${indexed} / ${data.gsc.indexUrls} 个网址已收录。`}><BarChart points={statuses} /></Card>
      </div>
    </>
  )
}

function Pace({ data, open }: { data: Dashboard; open: (detail: Detail) => void }) {
  const actions = byDate(data.actions)
  const inquiries = byDate(data.inquiries.items.map((row) => ({ date: row.created.slice(0, 10) })))
  return (
    <>
      <Header title="节奏" asof={data.exportedAt} lede="左边是我们动手的日子，右边是申请进来的日子。点一根柱子，看那天的明细。" />
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="动作" note="按执行日期。"><BarChart points={actions.map((day) => ({ label: day.label, full: day.date, value: day.value }))} onPick={(index) => open({ kind: "day-act", id: actions[index].date })} /></Card>
        <Card title="申请" note="按创建日期。"><BarChart points={inquiries.map((day) => ({ label: day.label, full: day.date, value: day.value }))} onPick={(index) => open({ kind: "day-inq", id: inquiries[index].date })} /></Card>
      </div>
    </>
  )
}

function Inquiries({ data, query, setQuery, status, setStatus, open }: { data: Dashboard; query: string; setQuery: (value: string) => void; status: string; setStatus: (value: string) => void; open: (detail: Detail) => void }) {
  const items = data.inquiries.items
  const statuses = ["询盘已收到", "形式发票已开", "已完成", "已取消"]
  const counts = Object.fromEntries(statuses.map((name) => [name, items.filter((row) => row.status === name).length]))
  const days = byDate(items.map((row) => ({ date: row.created.slice(0, 10) })))
  const rows = items.filter((row) => (!status || row.status === status) && matches(query, [row.number, row.company, row.contact, row.email, row.note, row.project, askOf(row), row.status].join(" ")))
  return (
    <>
      <Header title="询盘" asof={data.exportedAt} lede="点任何一行，看联系人、申请了什么、客户原话、规格和单据。这些正文只在这台电脑上，没有写回底表。" note={L3_INQUIRY_LIMIT} />
      {data.inquiries.liveError ? <p className="rounded-xl bg-destructive/10 px-3 py-2 text-sm text-destructive">申请正文这次没取到：{data.inquiries.liveError}</p> : null}
      <div className="grid gap-4 xl:grid-cols-[.8fr_1.2fr]">
        <Card title="结果" note={`共 ${items.length} 笔。已签发 ${data.inquiries.issued}。已归因 ${data.inquiries.attributed}。来源对不上执行登记的，归因留空。`}><DonutChart center={String(counts["询盘已收到"] || 0)} slices={statuses.map((name) => ({ label: name, value: counts[name] || 0 }))} /></Card>
        <Card title="怎么进来的" note="只记类别。没有来源记录的不画进图。"><DonutChart center={String(items.filter((row) => row.source).length)} slices={countBy(items.filter((row) => row.source), (row) => row.source || "").map((item) => ({ label: item.label, value: item.value }))} /></Card>
        <Card title="进来的节奏" note="每个点是当天新提交的申请。">{days.length > 1 ? <LineChart categories={days.map((day) => day.label)} series={[{ name: "申请", data: days.map((day) => day.value) }]} /> : <BarChart points={days.map((day) => ({ label: day.label, full: day.date, value: day.value }))} />}</Card>
      </div>
      <Card title="申请列表" note="点一行展开。搜索公司、联系人、产品或备注。">
        <div className="mb-3 flex flex-wrap gap-2">{[["", `全部 ${items.length}`], ...statuses.map((name) => [name, `${name} ${counts[name] || 0}`] as [string, string])].map(([id, label]) => <button key={id || "all"} type="button" onClick={() => setStatus(id)} className={`rounded-full border px-3 py-1 text-xs ${status === id ? "border-foreground bg-foreground text-background-1" : "border-layer-line bg-layer"}`}>{label}</button>)}</div>
        <Search value={query} set={setQuery} placeholder="搜索申请" />
        <Table headers={["创建", "单号", "公司 / 联系人", "来源", "申请了什么", "金额", "状态"]}>
          {rows.map((row) => <tr key={row.id} onClick={() => open({ kind: "inq", id: row.id })} className="cursor-pointer border-t border-card-divider hover:bg-muted-hover"><td className="whitespace-nowrap px-3 py-3">{row.created.slice(0, 16)}</td><td className="px-3">{row.number || row.id}</td><td className="px-3">{row.company || "没有公司名"}<br /><span className="text-xs text-muted-foreground-1">{row.contact}</span></td><td className="px-3">{row.source || "没有来源记录"}</td><td className="max-w-md px-3 whitespace-pre-wrap">{askOf(row)}</td><td className="whitespace-nowrap px-3">{money(row)}</td><td className="px-3"><span className="rounded-full bg-primary/10 px-2 py-0.5 text-xs text-primary">{row.status}</span></td></tr>)}
        </Table>
      </Card>
    </>
  )
}

function Actions({ data, query, setQuery, open }: { data: Dashboard; query: string; setQuery: (value: string) => void; open: (detail: Detail) => void }) {
  const levels = ["L0", "L1", "L2", "L3"].map((key) => ({ label: LEVEL[key][0], full: levelName(key), value: data.actions.filter((row) => row.level === key).length }))
  const rows = data.actions.filter((row) => matches(query, [row.id, row.action, row.summary, row.url, row.company, row.level].join(" ")))
  return (
    <>
      <Header title="动作" asof={data.exportedAt} lede="已执行是做了还没被看到。已被看到是到了搜索结果。有互动、有转化如果是 0，就是还没有点击或归因询盘。" />
      <Glossary />
      <Card title="现在停在哪一级" note="一个动作只算一次。悬停看个数。"><BarChart points={levels} /></Card>
      <Card title="做了什么" note="内容说明来自执行登记。点一行看查证证据和收录原因。">
        <Search value={query} set={setQuery} placeholder="搜索动作、说明或网址" />
        <Table headers={["日期", "动作", "内容说明", "页面", "收录", "现在怎样"]}>{rows.map((row) => <ActionLine key={row.id} row={row} open={open} wide />)}</Table>
      </Card>
    </>
  )
}

function Trend({ data }: { data: Dashboard }) {
  const grouped = useMemo(() => {
    const by = new Map<string, { impressions: number; clicks: number }>()
    data.performance.forEach((row) => {
      const cur = by.get(row.date) || { impressions: 0, clicks: 0 }
      cur.impressions += row.impressions
      cur.clicks += row.clicks
      by.set(row.date, cur)
    })
    return [...by.entries()].sort()
  }, [data.performance])
  return (
    <>
      <Header title="趋势" asof={data.exportedAt} lede={data.gsc.performanceRows ? "折线看搜索表现。悬停某个点看展示和点击。" : "网页表现现在是 0 行，所以这里不画一条贴在轴上的 0 线。"} />
      <Card title="展示和点击" note={data.gsc.performanceRows ? "左右留空，点和字不贴边。" : "底表的网页表现是空的。等 GSC 回流写出行之后，这里才是折线。"}>
        {data.gsc.performanceRows ? <LineChart categories={grouped.map(([date]) => date.slice(5))} series={[{ name: "展示", data: grouped.map(([, value]) => value.impressions) }, { name: "点击", data: grouped.map(([, value]) => value.clicks) }]} /> : <p className="py-16 text-center text-sm text-muted-foreground-1">没有搜索表现数据。<br />不是图坏了。</p>}
      </Card>
      {data.queries.length ? <Card title="搜索词" note="有点击或展示的词。"><Table headers={["日期", "搜索词", "展示", "点击"]}>{data.queries.slice(0, 50).map((row) => <tr key={row.date + row.query} className="border-t border-card-divider"><td className="px-3 py-2">{row.date}</td><td className="px-3">{row.query}</td><td className="px-3">{row.impressions}</td><td className="px-3">{row.clicks}</td></tr>)}</Table></Card> : null}
    </>
  )
}

function Pages({ data, query, setQuery, open }: { data: Dashboard; query: string; setQuery: (value: string) => void; open: (detail: Detail) => void }) {
  const items = countBy(data.pages, (row) => row.status)
  const indexed = items.find((item) => item.label === "已收录")?.value || 0
  const rows = data.pages.filter((row) => matches(query, [row.url, row.status, row.reason, row.compared].join(" ")))
  return (
    <>
      <Header title="收录" asof={data.exportedAt} lede={`${data.gsc.indexUrls} 个网址，${data.gsc.indexRows} 次检查。点一行看原因、正式地址和历次检查。`} />
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="结构" note="一个网址只算最新一次检查。"><DonutChart center={`${pct(indexed, data.gsc.indexUrls)}%`} slices={items} /></Card>
        <Card title="哪一种最多" note="柱高是网址数。完整状态名在悬停里。"><BarChart points={items.map((item) => ({ label: shortStatus(item.label), full: item.label, value: item.value }))} /></Card>
      </div>
      <Card title="网址" note="原因说明来自收录检查，不是只有一个状态词。">
        <Search value={query} set={setQuery} placeholder="搜索网址或原因" />
        <Table headers={["网址", "收录状态", "原因说明", "检查日期", "和上次比"]}>
          {rows.map((row) => <tr key={row.url} onClick={() => open({ kind: "page", id: row.url })} className="cursor-pointer border-t border-card-divider hover:bg-muted-hover"><td className="max-w-xs break-all px-3 py-3 text-primary">{shortUrl(row.url)}</td><td className="px-3">{row.status}</td><td className="max-w-md px-3">{row.reason}</td><td className="whitespace-nowrap px-3">{row.checked}</td><td className="px-3">{row.compared}</td></tr>)}
        </Table>
      </Card>
    </>
  )
}

function Mail({ data, open }: { data: Dashboard; open: (detail: Detail) => void }) {
  const events = data.mail.events
  const byEvent = countBy(events, (row) => row.event || "未分类")
  const byLevel = countBy(events, (row) => row.level || "未分级")
  return (
    <>
      <Header title="邮件" asof={data.exportedAt} lede={data.mail.rule} />
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="事件" note={`${events.length} 行。点表里的一行看分类和编号。`}>
          {events.length ? <DonutChart center={String(events.length)} slices={byEvent.map((item) => ({ label: item.label, value: item.value }))} /> : <p className="py-16 text-center text-sm text-muted-foreground-1">还没有已登记的发信，所以这里不画假图。</p>}
        </Card>
        <Card title="走到哪一级" note="未见退信是推断，不是投递回执。">
          {events.length ? <BarChart points={byLevel.map((item) => ({ label: item.label, value: item.value }))} /> : <p className="py-16 text-center text-sm text-muted-foreground-1">没有级别可画。</p>}
        </Card>
      </div>
      <Card title="事件明细">
        <Table headers={["日期", "登记编号", "公司", "事件", "级别", "退信码", "回复分类"]}>
          {events.map((row) => <tr key={`${row.id}-${row.event}-${row.replyId}`} onClick={() => open({ kind: "mail", id: mailKey(row) })} className="cursor-pointer border-t border-card-divider hover:bg-muted-hover"><td className="whitespace-nowrap px-3 py-3">{row.date}</td><td className="px-3 text-primary">{row.id}</td><td className="px-3">{row.company}</td><td className="px-3">{row.event}</td><td className="px-3">{row.level}</td><td className="px-3">{row.bounce}</td><td className="px-3">{row.replyClass}</td></tr>)}
        </Table>
      </Card>
    </>
  )
}

function mailKey(row: MailEvent) {
  return [row.id, row.event, row.replyId].join("|")
}

function Visits({ data }: { data: Dashboard }) {
  const ga = data.ga4
  return (
    <>
      <Header title="访问" asof={data.exportedAt} lede={ga.rule} note={ga.window ? `${ga.window} · ${ga.timezone}` : undefined} />
      {ga.error ? <p className="rounded-xl bg-destructive/10 px-3 py-2 text-sm text-destructive">这次没取到访问数：{ga.error}</p> : null}
      <div className="grid gap-3 sm:grid-cols-3">
        {[["会话", ga.sessions], ["用户", ga.users], ["浏览", ga.pageViews]].map(([label, value]) => (
          <article key={String(label)} className="rounded-2xl border border-card-line bg-card p-4"><span className="text-sm text-muted-foreground-1">{label}</span><strong className="mt-1 block text-3xl">{value}</strong></article>
        ))}
      </div>
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="来源" note="近 7 天会话。直接访问表示没有带来源标记。">
          {ga.sources.length ? <DonutChart center={String(ga.sessions)} slices={ga.sources.map((row) => ({ label: row.label, value: row.sessions }))} /> : <p className="py-16 text-center text-sm text-muted-foreground-1">这 7 天没有同意分析的访问，所以不画假图。</p>}
        </Card>
        <Card title="按日" note="德国时间。今天的数可能还不全。">
          {ga.byDate.length ? <BarChart points={ga.byDate.map((row) => ({ label: row.date.slice(5), full: row.date, value: row.sessions }))} /> : <p className="py-16 text-center text-sm text-muted-foreground-1">没有按日的会话。</p>}
        </Card>
      </div>
      <div className="grid gap-4 xl:grid-cols-2">
        <Card title="着陆页">
          <Table headers={["路径", "会话"]}>
            {ga.landings.map((row) => <tr key={row.path} className="border-t border-card-divider"><td className="px-3 py-3">{row.path}</td><td className="px-3">{row.sessions}</td></tr>)}
          </Table>
        </Card>
        <Card title="事件" note={ga.inquiryEvents.length ? "含询盘相关事件。" : "这 7 天没有询盘相关事件。"}>
          <Table headers={["事件", "次数"]}>
            {ga.events.map((row) => <tr key={row.name} className="border-t border-card-divider"><td className="px-3 py-3">{row.name}</td><td className="px-3">{row.count}</td></tr>)}
          </Table>
        </Card>
      </div>
    </>
  )
}

function Later({ data }: { data: Dashboard }) {
  return (
    <>
      <Header title="还没接上" asof={data.exportedAt} lede="邮件和访问都已接上。这里不再留空图。" />
      <Card title="没有待接的来源" note="GSC 搜索表现仍可能是 0，那是 Google 还没给出搜索行，不是没接。"><p className="py-16 text-center text-sm text-muted-foreground-1">没有还要接的数据源</p></Card>
    </>
  )
}

function Glossary() {
  return <div className="grid gap-3 sm:grid-cols-4">{["L0", "L1", "L2", "L3"].map((key) => <article key={key} className="rounded-xl border border-card-line bg-card p-3"><strong className="block text-sm">{LEVEL[key][0]} · {key}</strong><span className="text-xs text-muted-foreground-1">{LEVEL[key][1]}</span></article>)}</div>
}

function ActionLine({ row, open, wide }: { row: ActionRow; open: (detail: Detail) => void; wide?: boolean }) {
  return (
    <tr onClick={() => open({ kind: "act", id: row.id })} className="cursor-pointer border-t border-card-divider hover:bg-muted-hover">
      <td className="whitespace-nowrap px-3 py-3">{row.date}</td>
      <td className="px-3">{row.category}<br />{row.action}</td>
      <td className="max-w-md px-3">{row.summary || "没有内容说明"}</td>
      {wide ? <td className="max-w-xs break-all px-3 text-primary">{row.url ? shortUrl(row.url) : row.company || "—"}</td> : null}
      {wide ? <td className="px-3">{row.indexStatus || "—"}</td> : null}
      <td className="px-3"><span className="rounded-full bg-primary/10 px-2 py-0.5 text-xs text-primary">{levelName(row.level)}</span></td>
    </tr>
  )
}

function Drawer({ data, detail, onClose, open }: { data: Dashboard; detail: NonNullable<Detail>; onClose: () => void; open: (detail: Detail) => void }) {
  const body = drawerBody(data, detail, open)
  return (
    <>
      <button type="button" aria-label="关闭" className="fixed inset-0 z-30 bg-foreground/30" onClick={onClose} />
      <aside className="fixed inset-y-0 end-0 z-40 w-full max-w-xl overflow-auto border-s border-overlay-line bg-overlay p-6 shadow-xl">
        <button type="button" onClick={onClose} className="absolute end-4 top-4 rounded-lg border border-layer-line bg-layer px-3 py-1 text-sm">关闭</button>
        {body}
      </aside>
    </>
  )
}

function drawerBody(data: Dashboard, detail: NonNullable<Detail>, open: (detail: Detail) => void) {
  if (detail.kind === "inq") {
    const row = data.inquiries.items.find((item) => item.id === detail.id)
    return row ? <InquiryDetail row={row} /> : <p>找不到这笔申请</p>
  }
  if (detail.kind === "act") {
    const row = data.actions.find((item) => item.id === detail.id)
    return row ? <ActionDetail row={row} /> : <p>找不到这次动作</p>
  }
  if (detail.kind === "page") {
    const row = data.pages.find((item) => item.url === detail.id)
    return row ? <PageDetail row={row} /> : <p>找不到这个网址</p>
  }
  if (detail.kind === "mail") {
    const row = data.mail.events.find((item) => mailKey(item) === detail.id)
    return row ? <MailDetail row={row} /> : <p>找不到这件邮件事件</p>
  }
  const rows = detail.kind === "day-act"
    ? data.actions.filter((row) => row.date === detail.id)
    : data.inquiries.items.filter((row) => row.created.slice(0, 10) === detail.id)
  return (
    <div>
      <h2 className="mb-4 text-xl font-semibold">{detail.id}</h2>
      <table className="w-full text-sm">{rows.map((row) => "action" in row ? <tr key={row.id} onClick={() => open({ kind: "act", id: row.id })} className="cursor-pointer border-t border-card-divider"><td className="py-2">{row.action}</td><td>{row.summary}</td></tr> : <tr key={(row as Inquiry).id} onClick={() => open({ kind: "inq", id: (row as Inquiry).id })} className="cursor-pointer border-t border-card-divider"><td className="py-2">{(row as Inquiry).number}</td><td>{(row as Inquiry).company}</td><td>{askOf(row as Inquiry)}</td></tr>)}</table>
    </div>
  )
}

function shortStatus(label: string) {
  return label.replace("Google 还不知道这个网址", "还不知道").replace("已抓取、尚未收录", "已抓未收").replace("已发现、尚未抓取", "已发现").replace("被 noindex 挡住", "noindex")
}

function MailDetail({ row }: { row: MailEvent }) {
  const fields = [
    ["日期", row.date],
    ["登记编号", row.id],
    ["公司", row.company],
    ["事件", row.event],
    ["级别", row.level],
    ["退信码", row.bounce],
    ["回复分类", row.replyClass],
    ["回信编号", row.replyId],
    ["备注", row.note],
    ["写入时刻", row.writtenAt],
  ]
  return (
    <div>
      <h2 className="mb-1 text-xl font-semibold">{row.event || "邮件事件"}</h2>
      <p className="mb-4 text-sm text-muted-foreground-1">{row.company || row.id}</p>
      <dl className="grid gap-3">{fields.filter(([, value]) => value).map(([label, value]) => <div key={label}><dt className="text-xs text-muted-foreground-1">{label}</dt><dd className="break-all text-sm">{value}</dd></div>)}</dl>
    </div>
  )
}
