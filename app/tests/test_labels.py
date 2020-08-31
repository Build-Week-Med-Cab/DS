from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_post_1():
    """Return 405 when post-ing"""
    response = client.post('/labels')
    assert response.status_code == 405

def test_get_1():
    """Returns 200 for the get"""
    response = client.get('/labels')
    assert response.status_code == 200