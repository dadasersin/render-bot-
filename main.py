from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# 📦 .env dosyasını yükle (.env yerine api.env kullandıysan burayı değiştir)
load_dotenv("api.env")

# 🔑 OpenAI API anahtarını ortam değişkeninden al
openai.api_key = os.getenv("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")

app = FastAPI()

# 🌐 CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sadece belirli domainler eklemek için örnek: ["https://sites.google.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧾 İstek gövdesi modeli
class PromptRequest(BaseModel):
    prompt: str

# 🚀 Kod üretme API'si
@app.post("/api/generate-code")
async def generate_code(request: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen bir uzman Python geliştiricisisin."},
                {"role": "user", "content": request.prompt}
            ],
            temperature=0.7,
        )
        result = response['choices'][0]['message']['content']
        return {"code": result}
    except Exception as e:
        return {"error": str(e)}

# ✅ Ana sayfa - sağlık kontrolü
@app.get("/")
async def root():
    return {"message": "API çalışıyor, lütfen /api/generate-code endpoint'ini kullanın."}
