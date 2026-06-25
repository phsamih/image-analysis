import React from "react";
export default function ResultActions({ imageUrl, overlayUrl, maskUrl, geotiffMaskUrl }) {
  if (!overlayUrl) return null;
  const items = [
    ["Original Image", imageUrl, "bg-slate-800"],
    ["Overlay PNG", overlayUrl, "bg-cyan-600"],
    ["Mask PNG", maskUrl, "bg-emerald-600"],
    ["Mask GeoTIFF", geotiffMaskUrl, "bg-violet-600"],
  ].filter((x)=>x[1]);
  return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5"><h3 className="text-white font-bold mb-4">Downloads</h3><div className="flex flex-wrap gap-3">{items.map(([label,href,cls])=><a key={label} href={href} target="_blank" rel="noreferrer" className={`px-4 py-2 rounded-xl ${cls} text-white`}>{label}</a>)}</div></div>;
}
