from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel 

class Item(BaseModel):
    id: int
    name: str
    item_type: Optional[str] = "a"
    total: int 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.get("/user/{user_id}")
# async def get_user_by_id(user_id: int):
#     return {"user_id": user_id}




@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int, type: Optional[str] = "normal"):
    return {"user_id": user_id, "type": type} 



@app.post("/item")
def create_item(item: Item):
    return item



