from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_get_services():
    response = client.get("/api/booking/services")
    assert response.status_code == 200
    assert "Scheduled" in response.json()
