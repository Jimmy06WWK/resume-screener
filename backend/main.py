# backend/main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import asyncio

from backend.services.ranking_service import rank_candidates
from backend.utils.database import init_db, save_history, get_all_history
from backend.routes import employees_router, candidates_router, dashboard_router

app = FastAPI(title="AI Resume Screener & HR Management API")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

app.include_router(employees_router, prefix="/api", tags=["Employees"])
app.include_router(candidates_router, prefix="/api", tags=["Candidates"])
app.include_router(dashboard_router, prefix="/api", tags=["Dashboard"])

init_db()

@app.get("/")
async def health_check():
    return {"status": "online", "message": "AI Resume Screener & HR API is running with Ollama"}

@app.post("/screen")
async def screen(
    jd_text: str = Form(...), 
    output_lang: str = Form("Thai"), 
    resumes: List[UploadFile] = File(...)
):
    results = await asyncio.to_thread(rank_candidates, resumes, jd_text, output_lang)
    if results:
        save_history(jd_text, results)
    return results

@app.get("/health/ollama")
async def ollama_health():
    from backend.services.ai_service import check_ollama_health
    return {"ollama_available": check_ollama_health()}

@app.get("/history")
async def get_history():
    return get_all_history()