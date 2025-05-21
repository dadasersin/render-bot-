from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import openai
import os
import json

app = FastAPI()

# CORS ayarları (Google Sites vs için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("sk-proj-P-k5JrUtMrD1lisxd75Bbmn5aki8mUFal7hKbyA48_MDcMGKkq6iwtUsuZRdYxZqlK7cxTOsiQT3BlbkFJZLM98dVdkMETDp50kFGj89CMq0GFleZhYuUwH8Ceiz4")

@app.post("/generate_and_run")
async def generate_and_run(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    # OpenAI GPT ile Python kodu üret
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3,
    )
    code = response.choices[0].message.content

    # Üretilen kodu subprocess ile çalıştır
    try:
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = {
            "code": code,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        output = {
            "code": code,
            "error": "Execution timed out."
        }

    return output

@app.get("/")
async def root():
    return {"message": "FastAPI + OpenAI Python Code Runner is up!"}
