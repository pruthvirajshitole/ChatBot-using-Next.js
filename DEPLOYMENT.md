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

The project now has a simplified Vercel configuration:

**vercel.json:**
```json
{
  "rootDirectory": "frontend",
  "framework": "nextjs"
}
```

**.vercelignore:**
```
backend/
node_modules/
.git/
.env
.env.local
```

### Deploy to Vercel

1. **Push the changes to GitHub:**
```bash
git add .
git commit -m "Simplify Vercel configuration"
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
- **Error:** "Command cd frontend && npm install exited with 1"
  - **Solution:** Using simplified `vercel.json` with `rootDirectory: "frontend"`
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
git commit -m "Simplify Vercel configuration"
git push

# Test backend locally
cd backend
uvicorn main:app --reload

# Test frontend locally
cd frontend
npm run dev
``` 