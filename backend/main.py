from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware ayarı
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sites.google.com/view/dadasersin/httpsdashboard-render-com"],  # Geliştirme aşamasında tüm domainlere izin veriyoruz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI"}

