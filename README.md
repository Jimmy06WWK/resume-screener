# AI Resume Screener & HR Management System

## Project Title
AI-Powered Resume Screening and HR Management System

## Objective
To automate the resume screening process using AI and provide comprehensive HR management features including employee database, recruitment pipeline, and HR analytics.

## Tools Used
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI Model:** Google Gemini AI (API-based)
- **Database:** SQLite
- **Libraries:** pandas, plotly, pdfplumber, requests

## AI Model Used
- **Model:** Google Gemini 2.0 Flash (via API)
- **Type:** Pre-trained LLM from Google
- **Capabilities:** 
  - Resume text extraction and analysis
  - Skill matching against job descriptions
  - Score calculation (0-100%)
  - Multi-language support (English, Thai, Chinese)

## Features
1. **AI Resume Screener** - Upload PDF resumes and get AI-powered analysis
2. **Employee Database** - CRUD operations for employee management
3. **Recruitment Pipeline** - Kanban-style candidate tracking
4. **HR Dashboard** - Real-time analytics and charts
5. **Multi-language Support** - English, Thai, Chinese

## Installation

### Prerequisites
- Python 3.9+
- pip

### Step 1: Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set up environment variables
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Step 4: Run the application

**Terminal 1 - Backend:**
```bash
uvicorn backend.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
streamlit run frontend/app.py
```

### Step 5: Open browser
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000

## How to Use

### 1. AI Resume Screener
- Paste job description in the text area
- Upload PDF resumes (multiple files allowed)
- Click "Start Analysis"
- View ranked candidates with match scores
- See matched skills, missing skills, strengths, and concerns

### 2. Employee Database
- View all employees in a list
- Add new employees with complete information
- Search and filter by status
- View statistics and department charts

### 3. Recruitment Pipeline
- Track candidates through 6 stages: New → Screening → Interview → Offer → Hired → Rejected
- Drag-and-drop style via "Move to" buttons
- Add new candidates manually
- View upcoming interviews

### 4. HR Dashboard
- View key metrics (total employees, turnover rate, open positions)
- See employee distribution by department (pie chart)
- Monitor candidate pipeline (bar chart)
- View recent hires and alerts

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/screen` | Analyze resumes |
| GET | `/api/employees` | Get all employees |
| POST | `/api/employees` | Add new employee |
| GET | `/api/employees/{id}` | Get employee by ID |
| PUT | `/api/employees/{id}` | Update employee |
| DELETE | `/api/employees/{id}` | Delete employee |
| GET | `/api/candidates` | Get all candidates |
| POST | `/api/candidates` | Add new candidate |
| PUT | `/api/candidates/{id}/status` | Update candidate status |
| GET | `/api/dashboard/stats` | Get dashboard statistics |
| GET | `/api/dashboard/recent-hires` | Get recent hires |

## Project Structure
```
V5/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── employee.py
│   │   └── candidate.py
│   ├── routes/
│   │   ├── employees.py
│   │   ├── candidates.py
│   │   └── dashboard.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── ai_service_mock.py
│   │   └── ranking_service.py
│   └── utils/
│       ├── database.py
│       └── parser.py
├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── 1_Employee_Database.py
│   │   ├── 2_Recruitment_Pipeline.py
│   │   ├── 3_HR_Dashboard.py
│   │   └── 4_Resume_Screener.py
│   ├── components/
│   │   ├── language_manager.py
│   │   └── ui_parts.py
│   └── assets/
│       └── style.css
├── requirements.txt
├── .env
└── README.md
```

## Demo Data
The system comes with pre-loaded test data:
- **8 employees** across Engineering, HR, Sales, Marketing, Finance, Operations
- **8 candidates** in various pipeline stages (New, Screening, Interview, Offer, Hired, Rejected)

To load test data:
```bash
# Run the backend first, then:
curl -X POST http://localhost:8000/api/employees -H "Content-Type: application/json" -d '{"employee_code": "EMP-001", "first_name": "John", "last_name": "Doe", "department": "Engineering", "position": "Software Engineer", "level": "Senior", "hire_date": "2023-01-15", "email": "john@company.com", "phone": "081-111-1111", "salary": 75000}'
```

## Screenshots

### Streamlit Application Running
![Streamlit App](screenshots/streamlit_app.png)

### Backend API Running
![Backend API](screenshots/backend_api.png)

### Resume Screener Results
![Resume Screener](screenshots/resume_screener.png)

### HR Dashboard
![HR Dashboard](screenshots/hr_dashboard.png)

## Troubleshooting

### Backend connection error
```bash
# Check if backend is running
curl http://localhost:8000/

# Should return: {"status":"online","message":"AI Resume Screener & HR API is running"}
```

### Gemini API quota exceeded
The system has a Mock AI fallback mode. To enable:
```bash
# Use mock AI (no API key needed)
sed -i '' 's/from backend.services.ai_service import/from backend.services.ai_service_mock import/' backend/services/ranking_service.py
```

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 8501
lsof -ti:8501 | xargs kill -9
```

### PDF text extraction issues
```bash
# Install additional PDF support
pip install pdfplumber pypdf2
```

## Future Enhancements
- User authentication and roles (Admin, HR, Manager)
- Email notifications for interview scheduling
- Export reports to Excel/PDF
- Integration with calendar systems
- Advanced analytics and predictions

## Author
Wachaira 
Wa

## License
MIT

## Acknowledgments
- Google Gemini AI for providing the LLM API
- Streamlit for the amazing frontend framework
- FastAPI for the backend framework
``

