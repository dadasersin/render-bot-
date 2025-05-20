from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess, tempfile, os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kod çalıştırma modeli
class CodeRequest(BaseModel):
    language: str
    code: str

# Kod çalıştırma endpointi
@app.post("/run")
async def run_code(data: CodeRequest):
    code = data.code
    lang = data.language

    if lang == "python":
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".py", delete=False) as tmp:
            tmp.write(code)
            tmp.flush()
            try:
                output = subprocess.check_output(["python3", tmp.name], stderr=subprocess.STDOUT, timeout=5)
                return {"output": output.decode()}
            except subprocess.CalledProcessError as e:
                return {"output": e.output.decode()}
            except Exception as e:
                return {"error": str(e)}
            finally:
                os.remove(tmp.name)
    return {"error": "Unsupported language"}

# frontend klasörünü statik olarak sun
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

# Ana sayfa: / adresi için index.html göster
@app.get("/")
async def root():
    return FileResponse("frontend/index.html")
