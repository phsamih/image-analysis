import json, uuid
from pathlib import Path
from datetime import datetime
from app.config import PROJECTS_DIR

def create_project(payload: dict) -> str:
    project_id = uuid.uuid4().hex
    payload["project_id"] = project_id
    payload["created_at"] = datetime.utcnow().isoformat()
    project_dir = PROJECTS_DIR / project_id
    project_dir.mkdir(parents=True, exist_ok=True)
    with open(project_dir / "project.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return project_id

def list_projects():
    projects = []
    for p in PROJECTS_DIR.iterdir():
        if p.is_dir() and (p / "project.json").exists():
            with open(p / "project.json", "r", encoding="utf-8") as f:
                projects.append(json.load(f))
    projects.sort(key=lambda x: x.get("created_at",""), reverse=True)
    return projects
