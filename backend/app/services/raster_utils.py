from pathlib import Path
import numpy as np
from PIL import Image
import rasterio

def is_geotiff(path: Path) -> bool:
    return path.suffix.lower() in [".tif", ".tiff"]

def normalize_to_uint8(arr: np.ndarray) -> np.ndarray:
    arr = arr.astype(np.float32)
    minv = arr.min()
    maxv = arr.max()
    if maxv - minv < 1e-6:
        return np.zeros_like(arr, dtype=np.uint8)
    arr = (arr - minv) / (maxv - minv)
    return (arr * 255).clip(0,255).astype(np.uint8)

def load_image(path: Path):
    if is_geotiff(path):
        with rasterio.open(path) as src:
            arr = src.read()
            if arr.shape[0] >= 3:
                rgb = np.stack([arr[0], arr[1], arr[2]], axis=-1)
            else:
                band = arr[0]
                rgb = np.stack([band, band, band], axis=-1)
            rgb = normalize_to_uint8(rgb)
            transform = src.transform
            pixel_width = abs(transform.a)
            pixel_height = abs(transform.e)
            pixel_area_m2 = float(pixel_width * pixel_height) if src.crs and src.crs.is_projected else 1.0
            meta = {
                "width": src.width,
                "height": src.height,
                "crs": str(src.crs) if src.crs else None,
                "bounds": [[src.bounds.bottom, src.bounds.left], [src.bounds.top, src.bounds.right]],
                "pixel_area_m2": pixel_area_m2,
                "transform": transform,
            }
            return rgb, meta
    img = Image.open(path).convert("RGB")
    rgb = np.array(img)
    h, w = rgb.shape[:2]
    return rgb, {"width": w, "height": h, "crs": None, "bounds": None, "pixel_area_m2": 1.0, "transform": None}
