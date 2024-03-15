from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
import app.models

client = TestClient(app)


def test_get_admins():
    response = client.get("/admins/")
    assert response.status_code == 200
    assert response.json() == []