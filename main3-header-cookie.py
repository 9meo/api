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

@app.get("/member")
async def check_member(x_username : str = Header(...)):
    if [TSUTAYA_MEMBER[member] for member in TSUTAYA_MEMBER if TSUTAYA_MEMBER[member]['name'] == x_username]:
        return {"message" : f"{x_username} is member of TSUTAYA store"}
    else: 
        return {"message" : "Not found"}
    
@app.get("/member/token")
async def check_token(x_token : str = Cookie(None)):
    if x_token in TSUTAYA_MEMBER.keys():
        return {"message" : f"{TSUTAYA_MEMBER[x_token]['name']} is member of TSUTAYA store and Token is valid"}
    else: 
        return {"message" : "Invalid token"}