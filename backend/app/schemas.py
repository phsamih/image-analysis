from pydantic import BaseModel
from typing import Dict, List, Optional

class ClassStat(BaseModel):
    class_id: int
    class_name: str
    pixel_count: int
    percentage: float
    area_m2: float
    area_hectare: float
    area_km2: float

class AnalyzeResponse(BaseModel):
    filename: str
    width: int
    height: int
    pixel_area_m2: float
    image_url: str
    overlay_url: str
    mask_url: str
    geotiff_mask_url: Optional[str] = None
    stats: List[ClassStat]
    class_map: Dict[int, Dict]
    bounds: Optional[list] = None
    crs: Optional[str] = None
    project_id: Optional[str] = None
