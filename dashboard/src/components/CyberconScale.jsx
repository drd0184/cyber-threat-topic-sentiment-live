const levels = [
  { level: 1, name: "Critical", color: "#EF4444" },
  { level: 2, name: "High", color: "#F97316" },
  { level: 3, name: "Elevated", color: "#EAB308" },
  { level: 4, name: "Monitoring", color: "#84CC16" },
  { level: 5, name: "Nominal", color: "#22C55E" },
];

export function CyberconScale({ level }) {
  return (
    <div className="rounded-lg border border-slate-800 bg-slate-950/55 p-4">
      <div className="mb-3 flex items-center justify-between gap-3">
        <div>
          <div className="font-mono text-xs font-bold uppercase tracking-[0.16em] text-cyan-300">CYBERCON</div>
          <h3 className="mt-1 text-lg font-semibold text-slate-50">Scala di attenzione</h3>
        </div>
        <span className="rounded border border-cyan-300/30 bg-cyan-500/10 px-2 py-1 font-mono text-xs font-bold text-cyan-100">
          Livello {level}
        </span>
      </div>

      <div className="grid grid-cols-1 gap-2 sm:grid-cols-5">
        {levels.map((item) => {
          const active = item.level === Number(level);
          return (
            <div
              key={item.level}
              className={`relative rounded-lg border p-3 transition ${
                active ? "bg-slate-900/85 text-slate-50 shadow-lg" : "border-slate-800 bg-slate-900/30 text-slate-400"
              }`}
              style={{
                borderColor: active ? item.color : undefined,
                boxShadow: active ? `0 0 24px ${item.color}33` : undefined,
                background: active ? `linear-gradient(180deg, ${item.color}1f, rgba(15,23,42,0.88))` : undefined,
              }}
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <div className="font-mono text-[10px] font-bold uppercase tracking-[0.14em] text-slate-500">CYBERCON</div>
                  <div className="mt-1 font-mono text-4xl font-bold leading-none" style={{ color: active ? item.color : "#94A3B8" }}>
                    {item.level}
                  </div>
                </div>
                {active ? (
                  <span className="rounded border px-2 py-1 font-mono text-[10px] font-bold uppercase tracking-[0.08em]" style={{ borderColor: `${item.color}66`, color: item.color }}>
                    ATTUALE
                  </span>
                ) : null}
              </div>
              <div className={`mt-3 text-sm font-semibold ${active ? "text-slate-50" : "text-slate-400"}`}>{item.name}</div>
              <div className="mt-3 h-1.5 rounded-full" style={{ backgroundColor: active ? item.color : `${item.color}55` }} />
            </div>
          );
        })}
      </div>
    </div>
  );
}
