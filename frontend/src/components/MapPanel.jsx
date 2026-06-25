import React from "react";
import { MapContainer, ImageOverlay, Rectangle } from "react-leaflet";
import L from "leaflet";
export default function MapPanel({ imageUrl, overlayUrl, bounds }) {
  if (!imageUrl || !overlayUrl) return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 min-h-[420px] flex items-center justify-center text-slate-400">No analysis yet</div>;
  const mapBounds = bounds || [[0,0],[1000,1000]];
  return <div className="bg-slate-900 border border-slate-800 rounded-2xl p-3"><div className="h-[520px] overflow-hidden rounded-xl"><MapContainer bounds={mapBounds} style={{height:"100%", width:"100%"}} crs={bounds ? L.CRS.EPSG3857 : L.CRS.Simple}><ImageOverlay url={imageUrl} bounds={mapBounds} /><ImageOverlay url={overlayUrl} bounds={mapBounds} opacity={0.7} />{!bounds && <Rectangle bounds={mapBounds} pathOptions={{color:"transparent"}} />}</MapContainer></div></div>;
}
