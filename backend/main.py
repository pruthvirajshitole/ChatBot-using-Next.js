from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from pydantic import BaseModel
from query_pipeline import rag_pipeline
import gc
import os

app = FastAPI(title="RAG ChatBot API", version="1.0.0")

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "RagChatBot backend is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "memory_usage": "optimized"}

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = rag_pipeline(request.query)
        # Force garbage collection after each request
        gc.collect()
        return {"response": response}
    except Exception as e:
        return {"error": str(e)} 