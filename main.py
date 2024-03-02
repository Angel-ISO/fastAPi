from fastapi import FastAPI
from pydantic import BaseModel

import datetime

app = FastAPI()


""" con esto puedo personalizar aspectos que quiera en mi app
mientras se encuentra el servidor activo """

@app.on_event("startup")
async def startup_event():
    print('server started:', datetime.datetime.now())

@app.on_event("shutdown")
async def shutdown_event():
    print('server shutdown:', datetime.datetime.now())


# operaciones crud simples

data = []

class Book(BaseModel):
    id:int
    tittle:str
    author:str
    publisher:str


@app.post("/post")
def add_book(book: Book):
    data.append(book.dict())
    return data

@app.get("/list")
def get_book():
    return data


@app.delete("/book/{id}")
def delete_book(id: int):
    data.pop(id-1)
    return data
