from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas import AnalyzeResponse
from app.config import CLASS_MAP, RESULTS_DIR
from app.services.storage import save_upload
from app.services.raster_utils import load_image
from app.services.segmentation import segmenter
from app.services.stats import compute_stats
from app.services.export_utils import colorize_mask, create_overlay, save_png, save_json, save_mask_geotiff
from app.services.projects import create_project, list_projects

router = APIRouter(prefix="/api", tags=["analysis"])

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_image(file: UploadFile = File(...)):
    try:
        upload_path = save_upload(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    image_rgb, meta = load_image(upload_path)
    mask = segmenter.predict(image_rgb)
    color_mask = colorize_mask(mask)
    overlay = create_overlay(image_rgb, color_mask)

    stem = upload_path.stem
    image_png_path = RESULTS_DIR / f"{stem}_image.png"
    mask_png_path = RESULTS_DIR / f"{stem}_mask.png"
    overlay_png_path = RESULTS_DIR / f"{stem}_overlay.png"
    stats_json_path = RESULTS_DIR / f"{stem}_stats.json"
    geotiff_mask_path = RESULTS_DIR / f"{stem}_mask.tif"

    save_png(image_rgb, image_png_path)
    save_png(color_mask, mask_png_path)
    save_png(overlay, overlay_png_path)
    save_mask_geotiff(mask, geotiff_mask_path, meta)

    stats = compute_stats(mask, meta["pixel_area_m2"])
    payload = {
        "filename": file.filename,
        "width": meta["width"],
        "height": meta["height"],
        "pixel_area_m2": meta["pixel_area_m2"],
        "image_url": f"/static/results/{image_png_path.name}",
        "overlay_url": f"/static/results/{overlay_png_path.name}",
        "mask_url": f"/static/results/{mask_png_path.name}",
        "geotiff_mask_url": f"/static/results/{geotiff_mask_path.name}",
        "stats": stats,
        "class_map": CLASS_MAP,
        "bounds": meta["bounds"],
        "crs": meta["crs"],
    }
    project_id = create_project(payload.copy())
    payload["project_id"] = project_id
    save_json(payload, stats_json_path)
    return payload

@router.get("/projects")
async def get_projects():
    return list_projects()
