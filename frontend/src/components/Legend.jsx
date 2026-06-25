import React from "react";
const ITEMS = [
  { name: "Built-up", color: "#dc143c" }, { name: "Agriculture", color: "#228b22" },
  { name: "Bare Land", color: "#d2b48c" }, { name: "Roads", color: "#ffd700" }, { name: "Water", color: "#1e90ff" }
];
export default function Legend(){return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5"><h3 className="text-white font-bold mb-4">Legend</h3><div className="space-y-3">{ITEMS.map(i=><div key={i.name} className="flex items-center gap-3"><span className="inline-block w-5 h-5 rounded" style={{backgroundColor:i.color}}/><span className="text-slate-200">{i.name}</span></div>)}</div></div>}
