from phone_books.__main__ import get_user_handler

def test_get_contact_by_id():
    contact = get_user_handler(1)
    assert contact["id"] == 1 and contact["phone"]== '555-0001'
    