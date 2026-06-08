# backend/utils/__init__.py
from .database import init_db, save_history, get_all_history, get_all_employees, get_employee_by_id, create_employee, update_employee, delete_employee, get_all_candidates, create_candidate, update_candidate_status, update_candidate_offer, delete_candidate, get_dashboard_stats
from .parser import extract_text_from_pdf