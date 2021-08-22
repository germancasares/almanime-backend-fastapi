from typing import Optional

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from .repositories.anime import get_anime
from .repositories.database import SessionLocal
from .repositories.entities.anime import Anime

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/anime")
async def yo_anime(db: Session = Depends(get_db)):
    return get_anime(db=db, kitsu_id=10)


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "query": query}
