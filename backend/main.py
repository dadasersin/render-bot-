from flask_cors import CORS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⭐ CORS ayarları — Google Sites gibi dış kaynaklara izin verir
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için sadece belirli domain yazmak istersen: ["https://sites.google.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI"}
