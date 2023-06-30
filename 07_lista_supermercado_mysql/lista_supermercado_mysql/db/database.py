"""Configuração do acesso ao banco de dados"""

# Bibliotecas
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://prometheus:12345@172.17.0.2:3306/prometheus-mysql"

# Objeto de conexão com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Objeto que representará a sessão do acesso ao banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Usado para criação das classes do modelo do banco de dados
Base = declarative_base()

# Disponibiliza a instancia da classe de acesso ao banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# fonte: https://www.treinaweb.com.br/blog/criando-o-primeiro-crud-com-fastapi
