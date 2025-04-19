from sqlalchemy.orm import Session
from app.models.news import News
from app.schemas.news import NewsCreate

def save_news(db: Session, news_data: list[NewsCreate]):
    news_objects = [
        News(
            title=item.title,
            description=item.description,
            url=item.url,
            source=item.source
        )
        for item in news_data
    ]
    db.add_all(news_objects)
    db.commit()
    return news_objects

