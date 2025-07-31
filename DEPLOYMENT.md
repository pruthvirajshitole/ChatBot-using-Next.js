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

## Frontend Deployment Options

### Option 1: Deploy to Vercel (Recommended)

#### Current Configuration ✅

The project now has the correct Vercel configuration:

**vercel.json:**
```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/.next",
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
    "build": "cd frontend && npm install && npm run build",
    "dev": "cd frontend && npm run dev",
    "start": "cd frontend && npm run start"
  }
}
```

#### Deploy to Vercel

1. **Push the changes to GitHub:**
```bash
git add .
git commit -m "Add working Vercel configuration"
git push
```

2. **Vercel will automatically redeploy** with the new configuration

3. **Set Environment Variable in Vercel dashboard:**
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `https://chatbot-using-next-js.onrender.com`
   - **Environment:** All (Production, Preview, Development)

### Option 2: Deploy to Render

#### Configuration ✅

**render.yaml:**
```yaml
services:
  - type: web
    name: chatbot-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1 --log-level info
    envVars:
      - key: PYTHON_VERSION
        value: 3.10
      - key: PYTHONUNBUFFERED
        value: 1
      - key: PYTHONDONTWRITEBYTECODE
        value: 1
      - key: PORT
        value: 8000
    plan: starter
    rootDir: backend

  - type: web
    name: chatbot-frontend
    env: node
    buildCommand: npm install && npm run build
    startCommand: npm start
    envVars:
      - key: NODE_VERSION
        value: 18
      - key: NEXT_PUBLIC_API_URL
        value: https://chatbot-using-next-js.onrender.com
    plan: starter
    rootDir: frontend
```

#### Deploy to Render

1. **Push the changes to GitHub**
2. **Connect your repository to Render**
3. **Render will automatically deploy both backend and frontend**

## Troubleshooting

### Vercel Build Issues
- **Error:** "routes-manifest.json couldn't be found"
  - **Solution:** The new `vercel.json` configuration should fix this
  - **Alternative:** Deploy from `frontend/` directory directly

### Render Build Issues
- **Error:** "Invalid rootDirectory"
  - **Solution:** Use `rootDir: frontend` (not `rootDirectory`)
  - **Alternative:** Deploy services separately

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

### Frontend (Vercel/Render) 🔄
- [ ] Loads without errors
- [ ] Connects to backend
- [ ] Sends and receives chat messages
- [ ] Environment variable is set correctly

## Quick Commands

```bash
# Push changes to trigger deployment
git add .
git commit -m "Add working Vercel configuration"
git push

# Test backend locally
cd backend
uvicorn main:app --reload

# Test frontend locally
cd frontend
npm run dev
``` 