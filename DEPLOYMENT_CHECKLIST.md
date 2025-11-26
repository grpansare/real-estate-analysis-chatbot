# Deployment Checklist

## ✅ Pre-Deployment Checklist

### 1. Code Preparation
- [ ] All code committed to GitHub
- [ ] `.env` files added to `.gitignore`
- [ ] Production environment variables documented
- [ ] Dependencies up to date

### 2. Backend (Render)
- [ ] Create Render account
- [ ] Create new Web Service
- [ ] Connect GitHub repository
- [ ] Configure build settings:
  - Root Directory: `backend`
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn realestate_api.wsgi:application`
- [ ] Set environment variables:
  - `SECRET_KEY`
  - `DEBUG=False`
  - `ALLOWED_HOSTS`
  - `GEMINI_API_KEY`
  - `FRONTEND_URL`
- [ ] Deploy and test `/api/health/` endpoint

### 3. Frontend (Netlify)
- [ ] Create Netlify account
- [ ] Create new site from GitHub
- [ ] Configure build settings:
  - Base directory: `frontend`
  - Build command: `npm run build`
  - Publish directory: `frontend/dist`
- [ ] Set environment variable:
  - `VITE_API_URL` = your Render backend URL
- [ ] Deploy and test

### 4. Post-Deployment
- [ ] Update backend `FRONTEND_URL` with Netlify URL
- [ ] Update backend `ALLOWED_HOSTS` with Render domain
- [ ] Test full application flow
- [ ] Update README with live demo links

### 5. Demo Video
- [ ] Record 1-2 minute demo showing:
  - Application startup
  - Sample queries
  - Results (summary, charts, tables)
  - UI/UX walkthrough
- [ ] Upload to YouTube/Google Drive
- [ ] Add link to README

### 6. Final Submission
- [ ] GitHub repository link
- [ ] Live demo link (Netlify)
- [ ] Demo video link
- [ ] README updated with all links

---

## 🔗 Important URLs

### Development
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Health: http://localhost:8000/api/health/

### Production (Update after deployment)
- Frontend: https://your-app.netlify.app
- Backend: https://your-app.onrender.com
- API Health: https://your-app.onrender.com/api/health/

---

## 📝 Environment Variables Reference

### Backend (.env)
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
GEMINI_API_KEY=your-gemini-key
FRONTEND_URL=https://your-app.netlify.app
```

### Frontend (.env.production)
```
VITE_API_URL=https://your-app.onrender.com/api
```

---

## 🚨 Common Issues

### Backend not responding
- Check Render logs
- Verify environment variables
- Ensure service is running (free tier spins down after 15 min)

### CORS errors
- Verify `FRONTEND_URL` matches exactly
- Check `ALLOWED_HOSTS` includes Render domain
- Ensure HTTPS is used in production

### Frontend can't connect to API
- Verify `VITE_API_URL` is set correctly
- Check browser console for errors
- Test backend health endpoint directly

---

## ✨ Tips

1. **Free Tier Limits**: Render free tier spins down after inactivity. First request may take 30-60 seconds.
2. **Environment Variables**: Double-check all environment variables are set correctly.
3. **HTTPS**: Both Netlify and Render provide automatic HTTPS.
4. **Logs**: Use Render dashboard to view backend logs for debugging.
5. **Build Time**: Initial deployment may take 5-10 minutes.
