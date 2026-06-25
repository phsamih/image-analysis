import numpy as np
from app.config import CLASS_MAP

def compute_stats(mask: np.ndarray, pixel_area_m2: float):
    total_pixels = mask.size
    stats = []
    for class_id, meta in CLASS_MAP.items():
        if class_id == 0:
            continue
        count = int((mask == class_id).sum())
        pct = (count / total_pixels * 100) if total_pixels else 0
        area_m2 = count * pixel_area_m2
        stats.append({
            "class_id": class_id,
            "class_name": meta["name"],
            "pixel_count": count,
            "percentage": round(pct, 3),
            "area_m2": round(area_m2, 3),
            "area_hectare": round(area_m2 / 10000.0, 6),
            "area_km2": round(area_m2 / 1_000_000.0, 6),
        })
    return stats
