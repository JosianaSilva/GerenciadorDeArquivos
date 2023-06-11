import os
from diretorios import change_directory, list_directories, get_user_directory, list_all
from ScriptLeitorDeArquivos import listar_arquivos


#teste
diretorio_inicial = get_user_directory()
os.chdir(diretorio_inicial)

novo_dir = "./pt"
atual_dir = change_directory(novo_dir)

list_directories(atual_dir)
print()
listar_arquivos(atual_dir)
print()
list_all(atual_dir)

###
