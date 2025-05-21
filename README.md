# FastAPI Backend + Google Sites Frontend Entegrasyonu

## Backend'i çalıştırmak için:

1. Python 3.11+ yüklü olmalı.
2. Gerekli paketleri yükle:
   pip install fastapi uvicorn
3. Backend'i başlat:
   uvicorn backend.main:app --host 0.0.0.0 --port 8000

## Frontend Google Sites'ta:

- Google Sites > Embed > Embed Code seçeneğine tıklayın.
- frontend/index.html içeriğini açıp, 
  "(https://render-bot-r9rk.onrender.com)/api/hello" kısmını kendi backend URL'nizle değiştirip kopyalayın.
- Embed kodu olarak yapıştırın ve kaydedin.

## Not:

- Backend URL'nizin internetten erişilebilir olması gerekir.
- CORS ayarı Google Sites domainine göre backend'de yapılmıştır.
