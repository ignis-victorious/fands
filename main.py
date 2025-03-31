#  __________________
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException
from enum import Enum

#  Import FILES
from data import BANDS
#  __________________


class GenreURLChoices(Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS


@app.get("/bands/{band_id}")
# @app.get("/bands/{band_id}", status_code=206)
async def band(band_id: int) -> dict | None:
    band: dict | None = next((b for b in BANDS if b["id"] == band_id), None)
    if band is None:
        #  Status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


@app.get("/bands/genre/{genre}")
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    # async def bands_for_genre(genre: str) -> list[dict]:
    return [b for b in BANDS if b["genre"].lower() == genre.value]
    # return [b for b in BANDS if b["genre"].lower() == genre.lower()]


# def main():
#     print("Hello from fands!")

# if __name__ == "__main__":
#     main()


#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________
