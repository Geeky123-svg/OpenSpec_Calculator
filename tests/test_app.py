import json
from app import app


def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.content_type
    assert "OpenSpec Calculator" in response.get_data(as_text=True)


def test_api_status_route():
    client = app.test_client()
    response = client.get("/api")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Calculator API is running."
    assert "usage" in data


def test_calculate_add_route():
    client = app.test_client()
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "add", "a": 1, "b": 2}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == {"result": 3.0}


def test_calculate_validation_error():
    client = app.test_client()
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "divide", "a": 5, "b": 0}),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.get_json()["error"] == "Division by zero is not allowed."


def test_calculate_invalid_json():
    client = app.test_client()
    response = client.post(
        "/calculate",
        data="not json",
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.get_json()["error"] == "Request body must be valid JSON."
