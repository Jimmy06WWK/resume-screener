import sqlite3
import json
from datetime import datetime

DB_PATH = "history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS scan_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT,
                  jd_summary TEXT,
                  results TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  employee_code TEXT UNIQUE,
                  first_name TEXT,
                  last_name TEXT,
                  thai_name TEXT,
                  department TEXT,
                  position TEXT,
                  level TEXT,
                  hire_date TEXT,
                  birth_date TEXT,
                  email TEXT,
                  phone TEXT,
                  address TEXT,
                  bank_account TEXT,
                  bank_name TEXT,
                  salary REAL,
                  status TEXT DEFAULT 'active',
                  resign_date TEXT,
                  created_at TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS candidates
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT,
                  phone TEXT,
                  position_applied TEXT,
                  status TEXT DEFAULT 'new',
                  score REAL,
                  matched_skills TEXT,
                  missing_skills TEXT,
                  resume_filename TEXT,
                  interview_date TEXT,
                  interview_notes TEXT,
                  offer_sent_date TEXT,
                  offer_accepted INTEGER DEFAULT 0,
                  hired_date TEXT,
                  created_at TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  description TEXT,
                  assignee_id INTEGER,
                  due_date TEXT,
                  status TEXT DEFAULT 'pending',
                  created_at TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS employee_documents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  employee_id INTEGER,
                  document_type TEXT,
                  filename TEXT,
                  file_path TEXT,
                  uploaded_at TEXT)''')
    
    conn.commit()
    conn.close()

def get_all_employees(status="active"):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if status == "all":
        c.execute("SELECT * FROM employees ORDER BY id DESC")
    else:
        c.execute("SELECT * FROM employees WHERE status = ? ORDER BY id DESC", (status,))
    rows = c.fetchall()
    conn.close()
    
    employees = []
    for row in rows:
        employees.append({
            "id": row[0],
            "employee_code": row[1],
            "first_name": row[2],
            "last_name": row[3],
            "thai_name": row[4],
            "department": row[5],
            "position": row[6],
            "level": row[7],
            "hire_date": row[8],
            "birth_date": row[9],
            "email": row[10],
            "phone": row[11],
            "address": row[12],
            "bank_account": row[13],
            "bank_name": row[14],
            "salary": row[15],
            "status": row[16],
            "resign_date": row[17],
            "created_at": row[18]
        })
    return employees

def get_employee_by_id(emp_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "employee_code": row[1],
            "first_name": row[2],
            "last_name": row[3],
            "thai_name": row[4],
            "department": row[5],
            "position": row[6],
            "level": row[7],
            "hire_date": row[8],
            "birth_date": row[9],
            "email": row[10],
            "phone": row[11],
            "address": row[12],
            "bank_account": row[13],
            "bank_name": row[14],
            "salary": row[15],
            "status": row[16],
            "resign_date": row[17],
            "created_at": row[18]
        }
    return None

def create_employee(employee_data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO employees 
                 (employee_code, first_name, last_name, thai_name, department, 
                  position, level, hire_date, birth_date, email, phone, address,
                  bank_account, bank_name, salary, status, created_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (employee_data['employee_code'], employee_data['first_name'], 
               employee_data['last_name'], employee_data.get('thai_name', ''),
               employee_data['department'], employee_data['position'], 
               employee_data['level'], employee_data['hire_date'], 
               employee_data.get('birth_date', ''), employee_data['email'],
               employee_data['phone'], employee_data.get('address', ''),
               employee_data.get('bank_account', ''), employee_data.get('bank_name', ''),
               employee_data.get('salary', 0), 'active', datetime.now().isoformat()))
    conn.commit()
    emp_id = c.lastrowid
    conn.close()
    return emp_id

def update_employee(emp_id, employee_data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''UPDATE employees SET 
                 first_name=?, last_name=?, thai_name=?, department=?, 
                 position=?, level=?, phone=?, address=?, salary=?, status=?
                 WHERE id=?''',
              (employee_data['first_name'], employee_data['last_name'],
               employee_data.get('thai_name', ''), employee_data['department'],
               employee_data['position'], employee_data['level'],
               employee_data['phone'], employee_data.get('address', ''),
               employee_data.get('salary', 0), employee_data['status'], emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

def get_all_candidates(status=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if status:
        c.execute("SELECT * FROM candidates WHERE status = ? ORDER BY id DESC", (status,))
    else:
        c.execute("SELECT * FROM candidates ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    
    candidates = []
    for row in rows:
        candidates.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "position_applied": row[4],
            "status": row[5],
            "score": row[6],
            "matched_skills": json.loads(row[7]) if row[7] else [],
            "missing_skills": json.loads(row[8]) if row[8] else [],
            "resume_filename": row[9],
            "interview_date": row[10],
            "interview_notes": row[11],
            "offer_sent_date": row[12],
            "offer_accepted": bool(row[13]) if row[13] else False,
            "hired_date": row[14],
            "created_at": row[15]
        })
    return candidates

def create_candidate(candidate_data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO candidates 
                 (name, email, phone, position_applied, status, score, 
                  matched_skills, missing_skills, resume_filename, created_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (candidate_data['name'], candidate_data['email'], 
               candidate_data['phone'], candidate_data['position_applied'],
               candidate_data.get('status', 'new'), candidate_data.get('score', 0),
               json.dumps(candidate_data.get('matched_skills', [])),
               json.dumps(candidate_data.get('missing_skills', [])),
               candidate_data.get('resume_filename', ''), datetime.now().isoformat()))
    conn.commit()
    cand_id = c.lastrowid
    conn.close()
    return cand_id

def update_candidate_status(cand_id, status, interview_date=None, interview_notes=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE candidates SET status = ? WHERE id = ?", (status, cand_id))
    if interview_date:
        c.execute("UPDATE candidates SET interview_date = ? WHERE id = ?", (interview_date, cand_id))
    if interview_notes:
        c.execute("UPDATE candidates SET interview_notes = ? WHERE id = ?", (interview_notes, cand_id))
    conn.commit()
    conn.close()

def update_candidate_offer(cand_id, offer_sent_date=None, offer_accepted=None, hired_date=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if offer_sent_date:
        c.execute("UPDATE candidates SET offer_sent_date = ? WHERE id = ?", (offer_sent_date, cand_id))
    if offer_accepted is not None:
        c.execute("UPDATE candidates SET offer_accepted = ? WHERE id = ?", (1 if offer_accepted else 0, cand_id))
    if hired_date:
        c.execute("UPDATE candidates SET hired_date = ? WHERE id = ?", (hired_date, cand_id))
    conn.commit()
    conn.close()

def delete_candidate(cand_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM candidates WHERE id = ?", (cand_id,))
    conn.commit()
    conn.close()

def get_dashboard_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM employees WHERE status = 'active'")
    total_employees = c.fetchone()[0]
    
    c.execute("SELECT department, COUNT(*) FROM employees WHERE status = 'active' GROUP BY department")
    employees_by_dept = dict(c.fetchall())
    
    c.execute("SELECT status, COUNT(*) FROM candidates GROUP BY status")
    candidates_by_status = dict(c.fetchall())
    
    from datetime import datetime, timedelta
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    c.execute("SELECT COUNT(*) FROM candidates WHERE interview_date BETWEEN ? AND ?", (today.isoformat(), next_week.isoformat()))
    upcoming_interviews = c.fetchone()[0]
    
    one_year_ago = (datetime.now() - timedelta(days=365)).isoformat()
    c.execute("SELECT COUNT(*) FROM employees WHERE status = 'resigned' AND resign_date > ?", (one_year_ago,))
    resigned_count = c.fetchone()[0]
    turnover_rate = (resigned_count / total_employees * 100) if total_employees > 0 else 0
    
    conn.close()
    
    return {
        "total_employees": total_employees,
        "employees_by_dept": employees_by_dept,
        "candidates_by_status": candidates_by_status,
        "upcoming_interviews": upcoming_interviews,
        "turnover_rate": round(turnover_rate, 1),
        "resigned_count": resigned_count
    }

def save_history(jd_text, results):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    jd_summary = (jd_text[:100] + '...') if len(jd_text) > 100 else jd_text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO scan_history (timestamp, jd_summary, results) VALUES (?, ?, ?)", 
              (timestamp, jd_summary, json.dumps(results, ensure_ascii=False)))
    conn.commit()
    conn.close()

def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, timestamp, jd_summary, results FROM scan_history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows