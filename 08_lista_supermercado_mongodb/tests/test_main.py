from fastapi.testclient import TestClient
from lista_supermercado_mongodb.main import app

client = TestClient(app)

def test_listar_produtos_lista_vazia() -> None:
    response = client.delete('/produtos')
    assert response.status_code == 200
    assert response.json() == {"message": "A lista do supermercado está vazia!"}

    # response = client.get('/produtos')
    # assert response.status_code == 200
    # assert response.json() == {"message": "A lista do supermercado está vazia!"}

# def test_listar_produtos_lista_com_um_item() -> None:
#     response = client.post('/produtos', json={"item": "teste1", "quantidade": 5})
#     assert response.status_code == 200
#     # assert response.json() == {"message": "Produto adicionado com sucesso!"}

#     response = client.get('/produtos')
#     assert response.status_code == 200
#     # assert response.json() == [{"item": "teste1", "quantidade": 5, "preco": None}]

# def test_obter_produto_especifico() -> None:
#     response = client.post('/produtos', json={"item": "teste2", "quantidade": 10})
#     assert response.status_code == 200
#     # assert response.json() == {"message": "Produto adicionado com sucesso!"}

#     # response = client.get('/produtos/teste2')
#     # assert response.status_code == 200
#     # assert response.json() == {"item": "teste2", "quantidade": 10, "preco": None}

# def test_obter_produto_ausente() -> None:
#     response = client.get('/produtos/teste3')
#     assert response.status_code == 200
#     # assert response.json() == {"message": "Produto teste3 não foi encontrado na lista!"}

# def test_adicionar_produto() -> None:
#     response = client.post('/produtos', json={"item": "teste4", "quantidade": 5})
#     assert response.status_code == 200
#     # assert response.json() == {"message": "Produto adicionado com sucesso!"}

# def test_adicionar_produto_sem_body() -> None:
#     response = client.post('/produtos', json={})
#     assert response.status_code == 400
#     assert response.json() == {'error': '2 validation errors for Request\nbody -> item\n  field required (type=value_error.missing)\nbody -> quantidade\n  field required (type=value_error.missing)'} 

# def test_atualizar_produto() -> None:
#     response = client.post('/produtos', json={"item": "teste5", "quantidade": 5})
#     assert response.status_code == 200
    # assert response.json() == {"message": "Produto adicionado com sucesso!"}

    # response = client.put('/produtos/teste5', json={"item": "teste5", "quantidade": 10, "preco": 3.3})
    # assert response.status_code == 200
    # assert response.json() == {"message": "Produto teste5 atualizado com sucesso na lista!"}

# def test_atualizar_produto_ausente() -> None:
#     response = client.put('/produtos/teste6', json={"item": "teste6", "quantidade": 10, "preco": 3.3})
#     assert response.status_code == 200
#     # assert response.json() == {"message": "Produto teste6 não foi encontrado na lista!"}

# def test_apagar_produto() -> None:
#     response = client.post('/produtos', json={"item": "teste7", "quantidade": 5})
#     assert response.status_code == 200
#     assert response.json() == {"message": "Produto adicionado com sucesso!"}

#     response = client.delete('/produtos/teste7')
#     assert response.status_code == 200
#     assert response.json() == {"message": "Produto teste7 apagado com sucesso na lista!"}

# def test_apagar_produto_ausente() -> None:
#     response = client.delete('/produtos/teste8')
#     assert response.status_code == 200
#     assert response.json() == {"message": "Produto teste8 não foi encontrado na lista!"}

# def test_apagar_lista() -> None:
#     response = client.delete('/produtos/')
#     assert response.status_code == 200
#     assert response.json() == {"message": "Lista apagada com sucesso!"}