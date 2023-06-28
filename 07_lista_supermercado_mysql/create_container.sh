#!/bin/bash
#Subir o ambiente do Banco de Dados Relacional MySQL
result=$(docker container ls -a | grep mysql-prometheus)
container_mysql='mysql-prometheus'

# verificar se o container mysql-prometheus já foi criado
if [[ "$result" == *"$container_mysql"* ]]; 
then
    # apenas inicializa o container caso já esteja criado
    docker container start mysql-prometheus
else
    # cria o container caso não foi criado
    docker run --name mysql-prometheus  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=prometheus -e MYSQL_PASSWORD=12345 -e MYSQL_DATABASE=prometheus-mysql -d mysql:8.0.33
fi

docker container run --name lista-supermercado-mysql -v $(pwd):/apps -it -p 5000:5000  ambiente-prog-web-back-end

# # --name    nome do container
# # -v        mapear volume local:dentro_container
# # -it       modo iterativo, ou seja, permite entrar no container em modo console
# # -p        externalizar uma porta para acesso internamente ao container

docker container rm -f lista-supermercado-mysql

docker container stop mysql-prometheus

# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/