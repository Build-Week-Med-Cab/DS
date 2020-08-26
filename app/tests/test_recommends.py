"""Unit tests for /recommends route."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success on request to route."""
    request_data = {
        'effects': ['happy', 'focused', 'giggly', 'hungry', 'sleepy'],
        'helps': ['migranes', 'nausea'],
        'text': 'I prefer sativa heavy hybrids.',
        'count': 6
    }
    response = client.post('/recommends', json=request_data)
    json_body = response.json()

    assert response.status_code == 200
    assert 'strains' in json_body.keys()

    assert len(json_body['strains']) == 6
    for strain in json_body['strains']:
        assert 'strain' in strain.keys()
        assert 'strain_type' in strain.keys()
        assert 'description' in strain.keys()
        assert 'effects' in strain.keys()
        assert 'helps' in strain.keys()


def test_no_input():
    """Return 422 Unprocessable Entity on empty POST request."""
    response = client.post('/recommends')
    assert response.status_code == 422
    assert isinstance(response.json(), dict)


def test_request_get():
    """Return 405 Method Not Allowed on get request."""
    response = client.get('/recommends')
    assert response.status_code == 405
    assert isinstance(response.json(), dict)
