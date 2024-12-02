from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Descubre Rincones que Cuentan Historias" in response.text

def test_generate_response_success():
    response = client.post("/generate-response/", json={"place": "Vienna"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_generate_response_empty_place():
    response = client.post("/generate-response/", json={"place": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "El lugar no puede estar vacío."

def test_search_history():
    response = client.get("/search-history/")
    assert response.status_code == 200
    assert "search_history" in response.json()
