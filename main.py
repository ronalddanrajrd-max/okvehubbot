from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Premium Whitelist API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "premium whitelist",
        "version": "1.0.0"
    }

@app.get("/stats")
async def stats():
    return {
        "users": 152,
        "keys": 87,
        "projects": 4
    }

@app.get("/health")
async def health():
    return {
        "healthy": True
    }
