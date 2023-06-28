#!/bin/bash
#Subir o ambiente do Banco de Dados Não Relacional MongoDB
docker run --name mongodb-prometheus -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=prometheus -e MONGO_INITDB_ROOT_PASSWORD=12345 -d mongo:6.0

docker container run --name lista-supermercado-mongodb -v $(pwd):/apps -it -p 5000:5000  ambiente-prog-web-back-end

# --name    nome do container
# -v        mapear volume local:dentro_container
# -it       modo iterativo, ou seja, permite entrar no container em modo console
# -p        externalizar uma porta para acesso internamente ao container

docker container rm -f lista-supermercado-mongodb

docker container rm -f mongodb-prometheus

# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/