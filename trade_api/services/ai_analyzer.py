import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

MODEL_NAME = "models/gemini-1.5-flash"


def format_prompt(sector: str, data: str) -> str:
    return f"""
Using the news and data provided below, generate a markdown report on the Indian {sector} sector with:
- Current Trends
- News Highlights
- Trade Opportunities

Respond only in markdown.

Data:
{data}
"""



async def analyze_with_gemini(sector: str, data: str) -> str:
    prompt = format_prompt(sector, data)

    model = genai.GenerativeModel(model_name=MODEL_NAME)

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"
