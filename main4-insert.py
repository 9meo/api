from fastapi import FastAPI, Header, Cookie, Body
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from app.helper import generate_id
from pydantic import BaseModel
import uvicorn 

class MoviesObject(BaseModel):
    name : str 
    genre : str

app = FastAPI()

@app.post("/movies")
async def insert_movies(req_body : MoviesObject = Body(...), x_username : str = Header(...)):
    movie_id = generate_id()
    TSUTAYA_MOVIES.update({ movie_id : {"name" : req_body.name,
                                        "genre" : req_body.genre ,
                                        "created_by" : x_username}})
    return {"message" : f"{req_body.name}, added to TSUTAYA store"}
