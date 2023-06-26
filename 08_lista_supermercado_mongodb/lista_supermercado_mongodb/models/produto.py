"""Modelos usados para a criação das tabelas no banco de dados"""

# Bibliotecas
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from typing import Optional

try:
    from models.PyObjectId import PyObjectId

except:
    from lista_supermercado_mongodb.models.PyObjectId import PyObjectId

class ProdutoModel(BaseModel):
    item: str
    quantidade: int
    preco: Optional[float]
    
    def as_dict(self):
        return {"item": self.item,
                "quantidade": self.quantidade,
                "preco": self.preco}


class ProdutoUpdateModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    item: str = Field(..., title="Descricao do item", max_length=500)
    quantidade: int = Field(..., title="Quantidade de itens")
    preco: float = Field(None, title="Preco unitário do item")

    def as_dict(self):
        return {"id": self.id,
                "item": self.item,
                "quantidade": self.quantidade,
                "preco": self.price}

def ResponseModel(message, code):
    return JSONResponse(
        status_code = code,
        content = message,
    )