import contextlib

import databases
import sqlalchemy
from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route
from dotenv import load_dotenv
import os

load_dotenv("prod.env")
host = os.getenv("DB_HOST")
DATABASE_URL = host

print(DATABASE_URL)


@contextlib.asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.disconnect()

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

async def insert_user(request):
    data = await request.json()
    query = notes.insert().values(
       name=data["name"],
       email=data["email"],
       phone=data["phone"]
    )
    await database.execute(query)
    return JSONResponse({
       "name": data["name"],
       "email": data["email"],
       "phone": data["phone"],
    })


routes = [
    Route("/contacts/", endpoint=list_notes, methods=["GET"]),
    Route("/contacts", endpoint=insert_user, methods=["POST"]),
    Route("/contacts/{id}", endpoint=list_notes, methods=["GET"]),
    Route("/contacts/{id}", endpoint=list_notes, methods=["PATCH"]),
    Route("/contacts/{id}", endpoint=list_notes, methods=["DELETE"]),
]



app = Starlette(
    routes=routes,
    lifespan=lifespan,
)