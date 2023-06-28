from fastapi import APIRouter

try:
    from endpoints import produto
except:
    from lista_supermercado_mongodb.endpoints import produto


router = APIRouter()
router.include_router(produto.router)
