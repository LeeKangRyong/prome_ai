from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def running():
    return {"AI_1 running"}

@app.post("/ai_rag")
def whisper():
    return {"RAG"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)