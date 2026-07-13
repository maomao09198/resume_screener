# app/api.py
from fastapi import FastAPI, UploadFile, File
import shutil
import joblib
import numpy as np
from pathlib import Path
from src.parser.pdf_parser import ResumeParser
from src.features.extractor import FeatureExtractor
from src.llm.explainer import ResumeExplainer

app = FastAPI()
model = joblib.load('models/resume_model.pkl')
extractor = FeatureExtractor()
explainer = ResumeExplainer()

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = f"data/raw/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": "Resume uploaded", "filename": file.filename}

@app.post("/predict/")
async def predict_fit(filename: str, job_description: str):
    # Parse resume
    parser = ResumeParser(f"data/raw/{filename}")
    text = parser.extract_text()
    
    # Extract features
    features = extractor.create_features(text)
    
    # Predict
    X = np.concatenate([
        [features['num_skills'], features['skill_diversity']],
        features['bert_embedding']
    ]).reshape(1, -1)
    
    score = model.predict_proba(X)[0][1] * 100  # Fit percentage
    
    # LLM explanation
    explanation = explainer.generate_feedback(text, job_description, score)
    
    return {
        "candidate": parser.extract_email_phone(text),
        "fit_score": round(score, 2),
        "matched_skills": features['skills_list'],
        "explanation": explanation,
        "recommendation": "Interview" if score > 75 else "Reject"
    }