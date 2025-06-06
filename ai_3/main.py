from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def running():
    return {"AI_1 running"}

@app.post("/ai_whisper")
def whisper():
    return {"Whisper"}

@app.post("/ai_reccomend")
def whisper():
    return {"RECOMMEND"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)