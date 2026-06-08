# backend/routes/dashboard.py
from fastapi import APIRouter
from backend.utils.database import get_dashboard_stats, get_all_employees
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/dashboard/stats")
async def dashboard_stats():
    return get_dashboard_stats()

@router.get("/dashboard/recent-hires")
async def recent_hires():
    employees = get_all_employees("all")
    six_months_ago = (datetime.now() - timedelta(days=180)).isoformat()
    recent = []
    for emp in employees:
        if emp.get('hire_date', '') > six_months_ago:
            recent.append(emp)
    return recent[:10]