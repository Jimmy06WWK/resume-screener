from pydantic import BaseModel
from typing import Optional, List

class Candidate(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone: str
    position_applied: str
    status: str = "new"
    score: Optional[float] = 0
    matched_skills: Optional[List[str]] = []
    missing_skills: Optional[List[str]] = []
    resume_filename: Optional[str] = ""
    interview_date: Optional[str] = None
    interview_notes: Optional[str] = None
    offer_sent_date: Optional[str] = None
    offer_accepted: Optional[bool] = False
    hired_date: Optional[str] = None
    created_at: Optional[str] = None

class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    position_applied: str
    score: Optional[float] = 0
    matched_skills: Optional[List[str]] = []
    missing_skills: Optional[List[str]] = []
    resume_filename: Optional[str] = ""

class CandidateUpdateStatus(BaseModel):
    status: str
    interview_date: Optional[str] = None
    interview_notes: Optional[str] = None