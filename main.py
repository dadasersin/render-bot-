from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# .env dosyasından API anahtarını oku
load_dotenv()
openai.api_key = os.getenv("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")

app = FastAPI()

# CORS ayarları - Google Sites veya başka frontendlerden istek kabul etmek için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # istersen sadece belirli domainler yazabilirsin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# İstek için model
class PromptRequest(BaseModel):
    prompt: str

# Yapay zekaya kod üretme isteği atacağımız endpoint
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

# Ana sayfa endpoint'i - API çalışıyor kontrolü için
@app.get("/")
async def root():
    return {"message": "API çalışıyor, lütfen /api/... endpointlerini kullanın."}
