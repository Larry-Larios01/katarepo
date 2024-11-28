
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
from psycopg import AsyncRawCursor
load_dotenv(verbose=True)
DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await psycopg.AsyncConnection.connect(DATABASE_URL, row_factory=dict_row, cursor_factory= AsyncRawCursor)





class Contact(TypedDict):
    id: int
    name:str
    email: str
    phone: str
        
class GetResult():
    contacts: list[Contact]



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
    async with conn.cursor() as c:
            result = await c.execute(
                "INSERT INTO users (name, email, phone) VALUES ($1, $2, $3) RETURNING id, name, email, phone",
                [params["name"], params["email"], params["phone"]]
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
    user_id = request.path_params.get("id")
    dic_to_update = {"id":f"{user_id}"}
    data = request.json()
    allowed_parameters = ("name", "email", "phone")
    for key,value in data.items():
        if key in allowed_parameters:
             dic_to_update[key] = value
        
    return dic_to_update

async def partial_update_handler(params: dict)-> int:
    conn = await get_connection()
    id = params.pop("id", None)
    set_keys = []
    set_values = []
    for i, (key, value) in enumerate(params.items(), start=1):
        set_keys.append(f"{key} = ${i}")
        set_values.append(value)

    set_values.append(id)
    set_keys_as_text = ", ".join(set_keys)


                
    async with conn.cursor() as c:
            
            
            result = await c.execute(
            f"""
            UPDATE users
            SET {set_keys_as_text}
            WHERE id = ${len(set_values)}
            RETURNING id, name, email, phone
            """, set_values
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














def from_req_delete_user(request: Request)-> int:
    user_id = request.path_params.get("id")
    return int(user_id)


async def delete_user_handler(params: int)-> Contact:
    contact = await get_user_handler(params)
    conn = await get_connection()
    async with conn.cursor() as c:
        

            await c.execute(
            """
            DELETE FROM users
            WHERE id = $1
            """,
            [params]  )
        
            
    await conn.close()
    await c.close()
    return contact


def to_res_delete_user(params:Contact)-> JSONResponse:
    message = {"message": f"the user {params['name']}, user id {params["id"]} was succesfully deleted"}
    return JSONResponse(message)



async def delete_user(request: Request):
    params = from_req_delete_user(request)
    result = await delete_user_handler(params)
    return to_res_delete_user(result)
























def from_req_filter_contacts(request: Request)-> set:
    filters = request.query_params.get("filter", {})
    name_filter = filters.get("name")
    email_filter = filters.get("email")
    phone_filter = filters.get("phone")
    valid_filter = []
    if name_filter:
        valid_filter.append(name_filter)
    if email_filter:
        valid_filter.append(email_filter)
    if phone_filter:
        valid_filter.append(phone_filter)

    return valid_filter
    


    


async def filter_contacts_handler(params: list)-> GetResult:
    contact_list = Contact()
    list_contacts = []
    get_result = GetResult()
    conn = await get_connection()
    if not params:
         async with conn.cursor() as c:
            
            
            result = await c.execute(
            """
            select * from users
            """
        )
            contacts = await c.fetchall()
           
            for contact in contacts:
                contact_list["id"] = contact["id"]
                contact_list["name"] = contact["name"]
                contact_list["email"] = contact["email"]
                contact_list["phone"] = contact["phone"]
                list_contacts.append(contact_list)

            get_result.contacts = list_contacts
            return get_result.contacts

           


def to_res_filter_contacts(user: Contact)-> JSONResponse:
     return JSONResponse({
        "id": f"{user["id"]}",
        "message": "was succesful inserted"
    })

async def filter_contacts(request: Request):
    params = from_req_filter_contacts(request)
    result = await filter_contacts_handler(params)
    return to_res_filter_contacts(result)



routes = [
    Route("/contacts/", endpoint=filter_contacts, methods=["GET"]),
    Route("/contacts", endpoint=insert_user, methods=["POST"]),
    Route("/contacts/{id}", endpoint=get_user, methods=["GET"]),
    Route("/contacts/{id}", endpoint=partial_update, methods=["PATCH"]),
    Route("/contacts/{id}", endpoint=delete_user, methods=["DELETE"]),
]



app = Starlette(
    routes=routes
)



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)