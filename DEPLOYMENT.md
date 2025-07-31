# Full Stack Deployment Guide

## Backend (Render) ✅ DEPLOYED

### Status: Running Successfully
- **URL:** https://chatbot-using-next-js.onrender.com/
- **Status:** ✅ Working

### Environment Variables Required
Set these in your Render dashboard:
```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name
```

## Frontend (Vercel) 🔄 DEPLOYING

### Current Configuration ✅

The project now has the correct Vercel configuration:

**vercel.json:**
```json
{
  "buildCommand": "cd frontend && npm run build",
  "outputDirectory": "frontend/.next",
  "installCommand": "cd frontend && npm install",
  "framework": "nextjs"
}
```

**package.json:**
```json
{
  "name": "chatbot-nextjs",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "build": "cd frontend && npm run build",
    "dev": "cd frontend && npm run dev",
    "start": "cd frontend && npm run start"
  }
}
```

### Deploy to Vercel

1. **Push the changes to GitHub:**
```bash
git add .
git commit -m "Add Vercel configuration"
git push
```

2. **Vercel will automatically redeploy** with the new configuration

### Alternative: Manual Deploy

If automatic deployment doesn't work:

1. **Go to Vercel dashboard**
2. **Redeploy your project** (it will use the new configuration)
3. **Or create a new project** and import your repository

## Environment Variables for Frontend

Set in Vercel dashboard:
- **Name:** `NEXT_PUBLIC_API_URL`
- **Value:** `https://chatbot-using-next-js.onrender.com`
- **Environment:** All (Production, Preview, Development)

## Troubleshooting

### Vercel Build Issues
- **Error:** "routes-manifest.json couldn't be found"
  - **Solution:** The new `vercel.json` configuration should fix this
  - **Alternative:** Deploy from `frontend/` directory directly

### Backend Connection Issues
- ✅ Backend is running at https://chatbot-using-next-js.onrender.com/
- Check environment variables are set correctly
- Test backend endpoints directly

## Testing Checklist

### Backend (Render) ✅
- [x] `GET /` - Returns welcome message
- [ ] `GET /health` - Returns health status
- [ ] `GET /env-check` - Shows environment variables status
- [ ] `POST /chat` - Responds to queries

### Frontend (Vercel) 🔄
- [ ] Loads without errors
- [ ] Connects to backend
- [ ] Sends and receives chat messages
- [ ] Environment variable is set correctly

## Quick Commands

```bash
# Push changes to trigger Vercel deployment
git add .
git commit -m "Add Vercel configuration"
git push

# Test backend locally
cd backend
uvicorn main:app --reload

# Test frontend locally
cd frontend
npm run dev
``` 