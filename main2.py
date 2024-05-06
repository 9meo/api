from fastapi import FastAPI, Header, Cookie
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
import uvicorn 

app = FastAPI()

MOVIES_LIST = [{"name" : "TENET"}]

# @app.get("/movies")
# async def fetch_movies():
#     return {"data" : MOVIES_LIST}



# @app.get("/movies")
# async def fetch_movies(name : str = None):
#     return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['name'] == name]}


# @app.get("/movies")
# async def fetch_movies(name : str):
#     return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['name'] == name]}


@app.get("/movies")
async def fetch_movies(name : str = None):
    if name:
        return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['name'] == name]}

    return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES]}

