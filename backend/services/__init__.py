# backend/services/__init__.py
from .ai_service import evaluate_resume, check_ollama_health
from .ranking_service import rank_candidates