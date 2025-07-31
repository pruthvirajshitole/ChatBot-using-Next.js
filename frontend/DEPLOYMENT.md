# Frontend Deployment Guide for Vercel

## Setting up Backend URL

### Step 1: Get your Render Backend URL
Your backend URL will be something like: `https://your-app-name.onrender.com`

### Step 2: Set Environment Variable in Vercel

#### Option A: Using Vercel Dashboard (Recommended)
1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add a new environment variable:
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `https://your-app-name.onrender.com` (your actual Render URL)
   - **Environment:** Select all environments (Production, Preview, Development)

#### Option B: Using Vercel CLI
```bash
# Install Vercel CLI if you haven't
npm i -g vercel

# Login to Vercel
vercel login

# Add environment variable
vercel env add NEXT_PUBLIC_API_URL
```

### Step 3: Deploy
```bash
# Deploy to Vercel
vercel --prod
```

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Your Render backend URL | `https://rag-chatbot-backend.onrender.com` |

## Testing

### Local Development
```bash
# Start the development server
npm run dev

# The app will use localhost:8000 by default
```

### Production
- Deploy to Vercel
- The app will use the `NEXT_PUBLIC_API_URL` environment variable

## Troubleshooting

### CORS Issues
If you get CORS errors, make sure your backend (Render) has CORS configured properly. The backend should allow requests from your Vercel domain.

### Environment Variable Not Working
1. Check that the variable name is exactly `NEXT_PUBLIC_API_URL`
2. Ensure it's set for the correct environment (Production/Preview/Development)
3. Redeploy after adding environment variables

### Backend Connection Issues
1. Verify your Render backend is running
2. Test the backend URL directly: `https://your-backend-url.onrender.com/`
3. Check the `/health` endpoint: `https://your-backend-url.onrender.com/health`

## Configuration Files

- `config.ts` - Centralized configuration management
- `next.config.ts` - Next.js configuration
- `package.json` - Dependencies and scripts 