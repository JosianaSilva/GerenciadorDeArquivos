import os

#abrindo a pasta
os.chdir("C:\\Users\\humbe\\Downloads\\sistemaDeArquivos\\Arquivos")

os.listdir()

# listando cada arquivo presente no diretório
for f in os.listdir():
    print(f)