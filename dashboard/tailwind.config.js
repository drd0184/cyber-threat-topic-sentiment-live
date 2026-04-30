export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        cyber: {
          bg: "#050912",
          panel: "#0b1220",
          panel2: "#111827",
          line: "rgba(148, 163, 184, 0.22)",
          cyan: "#22d3ee",
          blue: "#60a5fa",
          red: "#ef4444",
          green: "#34d399",
          muted: "#94a3b8",
        },
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "Segoe UI", "Arial", "sans-serif"],
        mono: ["ui-monospace", "SFMono-Regular", "Menlo", "Consolas", "monospace"],
      },
    },
  },
  plugins: [],
};
