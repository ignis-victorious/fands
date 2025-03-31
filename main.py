#  __________________
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#  Import FILES
from data import BANDS
from schemas import GenreURLChoices, Band
#  __________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def bands() -> list[Band]:
    # async def bands() -> list[dict]:
    return [Band(**b) for b in BANDS]
    # return BANDS


@app.get("/bands/{band_id}")
async def band(band_id: int) -> Band:
    band: Band | None = next((Band(**b) for b in BANDS if b["id"] == band_id), None)
    if band is None:
        #  Sttus code 404
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
