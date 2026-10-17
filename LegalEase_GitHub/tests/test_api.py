from fastapi.testclient import TestClient
from legalEaseAPI.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_generate_demo_or_ai():
    response = client.post(
        "/generate",
        json={
            "document_type": "Freelance Work Contract",
            "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
            "terms": "Payment within 30 days; Confidentiality must be maintained",
            "dates": "April 15, 2025",
        },
    )
    assert response.status_code == 200
    assert "document" in response.json()
    assert response.json()["document"].strip()
