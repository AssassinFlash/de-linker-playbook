import { useEffect, useRef } from "react"
import ApexCharts from "apexcharts"

const PALETTE = ["#2563eb", "#38bdf8", "#6366f1", "#94a3b8", "#10b981", "#f59e0b", "#f97316"]

type Point = { label: string; full?: string; value: number }

export function BarChart({ points, onPick, height = 280 }: { points: Point[]; onPick?: (index: number) => void; height?: number }) {
  return <ApexBox height={height} options={barOptions(points, onPick)} />
}

export function LineChart({ categories, series, height = 280 }: { categories: string[]; series: { name: string; data: number[] }[]; height?: number }) {
  return <ApexBox height={height} options={lineOptions(categories, series)} />
}

export function DonutChart({ slices, center }: { slices: { label: string; value: number }[]; center: string }) {
  return <ApexBox height={260} options={donutOptions(slices, center)} />
}

function ApexBox({ options, height }: { options: ApexCharts.ApexOptions; height: number }) {
  const ref = useRef<HTMLDivElement>(null)
  const key = JSON.stringify(options.series) + JSON.stringify(options.labels)
  useEffect(() => {
    if (!ref.current) return
    const chart = new ApexCharts(ref.current, { ...options, chart: { ...options.chart, height } })
    void chart.render()
    return () => { chart.destroy() }
    // Rebuild when the plotted data changes.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [key, height])
  return <div ref={ref} />
}

function base(type: "bar" | "line" | "donut"): ApexCharts.ApexOptions {
  return {
    chart: { type, toolbar: { show: false }, fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif", animations: { enabled: false } },
    colors: PALETTE,
    dataLabels: { enabled: false },
    grid: { strokeDashArray: 3, borderColor: "#e7e8ec" },
    legend: { fontSize: "12px", labels: { colors: "#6b7280" } },
    tooltip: { enabled: true, theme: "light" },
    stroke: { width: type === "line" ? 2.5 : 0, curve: "straight" },
  }
}

function barOptions(points: Point[], onPick?: (index: number) => void): ApexCharts.ApexOptions {
  const many = points.length > 8
  return {
    ...base("bar"),
    series: [{ name: "数量", data: points.map((point) => point.value) }],
    chart: { ...base("bar").chart, type: "bar", events: onPick ? { dataPointSelection: (_e, _c, cfg) => onPick(cfg?.dataPointIndex ?? -1) } : {} },
    plotOptions: { bar: { borderRadius: 4, columnWidth: points.length > 16 ? "70%" : "46%" } },
    xaxis: {
      categories: points.map((point) => point.full || point.label),
      labels: { rotate: many ? -40 : 0, hideOverlappingLabels: true, style: { fontSize: "11px", colors: "#6b7280" } },
      axisBorder: { show: false },
      axisTicks: { show: false },
    },
    yaxis: { labels: { style: { fontSize: "11px", colors: "#9ca3af" } } },
    tooltip: { enabled: true },
  }
}

function lineOptions(categories: string[], series: { name: string; data: number[] }[]): ApexCharts.ApexOptions {
  return {
    ...base("line"),
    series,
    markers: { size: 4, strokeWidth: 2, hover: { size: 6 } },
    xaxis: {
      categories,
      tickAmount: Math.min(6, categories.length),
      labels: { rotate: -40, rotateAlways: categories.length > 6, hideOverlappingLabels: true, style: { fontSize: "11px", colors: "#6b7280" } },
      axisBorder: { show: false },
      axisTicks: { show: false },
      tooltip: { enabled: false },
    },
    yaxis: { labels: { style: { fontSize: "11px", colors: "#9ca3af" } } },
    tooltip: { enabled: true, shared: true, intersect: false },
  }
}

function donutOptions(slices: { label: string; value: number }[], center: string): ApexCharts.ApexOptions {
  return {
    ...base("donut"),
    series: slices.map((slice) => slice.value),
    labels: slices.map((slice) => slice.label),
    plotOptions: { pie: { donut: { size: "68%", labels: { show: true, total: { show: true, label: "合计", formatter: () => center }, value: { fontSize: "22px", fontWeight: 650 } } } } },
    legend: { position: "right", fontSize: "13px" },
    tooltip: { enabled: true },
  }
}
