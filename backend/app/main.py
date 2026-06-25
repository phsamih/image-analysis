from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes.analyze import router as analyze_router
from app.config import STATIC_DIR

app = FastAPI(title="Satellite AI Analyzer V2", version="2.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(analyze_router)

@app.get("/")
def root():
    return {"app": "Satellite AI Analyzer V2", "status": "running"}
