# Bibliotecas
from fastapi import APIRouter


try:
    from models.produto import ProdutoModel, ResponseModel
    from db import database
except:
    from lista_supermercado_mongodb.models.produto import ProdutoModel, ResponseModel
    from lista_supermercado_mongodb.db import database

# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_description="Product data added into the database")
async def adicionar_produto(produto: ProdutoModel):
    """Método que será chamado quando for requisitada a rota POST /produtos"""
    produto_a_cadatrar = produto.as_dict()
    new_product = await database.adicionar_produto(produto_a_cadatrar)
    return ResponseModel(new_product, 200)

# # @app.get('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# # requisições quando for requisitada a rota GET /produtos/{id}
@router.get("/{produto_id}")
async def obter_produto(produto_id: str):
    produto_encontrado = await database.encontrar_produto_por_id(produto_id)
    
    if produto_encontrado is not None:
        return ResponseModel(produto_encontrado, 200)
    else:
        return ResponseModel({"erro": 404, "message" : "Produto não encontrado"}, 200)


# @router.get('/produtos') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota GET /produtos
@router.get('/')
async def listar_produtos():
    """Método que será chamado quando for requisitada a rota GET /produtos"""

    # pesquisa na base de dados
    produtos = await database.listar_produtos()
    
    if len(produtos) > 0 :
        return ResponseModel(produtos, 200)
    else:
        return ResponseModel({"message": "A lista do supermercado está vazia!"}, 200)
        
# @app.delete('/produtos/') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/
@router.delete("/")
async def apagar_lista():
    """Método que será chamado quando for requisitada a rota DELETE /produtos/"""
    
    # pesquisa na base de dados
    produto_encontrado = await database.apagar_todos_produtos()

    return ResponseModel({"message": "A lista do supermercado está vazia!"}, 200)

# @app.put('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota PUT /produtos/{id}
@router.put("/{produto_id}")
async def atualizar_produto(produto_id: str, produto: ProdutoModel):
    """Método que será chamado quando for requisitada a rota PUT /produtos/{id}"""

    if not await database.existe_produto_por_id(produto_id):
        return ResponseModel({"erro": 404, "message" : "Produto não encontrado"}, 200)
    else:
        produto_a_atualizar = produto.as_dict()
        produto_atualizado = await database.atualizar_produto(produto_id, produto_a_atualizar)
        return ResponseModel(produto_atualizado, 200)

# @router.delete('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/{id}
@router.delete('/{produto_id}')
async def apagar_produto(produto_id: str):
    """Método que será chamado quando for requisitada a rota DELETE /produtos/{id}"""
    
    if not await database.existe_produto_por_id(produto_id):
        return ResponseModel({"erro": 404, "message" : "Produto não encontrado"}, 200)
    else:
        produto_apagado = await database.apagar_produto_por_id(produto_id)
        return ResponseModel({"message" : "Produto apagado com sucesso!"}, 200)


