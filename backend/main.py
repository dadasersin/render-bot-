from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate_and_run")
async def generate_and_run(req: CodeRequest):
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not set")

    # GPT’den Python kodu üret
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a python script for: {req.prompt}",
            max_tokens=150,
            temperature=0.5,
        )
        code = completion.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

    # Kod çalıştır
    try:
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=5
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Execution timed out")

    return {
        "generated_code": code,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
