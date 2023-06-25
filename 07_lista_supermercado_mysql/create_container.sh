#!/bin/bash
#Subir o ambiente do Banco de Dados Relacional MySQL
docker run --name mysql-prometheus  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=prometheus -e MYSQL_PASSWORD=12345 -e MYSQL_DATABASE=prometheus-mysql -d mysql:8.0.33

docker container run --name lista-supermercado-mysql -v $(pwd):/apps -it -p 5000:5000  ambiente-prog-web-back-end

# --name    nome do container
# -v        mapear volume local:dentro_container
# -it       modo iterativo, ou seja, permite entrar no container em modo console
# -p        externalizar uma porta para acesso internamente ao container

docker container rm -f lista-supermercado-mysql

docker container rm -f mysql-prometheus

# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/