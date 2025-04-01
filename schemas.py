#  __________________
#  Import LIBRARIES
from pydantic import BaseModel, field_validator
from datetime import date
from enum import Enum
#  Import FILES
#  __________________


#  Import FILES
from data import BANDS
#  __________________


class GenreURLChoices(Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"


class GenreChoices(Enum):
    ROCK = "Rock"
    ELECTRONIC = "Electronic"
    METAL = "Metal"
    HIP_HOP = "Hip-hop"


class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []


#  - OLD -
# class BandBase(BaseModel):
#     name: str
#     genre: str
#     albums: list[Album] = []


# class Band(BaseModel):
#     #  "id": 1, "name": "The Kinks", "genre": "Rock"
#     id: int
#     name: str
#     genre: str
#     albums: list[Album] = []


class BandCreate(BandBase):
    @field_validator("genre", mode="before")
    # @classmethod
    def title_case_genre(cls, value) -> str:
        return value.title()


# class BandCreate(BandBase):
#     pass


class BandWithID(BandBase):
    id: int
