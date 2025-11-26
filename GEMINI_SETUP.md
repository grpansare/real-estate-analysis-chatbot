# Google Gemini Setup Instructions

## Quick Start

### 1. Get Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### 2. Configure Environment
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a `.env` file (copy from `.env.example`):
   ```bash
   copy .env.example .env
   ```

3. Open `.env` and replace `your_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=AIzaSy...your_actual_key_here
   ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python manage.py runserver
```

## How It Works
- When you ask a question, the chatbot sends your query + filtered data to Gemini
- Gemini analyzes the data and generates intelligent insights
- If the API fails or no key is provided, it falls back to rule-based summaries

## Testing
Try queries like:
- "What's the investment potential in Wakad?"
- "Compare Aundh and Hinjewadi for first-time buyers"
- "Which area has the best price growth?"
