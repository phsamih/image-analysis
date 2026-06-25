from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

UPLOAD_DIR = BASE_DIR / "uploads"
STATIC_DIR = BASE_DIR / "static"
RESULTS_DIR = STATIC_DIR / "results"
PROJECTS_DIR = BASE_DIR / "projects"
MODELS_DIR = BASE_DIR / "models"

for d in [UPLOAD_DIR, STATIC_DIR, RESULTS_DIR, PROJECTS_DIR, MODELS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}

CLASS_MAP = {
    0: {"name": "Background", "color": [0, 0, 0]},
    1: {"name": "Built-up", "color": [220, 20, 60]},
    2: {"name": "Agriculture", "color": [34, 139, 34]},
    3: {"name": "Bare Land", "color": [210, 180, 140]},
    4: {"name": "Roads", "color": [255, 215, 0]},
    5: {"name": "Water", "color": [30, 144, 255]},
}
