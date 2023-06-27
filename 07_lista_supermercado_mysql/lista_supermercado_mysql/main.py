"""Lista de Supermercado"""

# Bibliotecas
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session

# quando for executar o servidor
try:
    from schemas.produto import ProdutoBase, ProdutoRequest, ProdutoResponse
    from db.models import Produto
    from db.repositories import ProdutoRepository
    from db.database import engine, Base, get_db
    
# quando for executar os testes
except ImportError:
    from lista_supermercado_mysql.schemas.produto import ProdutoBase, ProdutoRequest, ProdutoResponse
    from lista_supermercado_mysql.db.models import Produto
    from lista_supermercado_mysql.db.repositories import ProdutoRepository
    from lista_supermercado_mysql.db.database import engine, Base, get_db

# Configuração de acesso ao Banco de Dados
Base.metadata.create_all(bind=engine)

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# Tratamento de exceções
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, err):
    return JSONResponse(
        status_code = 400,
        content = {"error": str(err)},
    )

# @app.get('/produtos') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota GET /produtos
@app.get('/produtos')
async def listar_produtos(db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota GET /produtos"""

    # pesquisa na base de dados
    produtos = ProdutoRepository.listar_produtos(db)
    
    if len(produtos) > 0 :
        return [ProdutoResponse.from_orm(produto) for produto in produtos]
    else:
        return JSONResponse(
            status_code = 200,
            content = {"message": "A lista do supermercado está vazia!"},
        ) 

# @app.get('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota GET /produtos/{id}
@app.get('/produtos/{id}')
async def obter_produto(id: int, db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota GET /produtos/{id}"""

    produto = ProdutoRepository.encontrar_produto_por_id(db, id)
    if not produto:
        return JSONResponse(
            status_code = 404,
            content = {"message": "Produto " + id + " não foi encontrado na lista!"},
        )
    return ProdutoResponse.from_orm(produto)
    
# @app.post('/produtos') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota POST /produtos
@app.post('/produtos')
async def adicionar_produto(request: ProdutoRequest, db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota POST /produtos"""

    produto = ProdutoRepository.adicionar_produto(db, Produto(**request.dict()))
    return ProdutoResponse.from_orm(produto)

# @app.put('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota PUT /produtos/{id}
@app.put('/produtos/{id}')
async def atualizar_produto(id: int, request: ProdutoRequest, db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota PUT /produtos/{id}"""

    if not ProdutoRepository.existe_produto_por_id(db, id):
        return JSONResponse(
            status_code = 404,
            content = {"message": "Produto " + id + " não foi encontrado na lista!"},
        )
    else:
        produto = ProdutoRepository.atualizar_produto(db, Produto(id=id, **request.dict()))
        return ProdutoResponse.from_orm(produto)

# @app.delete('/produtos/{id}') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/{id}
@app.delete('/produtos/{id}')
async def apagar_produto(id: int, db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota DELETE /produtos/{id}"""
    
    if not ProdutoRepository.existe_produto_por_id(db, id):
        return JSONResponse(
            status_code = 404,
            content = {"message": "Produto " + str(id) + " não foi encontrado na lista!"},
        )
    else:
        produto = ProdutoRepository.apagar_produto_por_id(db, id)
        return JSONResponse(
            status_code = 200,
            content = {"message": "Produto id=" + str(id) + " apagado com sucesso!"},
        )
    

# @app.delete('/produtos/') informa ao FastAPI que esta função gerenciará as
# requisições quando for requisitada a rota DELETE /produtos/
@app.delete('/produtos/')
async def apagar_lista(db: Session = Depends(get_db)):
    """Método que será chamado quando for requisitada a rota DELETE /produtos/"""
    
    # pesquisa na base de dados
    produtos = ProdutoRepository.apagar_todos_produtos(db)
    
    return JSONResponse(
            status_code = 200,
            content = {"message": "A lista do supermercado está vazia!"},
        )
