from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

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

# -----------------------------
# TEMP DATABASE
# -----------------------------

keys_db: Dict[str, dict] = {
    "PREMIUM-123": {
        "redeemed": False,
        "hwid": None,
        "user": None
    }
}


# -----------------------------
# MODELS
# -----------------------------

class RedeemRequest(BaseModel):
    key: str
    discord_id: str
    hwid: str


class ValidateRequest(BaseModel):
    key: str
    hwid: str


# -----------------------------
# ROUTES
# -----------------------------

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "premium whitelist"
    }


@app.get("/stats")
async def stats():
    total_keys = len(keys_db)

    redeemed = sum(
        1 for k in keys_db.values()
        if k["redeemed"]
    )

    return {
        "total_keys": total_keys,
        "redeemed": redeemed
    }


@app.post("/redeem")
async def redeem(data: RedeemRequest):

    if data.key not in keys_db:
        return {
            "success": False,
            "message": "Invalid key"
        }

    key_data = keys_db[data.key]

    if key_data["redeemed"]:
        return {
            "success": False,
            "message": "Key already redeemed"
        }

    key_data["redeemed"] = True
    key_data["hwid"] = data.hwid
    key_data["user"] = data.discord_id

    return {
        "success": True,
        "message": "Key redeemed successfully"
    }


@app.post("/validate")
async def validate(data: ValidateRequest):

    if data.key not in keys_db:
        return {
            "success": False
        }

    key_data = keys_db[data.key]

    if key_data["hwid"] != data.hwid:
        return {
            "success": False
        }

    return {
        "success": True
    }


@app.post("/reset-hwid")
async def reset_hwid(key: str):

    if key not in keys_db:
        return {
            "success": False
        }

    keys_db[key]["hwid"] = None

    return {
        "success": True,
        "message": "HWID reset"
    }


@app.get("/keys")
async def get_keys():
    return keys_db
