from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import DateTime, Enum

from app.models.enums import AnimeStatus, Season

from .base import Base


class Anime(Base):
    __tablename__ = "animes"

    kitsu_id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, unique=True, nullable=False)

    season = Column(Enum(Season), nullable=False)
    status = Column(Enum(AnimeStatus), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    synopsis = Column(String)
    cover_image = Column(String)
    poster_image = Column(String)


def get_anime(database: Session, kitsu_id: int) -> Anime:
    return next(iter(database.query(Anime).filter(Anime.kitsu_id == kitsu_id)), None)


def create_anime(database: Session, anime: Anime):
    database.add(anime)
    database.commit()


def update_anime(database: Session, anime: Anime):
    db_anime = database.query(Anime).get(anime.id)

    for key, value in anime.__dict__.items():
        setattr(db_anime, key, value)

    database.commit()
