from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    description: str | None = None
    url: str
    source: str

class NewsCreate(NewsBase):
    pass

class NewsInDB(NewsBase):
    id: int

    class Config:
        orm_mode = True
