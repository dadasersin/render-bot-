from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

@app.get("/")
async def root():
    return {"message": "Hello from backend!"}