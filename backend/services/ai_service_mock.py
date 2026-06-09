# backend/services/ai_service_mock.py
from typing import Dict, Any

def analyze_resume_with_ai(job_description: str, resume_text: str, candidate_name: str, language: str = "English") -> Dict[str, Any]:
    """Mock AI analysis for testing when Ollama is not available"""
    
    # Simple keyword matching for demo
    keywords = ["python", "javascript", "react", "node", "sql", "aws", "docker", "git"]
    resume_lower = resume_text.lower()
    
    matched = [k for k in keywords if k in resume_lower]
    missing = [k for k in keywords if k not in resume_lower][:5]
    
    score = min(100, len(matched) * 15)
    
    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "strengths": ["Good technical foundation" if matched else "Willing to learn"],
        "concerns": ["Limited experience" if not matched else "Could improve on missing skills"]
    }

def check_ollama_health() -> bool:
    return False