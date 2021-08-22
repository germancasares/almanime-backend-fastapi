from datetime import datetime
from typing import Optional

from .base import Base
from .enums import AnimeStatus, Season


class Anime(Base):
    kitsu_id: int
    slug: str
    name: str

    season: Season
    status: AnimeStatus
    start_date: datetime
    end_date: Optional[datetime] = None
    synopsis: Optional[str] = None
    cover_image: Optional[str] = None
    poster_image: Optional[str] = None

    class Config:
        orm_mode = True
