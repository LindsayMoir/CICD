from fastapi.testclient import TestClient
from ingest_data import app  # Assuming your FastAPI app is in ingest_data.py

client = TestClient(app)


def test_ingest_data_negative_feature_1():
    # Test with a negative feature_1
    response = client.post(
        "/ingest_data",
        json={
            "feature_1": -5,
            "feature_2": "Valid string"})
    assert response.status_code == 400
    assert response.json() == {"detail": "feature_1 must be non-negative"}


def test_ingest_data_long_feature_2():
    # Test with a feature_2 that exceeds 280 characters
    long_string = "a" * 281  # 281 characters long
    response = client.post(
        "/ingest_data",
        json={
            "feature_1": 10.5,
            "feature_2": long_string})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "feature_2 must be 280 characters or less"}


def test_ingest_data_valid_input():
    # Test with valid input
    response = client.post(
        "/ingest_data",
        json={
            "feature_1": 10.5,
            "feature_2": "Valid string"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Data ingested successfully",
        "data": {"feature_1": 10.5, "feature_2": "Valid string"}
    }
