from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from pydantic import BaseModel
import gc
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="RAG ChatBot API", version="1.0.0")

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting RAG ChatBot API...")
    # Check if required environment variables are set
    required_vars = ["GROQ_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        logger.warning(f"Missing environment variables: {missing_vars}")
    else:
        logger.info("All required environment variables are set")
    
    # Import here to avoid startup errors if env vars are missing
    try:
        from query_pipeline import rag_pipeline
        logger.info("Query pipeline imported successfully")
    except Exception as e:
        logger.error(f"Failed to import query pipeline: {e}")

@app.get("/")
def read_root():
    return {"message": "RagChatBot backend is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "memory_usage": "optimized"}

@app.get("/env-check")
def env_check():
    """Check environment variables (without exposing sensitive data)"""
    env_status = {
        "GROQ_API_KEY": "set" if os.getenv("GROQ_API_KEY") else "missing",
        "PINECONE_API_KEY": "set" if os.getenv("PINECONE_API_KEY") else "missing",
        "PINECONE_INDEX": "set" if os.getenv("PINECONE_INDEX") else "missing",
        "PINECONE_ENV": "set" if os.getenv("PINECONE_ENV") else "missing"
    }
    return {"environment_variables": env_status}

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        from query_pipeline import rag_pipeline
        response = rag_pipeline(request.query)
        # Force garbage collection after each request
        gc.collect()
        return {"response": response}
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return {"error": str(e)} 