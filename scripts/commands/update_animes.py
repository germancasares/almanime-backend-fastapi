from datetime import datetime
from typing import Dict, List

from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from app.models.enums import AnimeStatus, Season
from app.repositories.anime import Anime, create_anime, get_anime, update_anime
from app.repositories.database import SessionLocal
from app.utils import get_season_from_date

KITSU_API = "https://kitsu.io/api/edge"
MAX_PER_PAGE = 20


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def run(database: Session = Depends(get_db)):
    date = datetime.utcnow()
    year = date.year
    season = get_season_from_date(date)

    raw_animes = get_raw_animes(year, season)
    animes = [map_anime(anime) for anime in raw_animes]
    filtered_animes = [
        anime
        for anime in animes
        if
        anime is not None and
        anime.status is not AnimeStatus.TO_BE_ANNOUNCED and
        anime.season is season
    ]

    for anime in filtered_animes:
        db_anime = get_anime(database, anime.kitsu_id)
        if db_anime:
            update_anime(database, anime)
        else:
            create_anime(database, anime)


def get_raw_animes(year: int, season: Season) -> List:
    url = (
        f'{KITSU_API}/anime?'
        f'filter[seasonYear]={year}&'
        f'filter[season]={season.value.lower()}&'
        f'page[limit]={MAX_PER_PAGE}'
    )

    raw_animes = []

    while url:
        response = get(url).json()

        raw_animes.extend(response['data'])

        url = response.get('links', {}).get('next')

    return raw_animes


def map_anime(raw_anime: Dict) -> Anime:
    anime = raw_anime['attributes']

    if anime['startDate'] is None:
        return None

    start_date = datetime.strptime(anime['startDate'], "%Y-%m-%d")
    end_date = datetime.strptime(
        anime['endDate'],
        "%Y-%m-%d"
    ) if 'endDate' in anime and anime['endDate'] else None

    return Anime(
        kitsu_id=raw_anime['id'],
        slug=anime['slug'],
        name=anime['canonicalTitle'],

        season=get_season_from_date(start_date),
        status=anime['status'],
        start_date=start_date,
        end_date=end_date,
        synopsis=anime['synopsis'],
        cover_image=anime['coverImage']['original'] if anime['coverImage'] else None,
        poster_image=anime['posterImage']['original'] if anime['posterImage'] else None,
    )
