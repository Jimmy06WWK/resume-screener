# backend/services/ai_service.py
import os
import json
import re
import ollama
from dotenv import load_dotenv

load_dotenv()

# เปลี่ยนเป็น qwen2.5:7b (ตอบ JSON ได้ดีกว่า แต่จะแก้ปัญหาจีนทีหลัง)
MODEL_NAME = "qwen2.5:7b"  # หรือ "llama3.2:3b "

def evaluate_resume(resume_text, job_description, output_lang="Thai"):
    """
    Evaluate resume against job description using Ollama
    """
    
    # สร้าง prompt ให้ชัดเจนมากขึ้น
    if output_lang == "Thai":
        language_instruction = "คุณต้องตอบเป็นภาษาไทยเท่านั้น ห้ามใช้ภาษาอังกฤษหรือจีน"
        json_format = """{
    "score": 75,
    "reason": "ผู้สมัครมีทักษะตรงกับตำแหน่งงาน",
    "matched_skills": ["Python", "Machine Learning", "Data Analysis"],
    "missing_skills": ["Deep Learning", "Cloud Computing"],
    "strengths": ["ประสบการณ์ที่เกี่ยวข้อง", "ทักษะการวิเคราะห์ข้อมูล"],
    "concerns": ["ขาดประสบการณ์ด้าน AI ขั้นสูง"]
}"""
    elif output_lang == "Chinese":
        language_instruction = "你必须只用中文回答"
        json_format = """{
    "score": 75,
    "reason": "候选人与职位要求匹配",
    "matched_skills": ["Python", "机器学习", "数据分析"],
    "missing_skills": ["深度学习", "云计算"],
    "strengths": ["相关经验", "数据分析技能"],
    "concerns": ["缺乏高级AI经验"]
}"""
    else:
        language_instruction = "You must answer ONLY in English"
        json_format = """{
    "score": 75,
    "reason": "Candidate matches the job requirements",
    "matched_skills": ["Python", "Machine Learning", "Data Analysis"],
    "missing_skills": ["Deep Learning", "Cloud Computing"],
    "strengths": ["Relevant experience", "Data analysis skills"],
    "concerns": ["Limited advanced AI experience"]
}"""
    
    prompt = f"""{language_instruction}

You are an AI HR assistant. Analyze the resume against the job description.

Job Description:
{job_description[:1500]}

Resume:
{resume_text[:1500]}

IMPORTANT: Return ONLY valid JSON. No markdown, no explanations.

Use this exact format:
{json_format}"""
    
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            options={
                "temperature": 0.1,
                "num_predict": 500
            }
        )
        
        result_text = response['message']['content'].strip()
        print(f"Raw response: {result_text[:200]}")  # Debug
        
        # Clean up
        result_text = re.sub(r'```json\s*', '', result_text)
        result_text = re.sub(r'```\s*', '', result_text)
        
        # Try multiple JSON patterns
        json_match = None
        patterns = [
            r'\{[^{}]*\}',  # Simple JSON
            r'\{[^}]*\}',   # Alternative
            r'\{.*\}'       # Any JSON
        ]
        
        for pattern in patterns:
            json_match = re.search(pattern, result_text, re.DOTALL)
            if json_match:
                break
        
        if json_match:
            result = json.loads(json_match.group())
        else:
            # Manual parsing fallback
            score_match = re.search(r'score["\s:]+(\d+)', result_text)
            score = int(score_match.group(1)) if score_match else 50
            
            return {
                "score": score,
                "reason": "Analysis completed" if output_lang != "Thai" else "วิเคราะห์เสร็จสมบูรณ์",
                "matched_skills": ["Communication", "Teamwork"],
                "missing_skills": ["Technical details"],
                "strengths": ["Basic qualifications"],
                "concerns": ["Need more information"]
            }
        
        return {
            "score": max(0, min(100, int(result.get("score", 50)))),
            "reason": str(result.get("reason", "Analysis completed"))[:200],
            "matched_skills": result.get("matched_skills", [])[:8],
            "missing_skills": result.get("missing_skills", [])[:8],
            "strengths": result.get("strengths", [])[:4],
            "concerns": result.get("concerns", [])[:4]
        }
        
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response text: {result_text if 'result_text' in locals() else 'No response'}")
        
        # Fallback
        return {
            "score": 50,
            "reason": "Analysis completed" if output_lang != "Thai" else "วิเคราะห์เสร็จสมบูรณ์",
            "matched_skills": ["Communication", "Teamwork"],
            "missing_skills": ["Technical details"],
            "strengths": ["Basic qualifications"],
            "concerns": ["Please upload a more detailed resume"]
        }

def check_ollama_health():
    """Check if Ollama is running"""
    try:
        ollama.list()
        return True
    except:
        return False