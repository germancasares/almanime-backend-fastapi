from sqlalchemy.orm import Session

from .entities.anime import Anime


def get_anime(db: Session, kitsu_id: int):
    return db.query(Anime).filter(Anime.kitsu_id == kitsu_id).first()
