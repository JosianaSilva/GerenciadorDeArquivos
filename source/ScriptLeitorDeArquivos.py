import os

#abrindo a pasta
# os.chdir("C:\\Users\\humbe\\Downloads\\sistemaDeArquivos\\Arquivos")

# os.listdir()

# listando cada arquivo presente no diretório
# for f in os.listdir():
#     print(f)

def get_files_in_directory(path_directory: str = os.getcwd()) -> list[str]:
    os.chdir(path_directory)
    return [obj.name for obj in os.scandir() if obj.is_file()]
