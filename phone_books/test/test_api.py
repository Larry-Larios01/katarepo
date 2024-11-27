from phone_books.__main__ import get_user_handler
import pytest

#given_we_need_a_specific_contact_when_we_seek_it_for_id_it_return_us_the_contact
@pytest.mark.asyncio
async def test_get_contact_by_id():
    #given
    id = 1
    #when
    contact = await get_user_handler(id)
    #then
    assert contact["id"] == 1 
    assert contact["name"] == 'John Doe'
    assert contact["email"] == 'john.doe1@example.com'
    assert contact["phone"] == '555-0001'


  
    