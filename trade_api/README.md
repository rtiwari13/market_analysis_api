# 📊 Market Analysis API (India Sectors)

This FastAPI application analyzes Indian market sectors and provides structured trade opportunity insights in markdown format. It uses real-time market news and Google Gemini AI to generate reports.

---

## 🚀 Features

* AI-powered market insights via Google Gemini  
* Live data collection using DuckDuckGo scraping  
* Structured markdown report generation  
* JWT Authentication  
* User registration & login  
* Rate limiting per user/session  
* Swagger (OpenAPI) interactive documentation

---
## 🏗️ Project Structure
```
trade_api/
├── main.py # FastAPI app entry
├── api/
│ ├── endpoints.py # /analyze/{sector} route
│ └── auth_routes.py # /register and /login
├── auth/
│ ├── jwt_handler.py # JWT encode/decode helpers
│ └── dependencies.py # Auth dependencies
├── services/
│ ├── data_collector.py # Web scraping news
│ ├── ai_analyzer.py # Gemini API analysis
│ └── report_generator.py # Markdown report formatting
├── utils/
│ ├── validators.py # Sector validation
│ └── user_store.py # In-memory user storage
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/rtiwari13/market_analysis_api.git
cd market-analysis-api
cd trade_api

```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key to .env
```bash
GEMINI_API_KEY = api_keye_here
```

### 5. run the server 
```bash
uvicorn main:app --reload
```

### API Usage
🔐 Register a new user
```
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}
```

🔐 Login
```
POST /login
Content-Type: application/json

{"username": "testuser",
  "password": "testpass"
}
```
Returns:

```
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 📈 Analyze Market Sector

```bash
GET /analyze/technology
Authorization: Bearer <JWT_TOKEN>
```
## Example response (markdown):

# Market Analysis: Technology Sector (India)

## 📈 Current Trends
...

## 📰 News Highlights
...

## 💡 Trade Opportunities
...

*Last Updated: DATE*

### 📚 API Documentation
Interactive docs available at:

```
http://127.0.0.1:8000/docs
```

### 🚧 Notes

* Supported sectors: pharmaceuticals, technology, agriculture, finance, energy

* In-memory storage only (no database)

* Rate limited to 5 requests/min per user

