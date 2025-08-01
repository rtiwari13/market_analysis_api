from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from auth.dependencies import get_current_user
from services.data_collector import fetch_sector_news
from services.ai_analyzer import analyze_with_gemini
from services.report_generator import generate_markdown
from utils.validators import validate_sector
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.get("/analyze/{sector}", response_class=PlainTextResponse)
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,  # REQUIRED for slowapi to work
    sector: str,
    user=Depends(get_current_user)
):
    validate_sector(sector)
    try:
        news_text = await fetch_sector_news(sector)
        ai_response = await analyze_with_gemini(sector, news_text)
        markdown = generate_markdown(sector, ai_response)
        return markdown
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
