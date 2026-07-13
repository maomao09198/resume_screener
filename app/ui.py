# app/ui.py
import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("🤖 AI-Powered Resume Screener")

# Sidebar
with st.sidebar:
    st.header("Upload Resume")
    uploaded_file = st.file_uploader("Choose PDF/DOCX", type=['pdf', 'docx'])
    job_description = st.text_area("Paste Job Description", 
                                   height=150)
    
    if uploaded_file and st.button("Analyze"):
        files = {"file": uploaded_file}
        response = requests.post("http://localhost:8000/upload/", 
                                 files=files)
        
        if response.status_code == 200:
            st.session_state.filename = uploaded_file.name
            st.success("Resume uploaded!")

# Main area
if 'filename' in st.session_state:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Candidate Analysis")
        
        # Get prediction
        payload = {
            "filename": st.session_state.filename,
            "job_description": job_description
        }
        response = requests.post("http://localhost:8000/predict/", 
                                json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            # Score gauge
            score = result['fit_score']
            st.metric("Fit Score", f"{score}%")
            st.progress(score/100)
            
            # Display skills
            st.subheader("Matched Skills")
            st.chips(result['matched_skills'])
            
            # Recommendation
            if score > 75:
                st.success("✅ **Recommendation: Move to Interview**")
            else:
                st.warning("⚠️ **Recommendation: Reject**")
            
            # Explanation
            st.subheader("AI Explanation")
            st.write(result['explanation'])
    
    with col2:
        st.subheader("Candidate Info")
        st.json(result.get('candidate', {}))