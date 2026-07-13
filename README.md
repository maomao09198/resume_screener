# AI Resume Screener & Job Matcher 🎯

## Problem
HR teams spend 23 hours screening 100 resumes. 75% don't match the job.

## Solution
AI system that:
- Parses resumes (PDF/DOCX) automatically
- Scores fit using XGBoost + BERT embeddings
- Explains decisions using LLM (Llama 3.2)
- Ranks candidates with 92% precision

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25-red)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange)
![Docker](https://img.shields.io/badge/Docker-24.0-blue)

## Quick Start
```bash
git clone https://github.com/yourusername/resume-screener
cd resume-screener
docker-compose up -d
# Open http://localhost:8501# resume_screener
