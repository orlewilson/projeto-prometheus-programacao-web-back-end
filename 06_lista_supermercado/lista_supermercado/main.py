"""Lista de Supermercado"""

# Bibliotecas
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# quando for executar o servidor
try:
    from schemas.produto import Produto

# quando for executar os testes
except ImportError:
    from lista_supermercado.schemas.produto import Produto

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# Tratamento de exceções
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, err):
    return JSONResponse(
        status_code = 400,
        content = {"error": str(err)},
    )

# Lista do supermercado
lista_supermercado = []

# @app.get('/produtos') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota GET /produtos
@app.get('/produtos')
async def listar_produtos():
    """Método que será chamado quando for requisitada a rota GET /produtos"""

    if len(lista_supermercado) > 0 :
        message = lista_supermercado
    else:
        message = {"message": "A lista do supermercado está vazia!"}

    return JSONResponse(
        status_code = 200,
        content = message,
    )

# @app.get('/produtos/{item}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota GET /produtos/{item}
@app.get('/produtos/{item}')
async def obter_produto(item: str):
    """Método que será chamado quando for requisitada a rota GET /produtos/{item}"""

    found = False
    for produto in lista_supermercado:
        if produto['item'] == item:
            message = produto
            found = True
            break
    
    if not found :
        message = {"message": "Produto " + item + " não foi encontrado na lista!"}

    return JSONResponse(
        status_code = 200,
        content = message,
    )

# @app.post('/produtos') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota POST /produtos
@app.post('/produtos')
async def adicionar_produto(produto : Produto):
    """Método que será chamado quando for requisitada a rota POST /produtos"""

    lista_supermercado.append(produto.dict())

    message = {"message": "Produto adicionado com sucesso!"}

    return JSONResponse(
        status_code = 200,
        content = message,
    )

# @app.put('/produtos/{item}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota PUT /produtos/{item}
@app.put('/produtos/{item}')
async def atualizar_produto(item : str, produto : Produto):
    """Método que será chamado quando for requisitada a rota PUT /produtos/{item}"""

    found = False
    for produto_a_atualizar in lista_supermercado:
        if produto_a_atualizar['item'] == item:
            lista_supermercado.remove(produto_a_atualizar)
            found = True
            break
    
    if not found :
        message = {"message": "Produto " + item + " não foi encontrado na lista!"}
    else:
        lista_supermercado.append(produto.dict())
        message = {"message": "Produto " + item + " atualizado com sucesso na lista!"}

    return JSONResponse(
        status_code = 200,
        content = message,
    )

# @app.delete('/produtos/{item}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/{item}
@app.delete('/produtos/{item}')
async def apagar_produto(item : str):
    """Método que será chamado quando for requisitada a rota DELETE /produtos/{item}"""
    
    found = False
    for produto_a_apagar in lista_supermercado:
        if produto_a_apagar['item'] == item:
            lista_supermercado.remove(produto_a_apagar)
            found = True
            break
    
    if not found :
        message = {"message": "Produto " + item + " não foi encontrado na lista!"}
    else:
        message = {"message": "Produto " + item + " apagado com sucesso na lista!"}

    return JSONResponse(
        status_code = 200,
        content = message,
    )

# @app.delete('/produtos/') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/
@app.delete('/produtos/')
async def apagar_lista():
    """Método que será chamado quando for requisitada a rota DELETE /produtos/"""
    
    lista_supermercado.clear()
    message = {"message": "Lista apagada com sucesso!"}
    
    return JSONResponse(
        status_code = 200,
        content = message,
    )