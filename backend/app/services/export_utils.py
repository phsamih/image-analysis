from pathlib import Path
import json
import numpy as np
from PIL import Image
import rasterio
from rasterio.transform import from_origin
from app.config import CLASS_MAP

def colorize_mask(mask: np.ndarray) -> np.ndarray:
    out = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    for cid, meta in CLASS_MAP.items():
        out[mask == cid] = meta["color"]
    return out

def create_overlay(image_rgb: np.ndarray, color_mask: np.ndarray, alpha: float = 0.45) -> np.ndarray:
    return (image_rgb * (1 - alpha) + color_mask * alpha).clip(0,255).astype(np.uint8)

def save_png(np_img: np.ndarray, path: Path):
    Image.fromarray(np_img).save(path)

def save_json(data: dict, path: Path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_mask_geotiff(mask: np.ndarray, path: Path, meta: dict):
    h, w = mask.shape
    transform = meta.get("transform") or from_origin(0, h, 1, 1)
    with rasterio.open(
        path, "w", driver="GTiff", height=h, width=w, count=1,
        dtype=mask.dtype, crs=meta.get("crs"), transform=transform
    ) as dst:
        dst.write(mask, 1)
