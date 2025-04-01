#  __________________
#  Import LIBRARIES
from typing import Any
from fastapi import FastAPI, HTTPException

#  Import FILES
from data import BANDS
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID
#  __________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None, has_albums: bool = False
) -> list[BandWithID]:
    band_list: list[BandWithID] = [BandWithID(**b) for b in BANDS]

    if genre:
        band_list = [b for b in band_list if b.genre.value.lower() == genre.value]
        # band_list = [b for b in band_list if b.genre.lower() == genre.value]
        # return [Band(**b) for b in BANDS if b["genre"].lower() == genre.value]
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0]
    return band_list


@app.get("/bands/{band_id}")
async def band(band_id: int) -> BandWithID:
    band: BandWithID | None = next(
        (BandWithID(**b) for b in BANDS if b["id"] == band_id), None
    )
    if band is None:
        #  Sttus code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


@app.post("/bands")
async def create_band(band_data: BandCreate) -> dict[str, Any]:
    id: int = BANDS[-1]["id"] + 1
    band: dict[str, Any] = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band


# def main():
#     print("Hello from fands!")

# if __name__ == "__main__":
#     main()


#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________
