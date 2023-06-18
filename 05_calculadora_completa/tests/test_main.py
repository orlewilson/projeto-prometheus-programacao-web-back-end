from fastapi.testclient import TestClient
from calculadora_completa.main import app

client = TestClient(app)

def test_somar_a_b_validos() -> None:
    response = client.get('/somar?a=2&b=2')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 2, "resultado" :4 }

def test_somar_a_invalido_b_valido() -> None:
    response = client.get('/somar?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() == {"error": "1 validation error for Request\nquery -> a\n  value is not a valid integer (type=type_error.integer)"}

def test_subtrair_a_b_validos() -> None:
    response = client.get('/subtrair?a=2&b=3')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 3, "resultado" : -1 }

def test_subtrarir_a_invalido_b_valido() -> None:
    response = client.get('/subtrair?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() == {"error": "1 validation error for Request\nquery -> a\n  value is not a valid integer (type=type_error.integer)"}

def test_multiplicar_a_b_validos() -> None:
    response = client.get('/multiplicar?a=2&b=3')
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 3, "resultado" : 6 }

def test_multiplicar_a_invalido_b_valido() -> None:
    response = client.get('/multiplicar?a=2.2&b=2')
    assert response.status_code == 400
    assert response.json() == {"error": "1 validation error for Request\nquery -> a\n  value is not a valid integer (type=type_error.integer)"}