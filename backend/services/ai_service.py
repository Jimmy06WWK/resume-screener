import os
import json
from dotenv import load_dotenv

load_dotenv()

# ใช้ google-genai แทน google.generativeai
from google import genai
from google.genai import types

# ตั้งค่า API Key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def evaluate_resume(resume_text, job_description, output_lang="Thai"):
    prompt = f"""
    Evaluate the resume against the job description with high precision.
    Instructions:
    1. Score the candidate (0-100) based on: Technical (40%), Experience (30%), Education/Projects (20%), Soft Skills (10%).
    2. Support English, Thai, and Chinese resumes.
    3. IMPORTANT: Write ALL descriptive fields ('reason', 'matched_skills', 'missing_skills', 'strengths', 'concerns') 
       strictly in {output_lang} language only.

    JD: {job_description}
    Resume: {resume_text}

    Return ONLY a valid JSON object:
    {{
      "score": number,
      "reason": "summary in {output_lang}",
      "matched_skills": ["list"],
      "missing_skills": ["list"],
      "strengths": ["list"],
      "concerns": ["list"]
    }}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json"
        )
    )
    
    return json.loads(response.text)
