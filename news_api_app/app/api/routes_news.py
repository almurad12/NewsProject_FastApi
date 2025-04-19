from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.database import get_db
from app.crud import news as news_crud
from app.services.newsapi_service import fetch_news_from_api
from app.schemas.news import NewsCreate
from fastapi.responses import JSONResponse
router = APIRouter()

@router.get("/news")
async def get_all_news(skip: int = 0, limit: int = 10, q: str = "bitcoin"):
    data = await fetch_news_from_api("everything", {
        "q": q,
        "pageSize": limit,
        "page": (skip // limit) + 1
    })
    return data

@router.post("/news/save-latest")
async def save_latest_news(db: Session = Depends(get_db)):
    data = await fetch_news_from_api("top-headlines", {"language": "en"})
    # print(data)
    articles = data.get("articles", [])[:3]
    print(articles)
    news_data = [NewsCreate(
        title=a.get("title"),
        description=a.get("description"),
        url=a.get("url"),
        source=a.get("source", {}).get("name")
    ) for a in articles]
    try:
        saved = news_crud.save_news(db, news_data)
    except Exception as e:
        print(f"Error saving news: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@router.get("/top-headlines/country/{country_code}")
async def headlines_by_country(country_code: str):
    return await fetch_news_from_api("top-headlines", {"country": country_code})

@router.get("/news/headlines/source/{source_id}")
async def headlines_by_source(source_id: str):
    return await fetch_news_from_api("top-headlines", {"sources": source_id})

@router.get("/news/headlines/filter")
async def filter_headlines(country: str = Query(None), source: str = Query(None)):
    params = {}
    if country:
        params["country"] = country
    if source:
        params["sources"] = source
    return await fetch_news_from_api("top-headlines", params)
