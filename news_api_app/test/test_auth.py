# tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={
       "username": "test8",
        "email": "test8@gmail.com",
        "full_name": "test8",
        "disabled": False,
        "password": "test8"
    })
    print("RESPONSE:", response.status_code, response.json())  # 👈 Add this for debug

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "test8"


def test_login_user():
    response = client.post("/login", data={
        "username": "test8",
        "password": "test8"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
