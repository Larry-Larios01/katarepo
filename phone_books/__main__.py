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
from psycopg2.extras import RealDictCursor
from starlette.requests import Request

load_dotenv(verbose=True)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)





class Contact(TypedDict):
    name:str
    email: str
    phone: str

class GetResult():
    Contacts: list[Contact]



def from_req_get_user(request: Request)-> int:
    pass






async def get_user(request):
    params = from_req(request)
    result = await get_user_handler(params)
    return to_res(result)






routes = [
    #Route("/contacts/", endpoint=list_notes, methods=["GET"]),
    Route("/contacts", endpoint=insert_user, methods=["POST"]),
    Route("/contacts/{id}", endpoint=get_user, methods=["GET"]),
    #Route("/contacts/{id}", endpoint=list_notes, methods=["PATCH"]),
    #Route("/contacts/{id}", endpoint=list_notes, methods=["DELETE"]),
]



app = Starlette(
    routes=routes,
)



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)