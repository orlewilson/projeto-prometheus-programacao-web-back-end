from fastapi.testclient import TestClient
from hello_world_fast_api.main import app

client = TestClient(app)

def test_say_hello():
    response = client.get('/hello-world')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}