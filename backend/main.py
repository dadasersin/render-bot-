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
