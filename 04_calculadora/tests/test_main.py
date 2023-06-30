from fastapi.testclient import TestClient
from calculadora.main import app

client = TestClient(app)

def test_somar_a_b_validos():
    response = client.get('/somar?a=2&b=2')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "resultado" :4 }

def test_somar_a_invalido_b_valido():
    response = client.get('/somar?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() == {"error": "1 validation error for Request\nquery -> a\n  value is not a valid integer (type=type_error.integer)"}