# Real Estate Analysis Chatbot

A full-stack web application that analyzes real estate data using a chat interface. Built with React, Django, and AI-powered insights.

## 🌐 Live Demo

- **Frontend**: https://real-estate-chatbot-grp.netlify.app/
- **Backend API**: https://real-estate-chatbot-api-isrj.onrender.com

## ✨ Features

- **Natural Language Queries**: Ask questions like "Analyze Wakad" or "Compare Aundh and Hinjewadi"
- **AI-Powered Summaries**: Smart insights generated using Google Gemini AI
- **Data Visualization**: Interactive charts showing price and demand trends
- **Detailed Data**: Filtered data tables based on your queries
- **Real-time Analysis**: Instant processing of real estate data from Excel

## 🛠️ Tech Stack

- **Frontend**: React, Vite, Bootstrap, Recharts, Axios
- **Backend**: Django, Django REST Framework, Pandas, OpenPyXL
- **AI**: Google Gemini API for intelligent summaries
- **Deployment**: Netlify (Frontend) + Render (Backend)

## 📋 Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- Google Gemini API Key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`.

## 💬 Sample Queries

Try these queries in the chat interface:

1. **Single Area Analysis**:
   - "Give me analysis of Wakad"
   - "Tell me about Akurdi"
   - "Analyze Aundh real estate market"

2. **Comparative Analysis**:
   - "Compare Ambegaon Budruk and Aundh"
   - "Show demand trends for Wakad vs Akurdi"
   - "Compare price growth in Wakad and Aundh"

3. **Trend Analysis**:
   - "Show price growth for Akurdi over the last 3 years"
   - "How has the demand changed in Aundh?"
   - "What are the sales trends in Wakad?"

## 📁 Project Structure

```
real-estate-chatbot/
├── backend/                # Django Backend
│   ├── analysis/           # Analysis App
│   ├── data/               # Excel Data
│   ├── realestate_api/     # Project Settings
│   └── manage.py
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── components/     # React Components
│   │   ├── services/       # API Services
│   │   └── App.jsx
│   └── package.json
└── DEPLOYMENT.md          # Deployment Guide
```

## 🚀 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy

**Backend (Render)**:
1. Push code to GitHub
2. Create new Web Service on Render
3. Set environment variables (GEMINI_API_KEY, etc.)
4. Deploy!

**Frontend (Netlify)**:
1. Connect GitHub repository
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Add environment variable: `VITE_API_URL`
5. Deploy!

## 📊 Data

The application uses real estate data for Pune areas including:
- **Wakad**: High-growth IT hub area
- **Akurdi**: Established residential locality
- **Aundh**: Premium residential area
- **Ambegaon Budruk**: Emerging residential zone

Data includes sales transactions, pricing trends, demand metrics, and property types from 2020-2024.

## 🎯 Assignment Features

This project fulfills all requirements of the Sigmavalue Full Stack Developer Assignment:

✅ **Backend (Django + Python)**
- Excel data parsing and filtering
- REST API endpoints
- AI-generated summaries (Google Gemini)
- Chart data generation
- Filtered table data

✅ **Frontend (React + Bootstrap)**
- Chat-style query interface
- Text-based summary display
- Interactive charts (Recharts)
- Filtered data tables
- Responsive design

✅ **Bonus Features**
- ✅ LLM Integration (Google Gemini API)
- ✅ Deployment ready (Netlify + Render)
- 📹 Demo video (to be recorded)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.
