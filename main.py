#  __________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  __________________


app = FastAPI()


@app.get('/')
async def root():
    return {'This is':'Root'} 






# def main():
#     print("Hello from fands!")
# if __name__ == "__main__":
#     main()


#  __________________
#  Import LIBRARIES
#  Import FILES
#  __________________