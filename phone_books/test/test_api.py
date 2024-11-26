import pytest
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
from phone_books.__main__ import app





def test_list_note_by_id():
    client = TestClient(app)
    response = client.get("/1")
    assert response.status_code == 200
