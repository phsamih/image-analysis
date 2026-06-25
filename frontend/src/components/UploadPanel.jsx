import React, { useState } from "react";
export default function UploadPanel({ onAnalyze, loading }) {
  const [file, setFile] = useState(null);
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl">
      <h2 className="text-xl font-bold text-white mb-3">Upload Satellite Image</h2>
      <p className="text-slate-400 text-sm mb-4">PNG / JPG / TIFF / GeoTIFF</p>
      <input type="file" accept=".png,.jpg,.jpeg,.tif,.tiff" onChange={(e)=>setFile(e.target.files?.[0]||null)} className="block w-full text-sm text-slate-300 mb-4" />
      {file && <div className="text-sm text-slate-300 mb-4">Selected: <span className="font-semibold">{file.name}</span></div>}
      <button onClick={()=>file && onAnalyze(file)} disabled={!file || loading} className="w-full rounded-xl bg-cyan-500 hover:bg-cyan-400 disabled:opacity-50 text-slate-950 font-semibold py-3">{loading ? "Analyzing..." : "Analyze Image"}</button>
    </div>
  );
}
