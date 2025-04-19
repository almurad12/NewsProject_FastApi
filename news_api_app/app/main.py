# from fastapi import FastAPI
# from app.db.database import Base, engine
# from app.api.routes_news import router as news_router

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="News API")

# app.include_router(news_router)

from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes_news import router as news_router
from app.api.routes_auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="News project with authentication")
app.include_router(auth_router)
app.include_router(news_router)
