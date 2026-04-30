import { useMemo, useState } from "react";
import { AppShell } from "./components/AppShell.jsx";
import { Overview } from "./pages/Overview.jsx";
import { Alerts } from "./pages/Alerts.jsx";
import { TopicExplorer } from "./pages/TopicExplorer.jsx";
import { Quality } from "./pages/Quality.jsx";
import { Methodology } from "./pages/Methodology.jsx";
import { DataConsole } from "./pages/DataConsole.jsx";
import { dashboardData } from "./utils/data.js";

export default function App() {
  const [activeView, setActiveView] = useState("overview");
  const [selectedTopicId, setSelectedTopicId] = useState(null);
  const [selectedAlertKey, setSelectedAlertKey] = useState(null);

  const selectedTopic = useMemo(
    () => (selectedTopicId === null ? null : dashboardData.topics.find((topic) => topic.topic_id === selectedTopicId) || null),
    [selectedTopicId]
  );

  const selectedAlert = useMemo(() => {
    if (!selectedAlertKey) return null;
    return dashboardData.alerts.find((row) => `${row.time_window}-${row.dominant_topic}` === selectedAlertKey) || null;
  }, [selectedAlertKey]);

  const openTopic = (topicId) => {
    setSelectedTopicId(topicId);
    setActiveView("topics");
  };

  const openAlert = (alert) => {
    setSelectedAlertKey(`${alert.time_window}-${alert.dominant_topic}`);
    setActiveView("alerts");
  };

  const pageProps = {
    data: dashboardData,
    selectedTopic,
    selectedAlert,
    openTopic,
    openAlert,
    setSelectedTopicId,
    setSelectedAlertKey,
  };

  return (
    <AppShell activeView={activeView} setActiveView={setActiveView} summary={dashboardData.summary}>
      {activeView === "overview" && <Overview {...pageProps} />}
      {activeView === "alerts" && <Alerts {...pageProps} />}
      {activeView === "topics" && <TopicExplorer {...pageProps} />}
      {activeView === "quality" && <Quality {...pageProps} />}
      {activeView === "methodology" && <Methodology />}
      {activeView === "data" && <DataConsole {...pageProps} />}
    </AppShell>
  );
}
