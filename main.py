from fastapi import FastAPI

app = FastAPI(title="Premium API")

@app.get("/")
async def root():
    return {"status":"online"}

@app.get("/stats")
async def stats():
    return {"users":152,"keys":87}
