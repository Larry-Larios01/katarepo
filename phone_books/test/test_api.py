from phone_books.__main__ import delete_user_handler,get_user_handler, Contact, insert_user_handler, partial_update_handler
import pytest

#given_we_need_a_specific_contact_when_we_seek_it_for_id_it_then__return_us_the_contact
@pytest.mark.asyncio
async def test_given_we_need_a_specific_contact_when_we_seek_it_for_id_it_then__return_us_the_contact():
    #given
    id = 1
    #when
    contact = await get_user_handler(id)
    #then
    assert contact["id"] == 1 
    assert contact["name"] == 'John Doe'
    assert contact["email"] == 'john.doe1@example.com'
    assert contact["phone"] == '555-0001'

#given_we_need_insert_a_specific_contact_when_we_insert_then_it_return_us_the_contact
@pytest.mark.asyncio
async def test_given_we_need_insert_a_specific_contact_when_we_insert_then_it_return_us_the_contact():
    #given
    contact = Contact(name="larry", email="larioslarry8@gmail.com", phone="76125113")
    #when
    contact = await insert_user_handler(contact)
    #then
    assert contact["name"] == 'larry'
    assert contact["email"] == 'larioslarry8@gmail.com'
    assert contact["phone"] == '76125113'


@pytest.mark.asyncio
async def test_given_we_need_to_delete_an_item_when_we_delete_it_then_return_the_id_of_the_user_deleted():
   #given
    contact_id = 3
    #when
    result =  await delete_user_handler(3)
    #then
    assert result["id"] == contact_id


@pytest.mark.asyncio
async def test_given_we_need_to_udate_specific_part_of_the_item_whe_we_update_it_the_atributes_change():
   #given
    dictionary = {"id": 1, "name": "larry"}
    #when
    result =  await partial_update_handler(dictionary)
    #then
    assert result["id"] == 1
    assert result["name"] == "larry"
    





  
    