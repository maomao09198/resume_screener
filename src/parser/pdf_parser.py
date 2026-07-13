# src/parser/pdf_parser.py
import PyPDF2
import re

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def extract_text(self):
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def extract_email_phone(self, text):
        email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        phone = re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
        return {
            'email': email.group(0) if email else None,
            'phone': phone.group(0) if phone else None
        }