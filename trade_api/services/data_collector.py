import httpx
from bs4 import BeautifulSoup

async def fetch_sector_news(sector: str) -> str:
    query = f"{sector} sector India market news"
    url = f"https://html.duckduckgo.com/html/?q={query}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        results = soup.select(".result__snippet")

    return "\n".join([r.get_text() for r in results][:10])
