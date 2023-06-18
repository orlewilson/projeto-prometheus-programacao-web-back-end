"""Calculadora Completa"""

# Bibliotecas
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

# Tratamento de exceções
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, err):
    return JSONResponse(
        status_code = 400,
        content = {"error": str(err)},
    )

# @app.get('/somar') informa ao FastAPI que esta função gerenciará as
# requisições a partir do caminho /somar
@app.get('/somar')
async def somar(a : int, b : int):
    """Método que será chamado quando for requisitada a rota /somar"""
    resultado = a + b

    return JSONResponse(
        status_code = 200,
        content = {"a": a,
                   "b": b,
                   "resultado" :resultado },
    )
