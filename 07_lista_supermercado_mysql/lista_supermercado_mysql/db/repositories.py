"""Para acesso às informações contidas no banco de dados"""

# Bibliotecas
from sqlalchemy.orm import Session

try:
    from db.models import Produto
except:
    from lista_supermercado_mysql.db.models import Produto

class ProdutoRepository:
    @staticmethod
    def listar_produtos(db: Session) -> list[Produto]:
        return db.query(Produto).all()

    @staticmethod
    def adicionar_produto(db: Session, produto: Produto) -> Produto:
        db.add(produto)
        db.commit()
        return produto
    
    def atualizar_produto(db: Session, produto: Produto) -> Produto:
        db.merge(produto)
        db.commit()
        return produto

    @staticmethod
    def encontrar_produto_por_id(db: Session, id: int) -> Produto:
        return db.query(Produto).filter(Produto.id == id).first()

    @staticmethod
    def existe_produto_por_id(db: Session, id: int) -> bool:
        return db.query(Produto).filter(Produto.id == id).first() is not None

    @staticmethod
    def apagar_produto_por_id(db: Session, id: int) -> None:
        produto = db.query(Produto).filter(Produto.id == id).first()
        if produto is not None:
            db.delete(produto)
            db.commit()

    @staticmethod
    def apagar_todos_produtos(db: Session) -> None:
        db.query(Produto).delete()
        db.commit()