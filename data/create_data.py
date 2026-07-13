# data/create_data.py
import pandas as pd
import random

# Create 500 sample resumes with labels
def generate_resume_data():
    skills_pool = ['Python', 'SQL', 'Machine Learning', 'Deep Learning', 'NLP',
                  'TensorFlow', 'PyTorch', 'AWS', 'Docker', 'Kubernetes',
                  'React', 'Node.js', 'Java', 'C++', 'Data Science']
    
    jobs = {
        'Data Scientist': ['Python', 'SQL', 'ML', 'Statistics', 'TensorFlow'],
        'ML Engineer': ['Python', 'ML', 'Docker', 'AWS', 'PyTorch'],
        'Software Developer': ['Java', 'Python', 'SQL', 'React', 'Docker']
    }
    
    data = []
    for i in range(500):
        job = random.choice(list(jobs.keys()))
        has_skills = random.sample(skills_pool, random.randint(2, 6))
        fit = 1 if len(set(has_skills) & set(jobs[job])) >= 3 else 0
        
        data.append({
            'resume_id': i,
            'skills': ','.join(has_skills),
            'years_experience': random.randint(0, 10),
            'job_title': job,
            'fit': fit
        })
    
    df = pd.DataFrame(data)
    df.to_csv('data/labels.csv', index=False)
    return df

generate_resume_data()