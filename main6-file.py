from fastapi import FastAPI, Header, Cookie, Body, File, UploadFile
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from app.helper import generate_id
from pydantic import BaseModel
from enum import Enum
import uvicorn 

app = FastAPI()

@app.post("/member/profile")
async def insert_image_profile(data : UploadFile = File(...)):
    image = await data.read()
    return {"message" : f"{data.filename}, size {len(image)} bytes, updated to your profile"}