import httpx
from app.core.config import settings
from sqlalchemy.orm import Session
from app.schemas.news import NewsCreate
from app.crud.news import save_news

async def fetch_news_from_api(endpoint: str, params: dict):
    async with httpx.AsyncClient() as client:
        params["apiKey"] = settings.NEWSAPI_KEY,
        response = await client.get(f"{settings.NEWSAPI_BASE_URL}/{endpoint}", params=params)
        
        response.raise_for_status()
        return response.json()


async def fetch_and_save_latest_news(db: Session):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.NEWSAPI_BASE_URL}/top-headlines", params={
            "apiKey": settings.NEWSAPI_KEY,
            "language": "en"
        })

    response.raise_for_status()
    data = response.json()
    articles = data.get("articles", [])[:3]

    saved_news = []

    for article in articles:
        news_data = NewsCreate(
            title=article.get("title"),
            description=article.get("description"),
            url=article.get("url"),
            source=article.get("source", {}).get("name")
        )
        saved = save_news(db, news_data)
        saved_news.append(saved)

    return saved_news
