from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/run")
async def run_code(req: CodeRequest):
    try:
        result = subprocess.run(
            ["python3", "-c", req.code],
            capture_output=True,
            text=True,
            timeout=5
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Execution timed out")

