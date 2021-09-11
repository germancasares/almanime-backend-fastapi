from datetime import datetime

from app.models.enums import Season

Y = 2000  # dummy leap year to allow input X-02-29 (leap day)
seasons = [
    (Season.WINTER, (datetime(Y,  1,  1),  datetime(Y,  3, 20))),
    (Season.SPRING, (datetime(Y,  3, 21),  datetime(Y,  6, 20))),
    (Season.SUMMER, (datetime(Y,  6, 21),  datetime(Y,  9, 22))),
    (Season.FALL,   (datetime(Y,  9, 23),  datetime(Y, 12, 20))),
    (Season.WINTER, (datetime(Y, 12, 21),  datetime(Y, 12, 31)))
]


def get_season_from_date(date: datetime):
    date = date.replace(year=Y)
    return next(
        season
        for season, (start, end) in seasons
        if start <= date <= end
    )
