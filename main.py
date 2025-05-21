from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# .env dosyasını yükle (örneğin api.env)
load_dotenv("api.env")

app = FastAPI()

# CORS ayarları - dışardan istek kabul etmek için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için spesifik domain ekleyebilirsin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq API anahtarını ortam değişkeninden al
openai.api_key = os.getenv("GROQ_API_KEY")
# Groq'un OpenAI API uyumlu URL'si
openai.base_url = "https://api.groq.com/openai/v1"

# İstek gövdesi modeli
class PromptRequest(BaseModel):
    prompt: str

# Kod üretme endpoint'i
@app.post("/api/generate-code")
async def generate_code(request: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="mixtral-8x7b-32768",  # Groq destekli model
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

# Ana sayfa endpoint'i
@app.get("/")
async def root():
    return {"message": "Groq AI API çalışıyor, /api/generate-code endpoint'ini kullanın."}
