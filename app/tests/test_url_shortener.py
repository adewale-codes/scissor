from fastapi.testclient import TestClient
from main import app
from app.db import database

client = TestClient(app)

def test_create_url():
    response = client.post("/create_url/", json={"original_url": "https://www.example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "original_url" in data
    assert len(data["original_url"]) > 0

def test_get_url():
    response = client.get("/get_url/sample_short_url")
    assert response.status_code == 404  

def test_get_url_analytics():
    response = client.get("/get_url_analytics/sample_short_url")
    assert response.status_code == 404 

def test_get_link_history():
    response = client.get("/get_link_history/1")
    assert response.status_code == 404 
