# backend/services/ranking_service.py
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.services.ai_service import evaluate_resume
from backend.utils.parser import extract_text_from_pdf

def rank_candidates(resumes, jd_text, output_lang="Thai"):
    all_results = []
    
    def process_one(uploaded_file):
        try:
            file_bytes = uploaded_file.file.read()
            filename = uploaded_file.filename
            resume_text = extract_text_from_pdf(file_bytes)
            
            if resume_text:
                # Ollama ไม่มี quota limit เลยไม่ต้องรอ
                # time.sleep(2)  # comment out หรือลบเลย
                analysis = evaluate_resume(resume_text, jd_text, output_lang)
                analysis['candidate_name'] = filename.replace('.pdf', '').replace('_', ' ').title()
                return analysis
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    # สามารถเพิ่ม max_workers ได้ เพราะ Ollama ไม่ limit
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(process_one, f) for f in resumes]
        for future in as_completed(futures):
            result = future.result()
            if result:
                all_results.append(result)
    
    return sorted(all_results, key=lambda x: x.get('score', 0), reverse=True)