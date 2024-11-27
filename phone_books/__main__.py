
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from dotenv import load_dotenv
import os
import uvicorn
from typing import TypedDict
from starlette.requests import Request
import psycopg
from psycopg.rows import dict_row

load_dotenv(verbose=True)
DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await psycopg.AsyncConnection.connect(DATABASE_URL, row_factory=dict_row)





class Contact(TypedDict):
    id: int
    name:str
    email: str
    phone: str
        
class GetResult():
    Contacts: list[Contact]



def from_req_get_user(request: Request)-> int:
    user_id = request.path_params.get("id")
    return int(user_id)


async def get_user_handler(params: int)-> Contact:
    conn = await get_connection()
    async with conn.transaction():
            restult = await conn.execute(f"SELECT * FROM users WHERE id = {params}")
            user = await restult.fetchone()
            contact = Contact(id=user["id"],name=user["name"], email=user["email"], phone=user["phone"])
    await conn.close()
    return contact


def to_res_get_user(contact: Contact)-> JSONResponse:
     return JSONResponse(contact)



async def get_user(request: Request):
    params = from_req_get_user(request)
    result = await get_user_handler(params)
    return to_res_get_user(result)







def from_req_insert_user(request: Request)-> Contact:
    data = request.json()
    contact = Contact(name=data["name"], email=data["email"], phone=data["phone"])
    return contact

async def insert_user_handler(params: Contact)-> int:
    conn = await get_connection()
    async with conn.transaction():
            result = await conn.execute(
                "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s) RETURNING id, name, email, phone",
                (params["name"], params["email"], params["phone"])  
                    )
            user = await result.fetchone()
            contact = Contact(id=user["id"],name=user['name'], email=user['email'], phone=user["phone"])
    await conn.close()
            
    return contact


def to_res_insert_user(user: Contact)-> JSONResponse:
     return JSONResponse({
        "id": f"{user["id"]}",
        "message": "was succesful inserted"
    })

async def insert_user(request: Request):
    params = from_req_get_user(request)
    result = await get_user_handler(params)
    return to_res_get_user(result)







def from_req_partial_update(request: Request)-> Contact:
    data = request.json()
    contact = Contact(name=data["name"], email=data["email"], phone=data["phone"])
    return contact


async def partial_update_handler(params: Contact)-> int:
    conn = await get_connection()
    async with conn.transaction():
            result = await conn.execute(
                "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s) RETURNING id, name, email, phone",
                (params["name"], params["email"], params["phone"])  
                    )
            user = await result.fetchone()
            contact = Contact(id=user["id"],name=user['name'], email=user['email'], phone=user["phone"])
    await conn.close()
            
    return contact


def to_res_partial_update(user: Contact)-> JSONResponse:
     return JSONResponse({
        "id": f"{user["id"]}",
        "message": "was succesful inserted"
    })

async def partial_update(request: Request):
    params = from_req_partial_update(request)
    result = await partial_update_handler(params)
    return to_res_partial_update(result)






routes = [
    #Route("/contacts/", endpoint=list_notes, methods=["GET"]),
    Route("/contacts", endpoint=insert_user, methods=["POST"]),
    Route("/contacts/{id}", endpoint=get_user, methods=["GET"]),
    Route("/contacts/{id}", endpoint=partial_update, methods=["PATCH"]),
    #Route("/contacts/{id}", endpoint=list_notes, methods=["DELETE"]),
]



app = Starlette(
    routes=routes
)



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)