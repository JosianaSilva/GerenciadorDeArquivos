#!/bin/bash

sudo systemctl start docker 

# Remover a imagem existente (opcional)
sudo docker rmi alpine-gerenc

# Construir a nova imagem
sudo docker build -t alpine-gerenc .

sudo docker run -it --rm  --name gerenciador-arquivos alpine-gerenc
