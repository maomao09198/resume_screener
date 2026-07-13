# src/llm/explainer.py
import ollama  # or openai

class ResumeExplainer:
    def __init__(self, use_local=True):
        self.use_local = use_local
        
    def generate_feedback(self, resume_text, job_description, score):
        """Generate human-readable feedback on fit"""
        prompt = f"""
        Given this resume summary: {resume_text[:500]}
        And job description: {job_description}
        The candidate scored {score}/100.
        
        Provide:
        1. Top 3 matching skills
        2. Top 3 missing skills
        3. 2 sentence summary of why they fit or don't
        4. Improvement suggestions
        
        Format as JSON.
        """
        
        if self.use_local:
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': prompt}
            ])
            return response['message']['content']
        else:
            # OpenAI implementation
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content']