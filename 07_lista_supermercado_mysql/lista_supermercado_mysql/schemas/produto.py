"""Modelo para representar um produto """

# Bibliotecas
from pydantic import BaseModel
from typing import Optional

# Classe para representar um produto na lista de supermercado
class ProdutoBase(BaseModel):
    item: str
    quantidade: int
    preco: Optional[float] = None

class ProdutoRequest(ProdutoBase):
    ...

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        orm_mode = True # está informando que utilizaremos o mapeamento objeto relacional
        from_attributes = True