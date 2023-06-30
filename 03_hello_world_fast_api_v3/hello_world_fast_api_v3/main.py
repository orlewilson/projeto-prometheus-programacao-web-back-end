"""Hello World com FastAPI V3"""

# Bibliotecas
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# @app.get('/hello-world') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /hello-world[?name=<nome>]
@app.get('/hello-world')
async def say_hello(name = None):
    """Método que será chamado quando for requisitada a rota /hello-world[?name=<nome>]"""
    if name is None:
        message = "Hello World!"
        code = 200
    elif name == "":
        message = "Name cannot be empty!"
        code = 404
    else:
        message = "Hello World, " + name + "!"
        code = 200

    return JSONResponse(
        status_code = code,
        content = {"message": message},
    )
