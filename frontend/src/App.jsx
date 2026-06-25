import React, { useEffect, useState } from "react";
import { analyzeImage, fetchProjects, API_BASE } from "./api";
import UploadPanel from "./components/UploadPanel";
import MapPanel from "./components/MapPanel";
import StatsPanel from "./components/StatsPanel";
import Legend from "./components/Legend";
import ResultActions from "./components/ResultActions";
import ProjectHistory from "./components/ProjectHistory";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [projects, setProjects] = useState([]);
  const [error, setError] = useState("");

  const loadProjects = async () => {
    try { setProjects(await fetchProjects()); } catch {}
  };
  useEffect(() => { loadProjects(); }, []);

  const handleAnalyze = async (file) => {
    try {
      setLoading(true); setError("");
      const data = await analyzeImage(file);
      setResult({
        ...data,
        image_url: `${API_BASE}${data.image_url}`,
        overlay_url: `${API_BASE}${data.overlay_url}`,
        mask_url: `${API_BASE}${data.mask_url}`,
        geotiff_mask_url: data.geotiff_mask_url ? `${API_BASE}${data.geotiff_mask_url}` : null,
      });
      await loadProjects();
    } catch (err) {
      setError(err?.response?.data?.detail || "Analysis failed.");
    } finally { setLoading(false); }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-7xl mx-auto px-4 py-8">
        <header className="mb-8">
          <h1 className="text-4xl font-black tracking-tight">Satellite AI Analyzer V2</h1>
          <p className="text-slate-400 mt-2">AI-based land-cover segmentation for satellite and drone imagery.</p>
        </header>
        {error && <div className="mb-6 rounded-xl bg-red-500/10 border border-red-500/20 text-red-300 px-4 py-3">{error}</div>}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div className="lg:col-span-4 space-y-6">
            <UploadPanel onAnalyze={handleAnalyze} loading={loading} />
            <Legend />
            <ResultActions imageUrl={result?.image_url} overlayUrl={result?.overlay_url} maskUrl={result?.mask_url} geotiffMaskUrl={result?.geotiff_mask_url} />
            <ProjectHistory projects={projects} />
          </div>
          <div className="lg:col-span-8 space-y-6">
            <MapPanel imageUrl={result?.image_url} overlayUrl={result?.overlay_url} bounds={result?.bounds || null} />
            <StatsPanel stats={result?.stats || []} />
          </div>
        </div>
      </div>
    </div>
  );
}
