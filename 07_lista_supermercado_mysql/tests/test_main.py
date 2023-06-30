from fastapi.testclient import TestClient
from lista_supermercado_mysql.main import app

client = TestClient(app)

def test_listar_produtos_lista_vazia():
    response = client.delete('/produtos/')
    response = client.get('/produtos')
    assert response.status_code == 200
    assert response.json() == {"message": "A lista do supermercado está vazia!"}

def test_listar_produtos_lista_com_um_item():
    response = client.delete('/produtos/')
    
    response = client.post('/produtos', json={"item": "teste1", "quantidade": 5})
    assert response.status_code == 200
    assert response.json()['item'] == "teste1"
    assert response.json()['quantidade'] == 5

def test_obter_produto_especifico():
    response = client.delete('/produtos/')
    
    response = client.post('/produtos', json={"item": "teste2", "quantidade": 10})

    response = client.get('/produtos/'+ str(response.json()['id']))
    assert response.json()['item'] == "teste2"
    assert response.json()['quantidade'] == 10
