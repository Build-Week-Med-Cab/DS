"""Unit tests for main app functinality."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_docs():
    """Return HTML docs for root route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('text/html')


def test_unknown():
    """Return 404 for unknown route."""
    response = client.get('/unknown_route')
    assert response.status_code == 404
