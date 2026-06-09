```markdown
# 🏢 AI-Powered HR Management System

An intelligent Human Resource Management System with AI-powered resume screening, employee database management, recruitment pipeline tracking, and real-time HR analytics.

## 🌟 Features

### 1. 🤖 AI Resume Screener
- Upload multiple PDF resumes
- Paste job description
- AI-powered candidate analysis using Ollama LLM
- Automatic scoring (0-100) based on job requirements
- Skill matching detection
- Multi-language support (Thai, English, Chinese)
- Detailed candidate reports with strengths and concerns

### 2. 👥 Employee Database
- Complete employee record management
- Search and filter employees
- Add, edit, delete employee records
- Department-wise statistics
- Status tracking (Active/Resigned)

### 3. 🎯 Recruitment Pipeline
- Kanban-style candidate tracking board
- 6 stages: New → Screening → Interview → Offer → Hired → Rejected
- Drag-and-drop candidate movement
- AI scoring for candidates
- Interview scheduling

### 4. 📊 HR Dashboard
- Real-time analytics
- Total employees and turnover rate
- Department distribution charts
- Candidate pipeline visualization
- Upcoming interviews tracking

### 5. 🌐 Multi-Language Support
- Thai (ภาษาไทย)
- English
- Chinese (中文)

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐  ┌──────────────┐   │
│  │ Landing  │ │Employee  │ │Recruitment│ │   Resume     │   │
│  │  Page    │ │ Database │ │ Pipeline  │ │  Screener    │   │
│  └──────────┘ └──────────┘ └──────────┘  └──────────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTP API
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐     │
│  │  Routes    │  │  Services  │  │     Models         │     │
│  │ - Employees│  │ - AI       │  │ - Employee         │     │
│  │ - Candidates│ │ - Ranking  │  │ - Candidate        │     │
│  │ - Dashboard│  └────────────┘  └────────────────────┘     │
│  └────────────┘         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                        │
│              │   Ollama (LLM)      │                        │
│              │  - qwen2.5:7b       │                        │
│              │  - llama3.2:1b/3b   │                        │
│              └─────────────────────┘                        │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    SQLite Database                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐    │
│  │ employees   │ │ candidates  │ │    scan_history     │    │
│  └─────────────┘ └─────────────┘ └─────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Ollama** (for AI model)
- **8GB+ RAM** (16GB recommended for 7B models)
- **Mac M1/M2/M3** or **Linux** with GPU support (optional)

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/resume-screener.git
cd resume-screener
```

#### 2. Install Ollama (for AI model)

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### 3. Download AI Model
```bash
# Recommended for Thai language support
ollama pull qwen2.5:7b

# Alternative lighter model
ollama pull llama3.2:3b

# Verify installation
ollama list
```

#### 4. Setup Python Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 5. Run the Application

**Terminal 1 - Start Ollama (if not running):**
```bash
ollama serve
```

**Terminal 2 - Start Backend:**
```bash
cd resume-screener
python -m uvicorn backend.main:app --reload --port 8000
```

**Terminal 3 - Start Frontend:**
```bash
cd resume-screener/frontend
streamlit run app.py
```

#### 6. Open Browser
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 📁 Project Structure

```
resume-screener/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── services/
│   │   ├── ai_service.py       # Ollama AI integration
│   │   ├── ai_service_mock.py  # Mock for testing
│   │   └── ranking_service.py  # Candidate ranking logic
│   ├── routes/
│   │   ├── employees.py        # Employee API endpoints
│   │   ├── candidates.py       # Candidate API endpoints
│   │   └── dashboard.py        # Analytics endpoints
│   ├── models/
│   │   ├── employee.py         # Employee Pydantic model
│   │   └── candidate.py        # Candidate Pydantic model
│   └── utils/
│       ├── database.py         # SQLite operations
│       └── parser.py           # PDF text extraction
├── frontend/
│   ├── app.py                  # Main Streamlit app
│   ├── components/
│   │   ├── language_manager.py # Multi-language support
│   │   └── ui_parts.py         # Reusable UI components
│   └── assets/
│       └── style.css           # Custom styling
├── pages/
│   ├── 1_Employee_Database.py  # Employee management page
│   ├── 2_Recruitment_Pipeline.py # Recruitment tracking
│   ├── 3_HR_Dashboard.py       # Analytics dashboard
│   └── 4_Resume_Screener.py    # AI resume screening
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/screen` | AI resume screening |
| GET | `/api/employees` | Get all employees |
| POST | `/api/employees` | Add new employee |
| PUT | `/api/employees/{id}` | Update employee |
| DELETE | `/api/employees/{id}` | Delete employee |
| GET | `/api/candidates` | Get all candidates |
| POST | `/api/candidates` | Add new candidate |
| PUT | `/api/candidates/{id}/status` | Update candidate status |
| GET | `/api/dashboard/stats` | Get HR analytics |
| GET | `/health/ollama` | Check AI service health |

## 💻 Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit, HTML/CSS |
| **Backend** | FastAPI, Python |
| **AI Model** | Ollama (Llama 3.2 / Qwen 2.5) |
| **Database** | SQLite |
| **PDF Processing** | pdfplumber, PyPDF2 |
| **Data Visualization** | Plotly, Pandas |

## 🎯 AI Model Details

### Current Model: Qwen 2.5 (7B parameters)
- Excellent Thai language support
- 4.7GB model size
- Runs locally on Mac M2 Pro at 30-50 tokens/second

### Alternative Models:
| Model | Size | Speed | Use Case |
|-------|------|-------|----------|
| llama3.2:3b | 3GB | Fast | General use |
| llama3.2:1b | 1.3GB | Very Fast | Quick screening |
| mistral:7b | 4.1GB | Moderate | High accuracy |

## 📊 Project Status

**Current Completion: 85%**

| Feature | Status |
|---------|--------|
| AI Resume Screening | ✅ Complete |
| Employee Database | ✅ Complete |
| Recruitment Pipeline | ✅ Complete |
| HR Dashboard | ✅ Complete |
| Multi-language Support | ✅ Complete |
| API Endpoints | ✅ Complete |
| PDF Processing | ✅ Complete |
| Thai Language Output | 🔄 Fine-tuning |

## 🔜 Upcoming Features

- [ ] Export reports (PDF/CSV)
- [ ] Email notifications for interviews
- [ ] User authentication and roles
- [ ] Bulk employee import from Excel
- [ ] Advanced filtering and search
- [ ] Interview scheduling calendar

## 🐛 Troubleshooting

### Ollama connection error
```bash
# Check if Ollama is running
ollama list

# Restart Ollama
pkill ollama
ollama serve &
```

### Port already in use
```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Use different port
python -m uvicorn backend.main:app --reload --port 8001
```

### PDF parsing errors
```bash
# Install alternative PDF parser
pip install pymupdf
```

### Module not found errors
```bash
# Ensure you're in the correct directory
cd /path/to/resume-screener

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 👥 Contributors

- Your Name - Project Lead & Developer

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Google Gemini AI (original inspiration)
- Ollama for local LLM deployment
- Streamlit for amazing frontend framework
- FastAPI for backend API

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Built with ❤️ using AI, Streamlit, and FastAPI**
```

## To add screenshots (optional):

Create a `screenshots/` folder and add:

```markdown
## 📸 Screenshots

### Landing Page
![Landing Page](screenshots/landing.png)

### AI Resume Screener
![Resume Screener](screenshots/resume_screener.png)

### Employee Database
![Employee Database](screenshots/employees.png)

### Recruitment Pipeline
![Recruitment Pipeline](screenshots/pipeline.png)

### HR Dashboard
![HR Dashboard](screenshots/dashboard.png)
```