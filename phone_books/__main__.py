import contextlib
import psycopg2
import databases
import sqlalchemy
from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route
from dotenv import load_dotenv
import os
import uvicorn
from typing import TypedDict
from http.client import HTTPResponse

load_dotenv(verbose=True)
DATABASE_URL = os.getenv("DATABASE_URL")




metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("phone", sqlalchemy.String),
)

database = databases.Database(DATABASE_URL)

@contextlib.asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.disconnect()


class insert_user_param(TypedDict):
    name:str
    email: str
    phone: str


def from_req(request) -> insert_user_param:
    data = request.json()
    return insert_user_param(name=data["name"], email=data["email"], phone=data["phone"])

async def insert_user_handler(params: insert_user_param):
    query = notes.insert().values(name=params["name"], email=params["email"], phone=params["phone"])
    await database.execute(query)
    return params

def to_res(user: insert_user_param) -> JSONResponse:
    return JSONResponse({"name": user["name"], "email": user["email"], "phone": user["phone"]})

async def insert_user(request):
    params = from_req(request)
    result = await get_user_handler(params)
    return to_res(result)


def from_req(request) -> int:
    data = request.path_params.get("id")
    return data

async def get_user_handler(params: int):
    query = notes.select().where(notes.c.id == params)
    contact = await database.fetch_one(query)
    return contact

def to_res(user) -> JSONResponse:
    return JSONResponse(dict(user))

async def list_notes(request):
    
    note_id = request.path_params.get("id")
    
    note_id = int(note_id)
    
    query = notes.select().where(notes.c.id == note_id)
    result = await database.fetch_one(query)


    content = {
        "id": result["id"],
        "name": result["name"],
        "email": result["email"],
        "phone": result["phone"],

    }
    return JSONResponse(content)





async def get_user(request):
    params = from_req(request)
    result = await get_user_handler(params)
    return to_res(result)






routes = [
    #Route("/contacts/", endpoint=list_notes, methods=["GET"]),
    Route("/contacts", endpoint=insert_user, methods=["POST"]),
    Route("/contacts/{id}", endpoint=list_notes, methods=["GET"]),
    #Route("/contacts/{id}", endpoint=list_notes, methods=["PATCH"]),
    #Route("/contacts/{id}", endpoint=list_notes, methods=["DELETE"]),
]



app = Starlette(
    routes=routes,
    lifespan=lifespan,
)



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)