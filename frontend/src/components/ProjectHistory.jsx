import React from "react";
export default function ProjectHistory({ projects }) {
  return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5"><h3 className="text-white font-bold mb-4">Analysis History</h3><div className="space-y-3 max-h-72 overflow-auto">{projects?.length ? projects.map(p=><div key={p.project_id} className="rounded-xl bg-slate-800 p-3"><div className="text-white font-semibold">{p.filename}</div><div className="text-slate-400 text-xs">{p.project_id}</div></div>) : <div className="text-slate-400 text-sm">No history yet</div>}</div></div>;
}
