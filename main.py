#  __________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  __________________


app = FastAPI()


@app.get("/")
async def index() -> dict[str, str]:
    return {"This is": "root"}


@app.get("/about")
async def about() -> str:
    return "What a lovely day"


# def main():
#     print("Hello from fands!")
# if __name__ == "__main__":
#     main()


#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________
