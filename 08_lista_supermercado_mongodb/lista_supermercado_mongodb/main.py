"""Lista de Supermercado"""

# Bibliotecas
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

try:
    from routes.api import router as api_router    
except:
    from lista_supermercado_mongodb.routes.api import router as api_router

# Cria uma instância da classe FastAPI para habilitar a interação com nossa API
app = FastAPI()

origins = ["http://0.0.0.0:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5000, log_level="info", reload=True)
    print("running")