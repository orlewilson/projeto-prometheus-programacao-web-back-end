from fastapi.testclient import TestClient
from hello_world_fast_api_v3.main import app

client = TestClient(app)

def test_say_hello_with_name_parameter():
    response = client.get('/hello-world?name=Orlewilson')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World, Orlewilson!'}

def test_say_hello_without_name_parameter():
    response = client.get('/hello-world')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World!'}

def test_say_hello_with_name_empty():
    response = client.get('/hello-world?name=')
    assert response.status_code == 404
    assert response.json() == {'message': 'Name cannot be empty!'}
