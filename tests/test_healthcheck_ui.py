from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthcheck_ui():
    response = client.get("/healthcheckui/")
    assert response.status_code == 200
