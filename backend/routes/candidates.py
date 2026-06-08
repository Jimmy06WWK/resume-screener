# backend/routes/candidates.py
from fastapi import APIRouter, HTTPException
from typing import Optional
from backend.models.candidate import Candidate, CandidateCreate, CandidateUpdateStatus
from backend.utils.database import get_all_candidates, create_candidate, update_candidate_status, update_candidate_offer, delete_candidate

router = APIRouter()

@router.get("/candidates", response_model=list)
async def list_candidates(status: Optional[str] = None):
    return get_all_candidates(status)

@router.post("/candidates", response_model=dict)
async def add_candidate(candidate: CandidateCreate):
    cand_id = create_candidate(candidate.dict())
    return {"success": True, "id": cand_id, "message": "Candidate added to pipeline"}

@router.put("/candidates/{cand_id}/status")
async def change_status(cand_id: int, update: CandidateUpdateStatus):
    update_candidate_status(cand_id, update.status, update.interview_date, update.interview_notes)
    return {"success": True, "message": f"Status updated to {update.status}"}

@router.put("/candidates/{cand_id}/offer")
async def update_offer(cand_id: int, offer_sent_date: Optional[str] = None, 
                       offer_accepted: Optional[bool] = None, hired_date: Optional[str] = None):
    update_candidate_offer(cand_id, offer_sent_date, offer_accepted, hired_date)
    return {"success": True, "message": "Offer updated"}

@router.delete("/candidates/{cand_id}")
async def remove_candidate(cand_id: int):
    delete_candidate(cand_id)
    return {"success": True, "message": "Candidate deleted"}