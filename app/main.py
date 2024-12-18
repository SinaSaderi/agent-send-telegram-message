from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/ping")
async def ping():
    return {"message": "pong"}
