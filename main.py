from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Key

app = FastAPI()

Base.metadata.create_all(bind=engine)

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
        "status": "online"
    }

@app.get("/keys")
async def get_keys():

    db: Session = SessionLocal()

    keys = db.query(Key).all()

    return [
        {
            "key": k.key,
            "redeemed": k.redeemed
        }
        for k in keys
    ]

@app.post("/create-test-key")
async def create_test_key():

    db: Session = SessionLocal()

    key = Key(
        key="PREMIUM-123"
    )

    db.add(key)
    db.commit()

    return {
        "success": True
    }
