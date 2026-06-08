import json
import random

def evaluate_resume(resume_text, job_description, output_lang="Thai"):
    """Mock version for testing without API"""
    
    # สุ่มคะแนนตามความยาวของ resume (เพื่อความสมจริง)
    base_score = min(len(resume_text) / 100, 85)
    score = min(85, max(40, base_score + random.randint(-10, 10)))
    
    # ข้อความตามภาษา
    if output_lang == "Thai":
        reason = f"ผู้สมัครมีความเหมาะสมในระดับ {score:.0f}% จากประสบการณ์และทักษะที่เกี่ยวข้อง"
        matched = ["Python", "Machine Learning", "Data Analysis"]
        missing = ["Deep Learning", "Cloud Computing"]
        strengths = ["ทักษะการวิเคราะห์ข้อมูล", "ประสบการณ์โครงการ"]
        concerns = ["ขาดประสบการณ์ด้าน AI ขั้นสูง"]
    elif output_lang == "Chinese":
        reason = f"候选人的匹配度为 {score:.0f}%，基于相关经验和技能"
        matched = ["Python", "机器学习", "数据分析"]
        missing = ["深度学习", "云计算"]
        strengths = ["数据分析技能", "项目经验"]
        concerns = ["缺乏高级AI经验"]
    else:
        reason = f"Candidate matches at {score:.0f}% based on relevant experience and skills"
        matched = ["Python", "Machine Learning", "Data Analysis"]
        missing = ["Deep Learning", "Cloud Computing"]
        strengths = ["Data analysis skills", "Project experience"]
        concerns = ["Limited advanced AI experience"]
    
    return {
        "score": round(score),
        "reason": reason,
        "matched_skills": matched,
        "missing_skills": missing,
        "strengths": strengths,
        "concerns": concerns
    }
