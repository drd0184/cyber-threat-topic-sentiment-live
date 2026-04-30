import { useMemo, useState } from "react";
import { Tags } from "lucide-react";
import { TopicCard } from "../components/TopicCard.jsx";
import { TopicDetailPanel } from "../components/TopicDetailPanel.jsx";
import { EmptyState, Panel, SearchInput, SectionHeader } from "../components/ui.jsx";

export function TopicExplorer({ data, selectedTopic, setSelectedTopicId, openAlert }) {
  const [query, setQuery] = useState("");
  const [quality, setQuality] = useState("all");
  const [noisy, setNoisy] = useState("all");

  const filteredTopics = useMemo(() => {
    const q = query.trim().toLowerCase();
    return data.topics
      .filter((topic) => quality === "all" || topic.topic_confidence === quality || topic.quality_score === quality)
      .filter((topic) => noisy === "all" || (noisy === "yes" ? topic.is_noisy : !topic.is_noisy))
      .filter((topic) => !q || topic.topic_label.toLowerCase().includes(q) || topic.top_words.join(" ").toLowerCase().includes(q))
      .sort((a, b) => b.max_abs_p2 - a.max_abs_p2 || b.total_volume - a.total_volume);
  }, [data.topics, query, quality, noisy]);

  const topicRows = selectedTopic ? data.p2ByTopic.get(selectedTopic.topic_id) || [] : [];
  const topicPosts = selectedTopic ? data.postsByTopic.get(selectedTopic.topic_id) || [] : [];
  const topicAlerts = [...topicRows].sort((a, b) => b.p2_abs - a.p2_abs);

  return (
    <div className="space-y-6">
      <Panel className="p-5">
        <SectionHeader eyebrow="Topic Explorer" title="Cluster semantici monitorati" description="Esplora i 10 topic LDA live ufficiali, inclusi quelli low-confidence." icon={Tags} />
        <div className="mb-5 grid gap-3 md:grid-cols-[1fr_180px_180px]">
          <SearchInput value={query} onChange={setQuery} placeholder="Cerca topic / top words" />
          <select value={quality} onChange={(event) => setQuality(event.target.value)} className="rounded-lg border border-slate-700 bg-slate-950/75 px-3 py-2 text-sm text-slate-100">
            <option value="all">Tutte le confidenze</option>
            <option value="high">Alta</option>
            <option value="medium">Media</option>
            <option value="low">Bassa</option>
          </select>
          <select value={noisy} onChange={(event) => setNoisy(event.target.value)} className="rounded-lg border border-slate-700 bg-slate-950/75 px-3 py-2 text-sm text-slate-100">
            <option value="all">Tutti i topic</option>
            <option value="yes">Low-confidence</option>
            <option value="no">Non low-confidence</option>
          </select>
        </div>
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {filteredTopics.length ? filteredTopics.map((topic) => <TopicCard key={topic.topic_id} topic={topic} onOpen={setSelectedTopicId} />) : <EmptyState />}
        </div>
      </Panel>
      <TopicDetailPanel topic={selectedTopic} p2Rows={topicRows} posts={topicPosts} alerts={topicAlerts} onInspectAlert={openAlert} />
    </div>
  );
}
