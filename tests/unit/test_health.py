from fastapi.testclient import TestClient

from backend.app.main import app


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_follow_up_preview_endpoint() -> None:
    client = TestClient(app)
    payload = {
        "thread_id": "thread-1",
        "last_reply_at": "2026-05-18T00:00:00Z",
        "email_body": "Checking in on this request",
    }
    response = client.post("/api/v1/follow-up/preview", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["thread_id"] == "thread-1"
    assert body["next_action"] in {
        "wait",
        "send_follow_up_email",
        "escalate_voice_or_manager",
    }
    assert isinstance(body["age_hours"], float)
