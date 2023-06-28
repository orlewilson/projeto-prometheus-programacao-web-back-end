# Imagem Base
FROM debian:11

# Mantenedor
LABEL version="1.0"
LABEL author="Orlewilson Maia (orlewilson.maia@gmail.com)"
LABEL description="Debian 11 + Python3 + FastAPI + QA"

# Atualização dos Pacotes
RUN apt update

# Instalação dos Pacotes 
# Python
RUN apt install -y python3
RUN apt install -y pip

# FastAPI
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install httpx

# Banco de Dados (MySQL)
RUN pip install sqlalchemy 
RUN pip install pymysql
RUN pip install cryptography

# Banco de Dados (MongoDB)
RUN pip install pymongo
RUN pip install motor

# Qualidade de Software (QA)
RUN pip install pytest 
RUN pip install pytest-cov
RUN pip install pylint
RUN pip install pylint-json2html

# Diretório Padrão
WORKDIR /apps