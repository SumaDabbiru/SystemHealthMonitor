from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_healthcheck_json():
    dag_file = os.path.join(os.path.dirname(__file__), '..', 'dag_graph.json')
    response = client.get(f"/healthcheck?dag_file={dag_file}")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "components" in response.json()
