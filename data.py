#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________

BANDS: list[dict] = [
    {"id": 1, "name": "The Kinks", "genre": "Rock"},
    {"id": 2, "name": "Aphex Twin", "genre": "Electronic"},
    {
        "id": 3,
        "name": "Black Sabbath",
        "genre": "Metal",
        "albums": [
            {"title": "Master of Reality", "release_date": "1971-07-21"},
            {"title": "elle", "release_date": "2971-11-11"},
        ],
    },
    {"id": 4, "name": "Wu-Tang Clan", "genre": "Hip-Hop"},
    {"id": 5, "name": "The Kinks", "genre": "Rock"},
    {"id": 6, "name": "Slowdive", "genre": "Shoegaze"},
]
