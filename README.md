# 📂 GerenciadorDeArquivos

## >_ Estrutura no terminal
O objetivo deste projeto é criar um gerenciador de arquivos simples usando python, com as seguintes características:

1. Alterar o diretório de trabalho;
2. Listar arquivos e diretórios;
3. Permitir consulta de informações sobre um determinado arquivo/diretório, tais como:
- Identificador de Prorietário (UID);
- Identificador de Grupo (GID);
- Permissões de acesso;
- Datas (criação, acesso e modificação);
- Tamanho em disco (armazenamento).
4. Permitir alterar os seguintes atributos:
- Identificador de Prorietário (UID);
- Identificador de Grupo (GID);
- Permissões de acesso.
5. Permitir operações em arquivos/diretórios, tais como:
- Criação;
- Remoção;
- Cópia;
- Movimento;
- Criação de links simbólicos (ou atalhos). 
---

## 💻 Como executar
Aqui está como executá-lo:

1. Clone o repositório em sua máquina local.
2. Abra o terminal e navegue até o diretório do projeto.
3. Siga as próximas instruções, para executar com o python ou com docker.


### Usando Python

~~~python
python3 ./source/app.py
~~~

### Usando docker
Comando para criar a imagem:
~~~bash
docker build -t <substitua pelo nome da imagem> .
~~~
Comando para rodar o container:
~~~bash
docker run -it --rm  --name <substitua pelo nome do container> <substitua pelo nome da imagem>
~~~

---
## 👥 Equipe
- [Francisco Humberto Tavares Sampaio](https://github.com/Humbert010)
- [João Victor Cordeiro de Norões](https://github.com/jvictor-cordeiro)
- [Josiana Francisca de Souza Silva](https://github.com/JosianaSilva/)