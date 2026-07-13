# src/features/extractor.py
import pandas as pd
from sentence_transformers import SentenceTransformer

class FeatureExtractor:
    def __init__(self):
        self.bert = SentenceTransformer('all-MiniLM-L6-v2')  # Fast embedding
        self.skill_list = ['Python', 'SQL', 'ML', 'NLP', 'TensorFlow', 
                          'PyTorch', 'AWS', 'Docker', 'React', 'Java']
    
    def extract_skills(self, text):
        """Find skills in resume text"""
        found_skills = [skill for skill in self.skill_list 
                       if skill.lower() in text.lower()]
        return found_skills
    
    def get_bert_embedding(self, text):
        """Create semantic embedding of resume"""
        return self.bert.encode(text[:512])  # Truncate to 512 tokens
    
    def create_features(self, resume_text):
        skills = self.extract_skills(resume_text)
        embedding = self.get_bert_embedding(resume_text)
        
        # Feature vector: [skill_count, unique_skills, embedding...]
        features = {
            'num_skills': len(skills),
            'skill_diversity': len(set(skills)) / len(self.skill_list),
            'bert_embedding': embedding,
            'skills_list': skills
        }
        return features