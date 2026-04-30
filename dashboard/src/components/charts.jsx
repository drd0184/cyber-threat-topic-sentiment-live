import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  Line,
  LineChart,
  Legend,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { formatDate, formatNumber, formatP2 } from "../utils/formatters.js";

const grid = "rgba(148, 163, 184, 0.13)";
const tick = "#94A3B8";
const topicColors = ["#22D3EE", "#3B82F6", "#06B6D4", "#A78BFA", "#EF4444", "#F59E0B", "#FB7185", "#64748B", "#22C55E", "#14B8A6"];

export function P2OverviewChart({ p2, topTopicIds, topics }) {
  const windows = [...new Set(p2.map((row) => row.time_window))].sort();
  const data = windows.map((window) => {
    const point = { time_window: window, label: formatDate(window, true) };
    for (const topicId of topTopicIds) {
      const match = p2.find((row) => row.time_window === window && row.dominant_topic === topicId);
      point[`topic_${topicId}`] = match?.p2_index ?? null;
    }
    return point;
  });
  return (
    <ResponsiveContainer width="100%" height="100%">
      <LineChart data={data}>
        <CartesianGrid stroke={grid} vertical={false} />
        <XAxis dataKey="label" stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <YAxis stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <Tooltip contentStyle={{ background: "#0B1120", border: "1px solid #1F2937", borderRadius: 8 }} />
        {topTopicIds.map((topicId, index) => {
          const topic = topics.find((item) => item.topic_id === topicId);
          return (
            <Line
              key={topicId}
              type="monotone"
              dataKey={`topic_${topicId}`}
              name={`T${topicId} ${topic?.topic_label || ""}`}
              stroke={topicColors[index % topicColors.length]}
              strokeWidth={2}
              dot={{ r: 3 }}
              connectNulls
            />
          );
        })}
      </LineChart>
    </ResponsiveContainer>
  );
}

export function MiniTimeline({ p2, onSelectAlert }) {
  const windows = [...new Set(p2.map((row) => row.time_window))].sort();
  const data = windows.map((window) => {
    const rows = p2.filter((row) => row.time_window === window);
    const strongest = [...rows].sort((a, b) => b.p2_abs - a.p2_abs)[0];
    return { window, strongest };
  });
  return (
    <div className="flex gap-1 overflow-x-auto pb-1">
      {data.map(({ window, strongest }) => {
        const height = Math.min(54, Math.max(12, strongest.p2_abs * 1.7));
        const color = strongest.p2_direction === "negative" ? "bg-red-400" : strongest.p2_direction === "positive" ? "bg-green-400" : "bg-cyan-300";
        return (
          <button
            key={window}
            type="button"
            title={`${formatDate(window)} | ${strongest.topic_label} | P2 ${strongest.p2_index.toFixed(2)}`}
            onClick={() => onSelectAlert(strongest)}
            className="flex h-16 w-5 shrink-0 items-end justify-center rounded border border-slate-800 bg-slate-950/60 px-0.5"
          >
            <span className={`w-full rounded-sm ${color}`} style={{ height }} />
          </button>
        );
      })}
    </div>
  );
}

export function P2TrendChart({ trend = [] }) {
  const data = trend.map((row) => ({
    ...row,
    label: formatDate(row.time_window, true),
    signed_abs: row.direction === "negative" ? -Math.abs(row.max_abs_p2) : Math.abs(row.max_abs_p2),
  }));

  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={data} margin={{ top: 8, right: 16, bottom: 0, left: 0 }}>
        <defs>
          <linearGradient id="p2TrendFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#22D3EE" stopOpacity={0.28} />
            <stop offset="100%" stopColor="#22D3EE" stopOpacity={0.03} />
          </linearGradient>
        </defs>
        <CartesianGrid stroke={grid} vertical={false} />
        <XAxis
          dataKey="label"
          stroke={tick}
          fontSize={11}
          tickLine={false}
          axisLine={false}
          minTickGap={34}
          interval="preserveStartEnd"
        />
        <YAxis stroke={tick} fontSize={11} tickLine={false} axisLine={false} width={42} />
        <Tooltip content={<P2TrendTooltip />} />
        <Area
          type="monotone"
          dataKey="signed_abs"
          name="P2 trend"
          stroke="#22D3EE"
          fill="url(#p2TrendFill)"
          strokeWidth={2}
          dot={false}
          activeDot={{ r: 4 }}
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}

function P2TrendTooltip({ active, payload }) {
  if (!active || !payload?.length) return null;
  const row = payload[0].payload;
  return (
    <div className="rounded-lg border border-slate-700 bg-slate-950/95 p-3 text-sm shadow-xl">
      <div className="font-mono text-xs text-slate-500">{formatDate(row.time_window)}</div>
      <div className="mt-1 font-semibold text-slate-100">{row.topic_label}</div>
      <div className="mt-2 grid gap-1 font-mono text-xs text-slate-300">
        <span>P2 {formatP2(row.p2_index, 2)}</span>
        <span>|P2| {formatNumber(row.max_abs_p2, 2)}</span>
        <span>severity {row.severity}</span>
        <span>confidence {row.topic_confidence}</span>
      </div>
    </div>
  );
}

export function TopicLineChart({ rows, dataKey, color = "#22D3EE" }) {
  const data = rows.map((row) => ({ ...row, label: formatDate(row.time_window, true) }));
  return (
    <ResponsiveContainer width="100%" height="100%">
      <LineChart data={data}>
        <CartesianGrid stroke={grid} vertical={false} />
        <XAxis dataKey="label" stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <YAxis stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <Tooltip contentStyle={{ background: "#0B1120", border: "1px solid #1F2937", borderRadius: 8 }} />
        <Line type="monotone" dataKey={dataKey} stroke={color} strokeWidth={2} dot={false} activeDot={{ r: 4 }} />
      </LineChart>
    </ResponsiveContainer>
  );
}

export function TopicBarChart({ rows, dataKey, color = "#3B82F6" }) {
  const data = rows.map((row) => ({ ...row, label: formatDate(row.time_window, true) }));
  return (
    <ResponsiveContainer width="100%" height="100%">
      <BarChart data={data}>
        <CartesianGrid stroke={grid} vertical={false} />
        <XAxis dataKey="label" stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <YAxis stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <Tooltip contentStyle={{ background: "#0B1120", border: "1px solid #1F2937", borderRadius: 8 }} />
        <Bar dataKey={dataKey} fill={color} radius={[4, 4, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
}

export function TopicAreaChart({ rows, dataKey, color = "#22C55E" }) {
  const data = rows.map((row) => ({ ...row, label: formatDate(row.time_window, true) }));
  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={data}>
        <CartesianGrid stroke={grid} vertical={false} />
        <XAxis dataKey="label" stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <YAxis stroke={tick} fontSize={11} tickLine={false} axisLine={false} />
        <Tooltip contentStyle={{ background: "#0B1120", border: "1px solid #1F2937", borderRadius: 8 }} />
        <Area type="monotone" dataKey={dataKey} stroke={color} fill={color} fillOpacity={0.16} strokeWidth={2} />
      </AreaChart>
    </ResponsiveContainer>
  );
}

export function SentimentDistributionChart({ posts }) {
  const normalized = posts.map((post) => {
    if (post.sentiment_class) return post.sentiment_class;
    const value = Number(post.vader_compound || 0);
    if (value <= -0.05) return "negative";
    if (value >= 0.05) return "positive";
    return "neutral";
  });
  const total = normalized.length;
  const counts = ["negative", "neutral", "positive"].map((name) => ({
    name,
    value: normalized.filter((sentiment) => sentiment === name).length,
    percent: total ? normalized.filter((sentiment) => sentiment === name).length / total * 100 : 0,
  }));
  const colors = { negative: "#EF4444", positive: "#22C55E", neutral: "#64748B" };
  const labelMap = { negative: "Negative", neutral: "Neutral", positive: "Positive" };
  return (
    <div className="grid h-full gap-4 md:grid-cols-[minmax(180px,0.9fr)_minmax(180px,1fr)] md:items-center">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie data={counts} dataKey="value" nameKey="name" innerRadius={54} outerRadius={84} paddingAngle={3}>
            {counts.map((entry) => <Cell key={entry.name} fill={colors[entry.name]} />)}
          </Pie>
          <Tooltip
            formatter={(value, name, props) => [`${formatNumber(value)} (${formatNumber(props.payload.percent, 1)}%)`, labelMap[name] || name]}
            contentStyle={{ background: "#0B1120", border: "1px solid #1F2937", borderRadius: 8 }}
          />
          <Legend verticalAlign="bottom" height={24} formatter={(value) => labelMap[value] || value} />
        </PieChart>
      </ResponsiveContainer>
      <div className="space-y-2">
        <div className="rounded border border-slate-800 bg-slate-900/40 p-3">
          <span className="block text-xs uppercase tracking-[0.12em] text-slate-500">Totale post Topic</span>
          <strong className="mt-1 block font-mono text-xl text-slate-100">{formatNumber(total)}</strong>
        </div>
        {counts.map((entry) => (
          <div key={entry.name} className="flex items-center justify-between gap-3 rounded border border-slate-800 bg-slate-900/35 px-3 py-2 text-sm">
            <span className="flex items-center gap-2 text-slate-300">
              <span className="h-2.5 w-2.5 rounded-full" style={{ backgroundColor: colors[entry.name] }} />
              {labelMap[entry.name]}
            </span>
            <span className="font-mono text-slate-100">
              {formatNumber(entry.value)} · {formatNumber(entry.percent, 1)}%
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
