# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run both services
CMD ["sh", "-c", "uvicorn app.api:app --host 0.0.0.0 --port 8000 & streamlit run app/ui.py --server.port 8501 --server.address 0.0.0.0"]