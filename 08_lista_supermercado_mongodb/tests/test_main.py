from fastapi.testclient import TestClient
from lista_supermercado_mongodb.main import app

client = TestClient(app)

def test_listar_produtos_lista_vazia():
    response = client.delete('/produtos')
    assert response.status_code == 200
    assert response.json() == {"message": "A lista do supermercado está vazia!"}
