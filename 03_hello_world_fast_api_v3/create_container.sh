#!/bin/bash

docker container run --name hello-world-fast-api-v3 -v $(pwd):/apps -it -p 5000:5000 ambiente-prog-web-back-end

# --name    nome do container
# -v        mapear volume local:dentro_container
# -it       modo iterativo, ou seja, permite entrar no container em modo console
# -p        externalizar uma porta para acesso internamente ao container

docker container rm -f hello-world-fast-api-v3
# rm -f     apaga um container (-f )

# Fonte: https://docs.docker.com/engine/reference/run/