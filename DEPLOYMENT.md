# Full Stack Deployment Guide

## Backend (Render)

### Current Status
- ✅ Build successful
- ⚠️ Port binding issue (check environment variables)

### Environment Variables Required
Set these in your Render dashboard:
```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name
```

### Debugging Backend
- Check `/health` endpoint
- Check `/env-check` endpoint
- Review Render logs for startup errors

## Frontend (Vercel)

### Option 1: Deploy from Root (Recommended)

1. **Create `vercel.json` in root directory:**
```json
{
  "rootDirectory": "frontend"
}
```

2. **Deploy to Vercel:**
```bash
# From the root directory
vercel --prod
```

### Option 2: Deploy Frontend Directory Directly

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Deploy from frontend directory:**
```bash
vercel --prod
```

### Environment Variables for Frontend

Set in Vercel dashboard:
- **Name:** `NEXT_PUBLIC_API_URL`
- **Value:** `https://your-render-backend-url.onrender.com`
- **Environment:** All (Production, Preview, Development)

## Troubleshooting

### Vercel Build Issues
- **Error:** "routes-manifest.json couldn't be found"
  - **Solution:** Use `vercel.json` with `rootDirectory: "frontend"`
  - **Alternative:** Deploy from `frontend/` directory directly

### Backend Connection Issues
- Verify Render backend is running
- Check environment variables are set
- Test backend endpoints directly

### CORS Issues
- Backend already configured to allow all origins
- If issues persist, check Vercel domain is allowed

## Testing Checklist

### Backend (Render)
- [ ] `GET /` - Returns welcome message
- [ ] `GET /health` - Returns health status
- [ ] `GET /env-check` - Shows environment variables status
- [ ] `POST /chat` - Responds to queries

### Frontend (Vercel)
- [ ] Loads without errors
- [ ] Connects to backend
- [ ] Sends and receives chat messages
- [ ] Environment variable is set correctly

## Quick Commands

```bash
# Deploy backend to Render
# (Already done via Git integration)

# Deploy frontend to Vercel
vercel --prod

# Test backend locally
cd backend
uvicorn main:app --reload

# Test frontend locally
cd frontend
npm run dev
``` 