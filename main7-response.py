from fastapi import FastAPI, Header, Cookie, Body, File, UploadFile
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from starlette.responses import JSONResponse
from app.helper import generate_id
from pydantic import BaseModel
from enum import Enum
import uvicorn 

class Genre(str, Enum):
    action = "action"
    sci_fi = "sci-fi"
    romantic = "romantic"
    horror = "horror"
    drama = "drama"
    adult = "adult"

class MoviesObject(BaseModel):
    name : str = "Untitled"
    genre : Genre

app = FastAPI()

@app.post("/movies")
async def insert_movies(req_body : MoviesObject = Body(...), x_username : str = Header(...)):
    movie_id = generate_id()
    TSUTAYA_MOVIES.update({ movie_id : {"name" : req_body.name,
                                        "genre" : req_body.genre ,
                                        "created_by" : x_username}})
    return JSONResponse(content = {"message" : f"{req_body.name}, added to TSUTAYA store"}, status_code = 201)