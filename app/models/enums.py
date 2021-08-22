from enum import Enum


class Season(Enum):
    WINTER = "Winter"
    SPRING = "Spring"
    SUMMER = "Summer"
    FALL = "Fall"


class AnimeStatus(Enum):
    TO_BE_ANNOUNCED = "Tba"
    UNRELEASED = "Unreleased"
    UPCOMING = "Upcoming"
    CURRENT = "Current"
    FINISHED = "Finished"
