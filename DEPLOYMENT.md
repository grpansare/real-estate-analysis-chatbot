# Deployment Guide

This guide will help you deploy the Real Estate Analysis Chatbot to production.

## 📋 Prerequisites

- GitHub account
- Netlify account (for frontend)
- Render account (for backend)
- Google Gemini API key

---

## 🚀 Part 1: Deploy Backend to Render

### Step 1: Prepare Your Repository

1. **Push your code to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

### Step 2: Create Render Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `real-estate-chatbot-api` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn realestate_api.wsgi:application`

### Step 3: Set Environment Variables

In Render dashboard, add these environment variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate a new secret key (use Django's `get_random_secret_key()`) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `GEMINI_API_KEY` | Your Google Gemini API key |
| `FRONTEND_URL` | `https://your-netlify-app.netlify.app` (add after deploying frontend) |
| `PYTHON_VERSION` | `3.11.0` |

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait for deployment to complete (5-10 minutes)
3. Copy your backend URL: `https://your-app-name.onrender.com`

### Step 5: Test Backend

Visit: `https://your-app-name.onrender.com/api/health/`

You should see: `{"status":"ok","message":"Real Estate Analysis API is running"}`

---

## 🎨 Part 2: Deploy Frontend to Netlify

### Step 1: Build Configuration

The `netlify.toml` file is already configured in your project.

### Step 2: Create Environment Variable

1. Create a file `.env.production` in the `frontend` directory:
   ```
   VITE_API_URL=https://real-estate-chatbot-api-isrj.onrender.com/api
   ```
   
   Replace `your-backend-app` with your actual Render app name.

### Step 3: Deploy to Netlify

#### Option A: Deploy via Netlify UI

1. Go to [Netlify](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect to GitHub and select your repository
4. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
5. Add environment variable:
   - Go to **Site settings** → **Environment variables**
   - Add `VITE_API_URL` with your Render backend URL
6. Click **"Deploy site"**

#### Option B: Deploy via Netlify CLI

```bash
cd frontend
npm install -g netlify-cli
netlify login
netlify init
netlify deploy --prod
```

### Step 4: Update Backend CORS

1. Go back to Render dashboard
2. Update the `FRONTEND_URL` environment variable with your Netlify URL
3. Trigger a redeploy

---

## 🔄 Update Backend ALLOWED_HOSTS

After getting your Netlify URL, update Render environment variables:

1. `ALLOWED_HOSTS`: Add your Render domain (e.g., `your-app.onrender.com`)
2. `FRONTEND_URL`: Add your Netlify URL (e.g., `https://your-app.netlify.app`)

---

## ✅ Verification

### Test Backend
```bash
curl https://your-backend.onrender.com/api/health/
```

### Test Frontend
1. Visit your Netlify URL
2. Try a query: "Give me analysis of Wakad"
3. Verify you see:
   - AI-generated summary
   - Interactive chart
   - Data table

---

## 🔧 Troubleshooting

### Backend Issues

**Problem**: 500 Internal Server Error
- Check Render logs: Dashboard → Your Service → Logs
- Verify all environment variables are set
- Ensure `ALLOWED_HOSTS` includes your Render domain

**Problem**: CORS errors
- Verify `FRONTEND_URL` is set correctly
- Check that frontend URL matches exactly (with https://)

### Frontend Issues

**Problem**: API connection failed
- Verify `VITE_API_URL` environment variable
- Check browser console for errors
- Ensure backend is running (visit `/api/health/`)

**Problem**: Build fails
- Check Node.js version (should be 18+)
- Clear cache: `npm ci` then rebuild

---

## 📝 Important Notes

### Free Tier Limitations

**Render Free Tier**:
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month free

**Netlify Free Tier**:
- 100GB bandwidth/month
- Unlimited sites
- Automatic HTTPS

### Performance Tips

1. **Backend**: Consider upgrading to paid tier for production use
2. **Frontend**: Enable Netlify's asset optimization
3. **API**: Implement caching for frequently accessed data

---

## 🎯 Next Steps

1. ✅ Deploy backend to Render
2. ✅ Deploy frontend to Netlify
3. ✅ Test the application
4. 📹 Record demo video
5. 📄 Update README with live links
6. 🎉 Submit assignment!

---

## 📧 Support

If you encounter issues:
- Check Render logs for backend errors
- Check Netlify deploy logs for frontend errors
- Verify all environment variables are set correctly
