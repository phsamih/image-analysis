import uuid
from pathlib import Path
from fastapi import UploadFile
from app.config import UPLOAD_DIR, ALLOWED_EXTENSIONS

def validate_extension(filename: str):
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")

def save_upload(file: UploadFile) -> Path:
    validate_extension(file.filename)
    ext = Path(file.filename).suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    file_path = UPLOAD_DIR / unique_name
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
