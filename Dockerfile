FROM python:3.11-slim

WORKDIR /app

# Gerekli kütüphaneler
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyasını kopyala
COPY main.py .

# Uygulama başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
