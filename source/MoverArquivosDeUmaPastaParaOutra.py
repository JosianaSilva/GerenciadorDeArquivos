import os

DePasta = "C:\\Users\\humbe\\Downloads\\sistemaDeArquivos\\Arquivos"
ParaPasta = "C:\\Users\\humbe\\Downloads\\sistemaDeArquivos\\OutrosArquivos"

os.chdir(DePasta)

os.listdir()

# listando cada arquivo presente no diretório
for f in os.listdir():
    os.rename(f, ParaPasta + "\\" + f)