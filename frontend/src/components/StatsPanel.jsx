import React from "react";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";
const colorMap = {"Built-up":"#dc143c","Agriculture":"#228b22","Bare Land":"#d2b48c","Roads":"#ffd700","Water":"#1e90ff"};
export default function StatsPanel({ stats }) {
  if (!stats?.length) return null;
  return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5"><h3 className="text-white font-bold mb-4">Land Cover Statistics</h3><div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">{stats.map(s=><div key={s.class_id} className="rounded-xl bg-slate-800 p-4"><div className="text-white font-semibold">{s.class_name}</div><div className="text-slate-300 text-sm mt-2">Pixels: {s.pixel_count}</div><div className="text-slate-300 text-sm">Percent: {s.percentage}%</div><div className="text-slate-300 text-sm">Area (m²): {s.area_m2}</div><div className="text-slate-300 text-sm">Area (ha): {s.area_hectare}</div><div className="text-slate-300 text-sm">Area (km²): {s.area_km2}</div></div>)}</div><div className="h-72"><ResponsiveContainer width="100%" height="100%"><PieChart><Pie data={stats} dataKey="percentage" nameKey="class_name" cx="50%" cy="50%" outerRadius={100} label>{stats.map(entry=><Cell key={entry.class_id} fill={colorMap[entry.class_name] || "#8884d8"} />)}</Pie><Tooltip /></PieChart></ResponsiveContainer></div></div>;
}
