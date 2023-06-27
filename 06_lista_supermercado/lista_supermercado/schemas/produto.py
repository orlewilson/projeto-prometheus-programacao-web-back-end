"""Modelo para representar um produto """

# Bibliotecas
from pydantic import BaseModel
from typing import Optional

# Classe para representar um produto na lista de supermercado
class Produto(BaseModel):
    item: str
    quantidade: int
    preco: Optional[float] = None
