from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def get_all_news():
    response = client.get(f"/news/")
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] == "ok"

def test_headlines_by_source():
    source_id = "bbc-news"
    response = client.get(f"/news/headlines/source/{source_id}")
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] == "ok"
    assert "articles" in json_data
    assert isinstance(json_data["articles"], list)


def test_headlines_with_filters():
    params = {
        "source":"us"
    }
    response = client.get("/news/headlines/filter", params=params)
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] == "ok"
    assert "articles" in json_data
    assert isinstance(json_data["articles"], list)
