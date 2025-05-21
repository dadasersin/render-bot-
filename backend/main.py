from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Google Sites için CORS ayarı (test için "*" da kullanılabilir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sites.google.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    return {"message": "Merhaba, backend yanıt verdi!"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⭐ CORS Middleware'i EKLE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için sadece "https://sites.google.com" da yazabilirsin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI"}
