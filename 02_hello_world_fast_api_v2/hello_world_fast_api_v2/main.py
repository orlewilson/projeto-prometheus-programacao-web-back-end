"""Hello World com FastAPI V2"""

# Bibliotecas
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# @app.get('/hello-world') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /hello-world?name=<nome>
@app.get('/hello-world')
async def say_hello(name : str):
    """Método que será chamado quando for requisitada a rota /hello-world?name=<nome>"""
    return JSONResponse(
        status_code = 200,
        content = {"message": "Hello World, " + name + "!"},
    )
