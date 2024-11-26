import pytest
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
from phone_books.__main__ import app




def test_insert_user(setup_database):
    # Crear cliente de prueba
    client = TestClient(app)

    # Datos de ejemplo para la prueba
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "555-1234"
    }

    # Realizar la solicitud POST
    response = client.post("/contacts", json=user_data)

    # Verificar que el estado de la respuesta sea 200
    assert response.status_code == 200
