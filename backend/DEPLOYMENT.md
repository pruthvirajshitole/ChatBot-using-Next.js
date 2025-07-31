# Backend Deployment Guide for Render

## Memory Optimization Solutions

### Option 1: Standard Deployment (Recommended)
Use the current setup with memory optimizations:
- Lazy loading of embedding model
- Garbage collection after requests
- Lighter embedding model (`paraphrase-MiniLM-L3-v2`)

### Option 2: Lightweight Deployment (If Option 1 fails)
If you still face memory issues, use the lightweight version:

1. Rename files:
   ```bash
   mv requirements.txt requirements_standard.txt
   mv requirements_lightweight.txt requirements.txt
   mv query_pipeline.py query_pipeline_standard.py
   mv query_pipeline_lightweight.py query_pipeline.py
   ```

2. The lightweight version uses TF-IDF instead of sentence-transformers, which uses ~90% less memory.

## Environment Variables Required

Set these in your Render dashboard:

```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name
```

## Troubleshooting

### Memory Issues
- Try the lightweight version
- Upgrade to Render's 1GB or 2GB plan
- Monitor memory usage with `/health` endpoint

### Version Conflicts
- The current requirements.txt uses flexible versioning
- If issues persist, try Python 3.9 instead of 3.10

### Package Name Issues
- **Pinecone**: Use `pinecone` package (not `pinecone-client`)
- **Import**: Use `from pinecone import Pinecone`

### Build Failures
- Check that all environment variables are set
- Ensure Pinecone index exists and is accessible
- Verify API keys are valid

## Testing Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Test endpoints:
- `GET /` - Health check
- `GET /health` - Memory status
- `POST /chat` - Chat endpoint 