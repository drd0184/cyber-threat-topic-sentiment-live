import {
  BookOpen,
  Database,
  LayoutDashboard,
  RadioTower,
  ShieldCheck,
  Siren,
  Tags,
} from "lucide-react";

const navItems = [
  { id: "overview", label: "Panoramica", subtitle: "Sintesi operativa", icon: LayoutDashboard },
  { id: "alerts", label: "Allarmi", subtitle: "Alert P2", icon: Siren },
  { id: "topics", label: "Esplora Topic", subtitle: "Cluster LDA", icon: Tags },
  { id: "quality", label: "Qualità e affidabilità", subtitle: "Controlli ex post", icon: ShieldCheck },
  { id: "methodology", label: "Metodologia", subtitle: "Pipeline NLP", icon: BookOpen },
  { id: "data", label: "Console dati", subtitle: "Record e artifact", icon: Database },
];

export function AppShell({ activeView, setActiveView, children }) {
  const active = navItems.find((item) => item.id === activeView) || navItems[0];
  return (
    <div className="min-h-screen bg-[#05070B] text-slate-100">
      <div className="lg:flex">
        <Sidebar activeView={activeView} setActiveView={setActiveView} />
        <main className="min-w-0 flex-1 lg:ml-72">
          <Header title={active.label} subtitle={active.subtitle} />
          <div className="mx-auto max-w-[1480px] px-4 py-5 sm:px-6 xl:px-8">{children}</div>
          <footer className="mx-auto max-w-[1480px] px-4 pb-8 pt-2 text-xs leading-6 text-slate-500 sm:px-6 xl:px-8">
            Demo locale per finalità didattiche. P2 misura momentum semantico, non incidenti verificati.
          </footer>
        </main>
      </div>
    </div>
  );
}

function Sidebar({ activeView, setActiveView }) {
  return (
    <aside className="border-b border-slate-800 bg-slate-950/95 p-4 backdrop-blur-xl lg:fixed lg:inset-y-0 lg:left-0 lg:z-30 lg:w-72 lg:border-b-0 lg:border-r">
      <div className="flex items-center gap-3">
        <div className="grid h-11 w-11 place-items-center rounded-lg border border-cyan-300/25 bg-cyan-400/10">
          <RadioTower className="h-5 w-5 text-cyan-200" />
        </div>
        <div className="min-w-0">
          <div className="text-sm font-semibold uppercase tracking-[0.08em] text-slate-50">Hot Topic Index</div>
          <div className="text-xs text-slate-500">Cyber Threat Intelligence</div>
        </div>
      </div>

      <nav className="mt-7 grid grid-cols-2 gap-2 lg:grid-cols-1">
        {navItems.map((item) => {
          const Icon = item.icon;
          const active = item.id === activeView;
          return (
            <button
              key={item.id}
              type="button"
              onClick={() => setActiveView(item.id)}
              className={`group flex items-center gap-3 rounded-lg border px-3 py-3 text-left text-sm transition ${
                active
                  ? "border-cyan-300/40 bg-cyan-400/10 text-cyan-50"
                  : "border-slate-800 bg-slate-900/30 text-slate-400 hover:border-slate-600 hover:text-slate-100"
              }`}
            >
              <Icon className="h-4 w-4 shrink-0" />
              <span className="min-w-0">
                <span className="block truncate font-medium">{item.label}</span>
                <span className="mt-0.5 hidden truncate text-xs text-slate-500 lg:block">{item.subtitle}</span>
              </span>
            </button>
          );
        })}
      </nav>
    </aside>
  );
}

function Header({ title, subtitle }) {
  return (
    <header className="sticky top-0 z-20 border-b border-slate-800/90 bg-[#05070B]/88 px-4 py-3 backdrop-blur-xl sm:px-6 xl:px-8">
      <div className="mx-auto flex max-w-[1480px] items-center justify-between gap-4">
        <div className="min-w-0">
          <h1 className="truncate text-base font-semibold text-slate-50">{title}</h1>
          <p className="truncate text-sm text-slate-500">{subtitle}</p>
        </div>
      </div>
    </header>
  );
}
