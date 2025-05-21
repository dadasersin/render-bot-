from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# .env dosyasından anahtarları al
load_dotenv("api.env")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq API ayarları
openai.api_key = os.getenv("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")  # api.env içine yaz: GROQ_API_KEY=xxx
openai.base_url = "https://api.groq.com/openai/v1"  # 🔁 DİKKAT: bu Groq'un URL’si

# İstek modeli
class PromptRequest(BaseModel):
    prompt: str

# Kod üretici endpoint
@app.post("/api/generate-code")
async def generate_code(request: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="mixtral-8x7b-32768",  # Groq destekli modellerden biri
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

@app.get("/")
async def root():
    return {"message": "Groq AI API çalışıyor, /api/generate-code endpoint'ini kullanın."}
