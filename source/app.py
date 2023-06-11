import os
from diretorios import change_directory, list_directories, get_user_directory, list_all
from ScriptLeitorDeArquivos import get_files_in_directory


#teste
diretorio_inicial = get_user_directory()
os.chdir(diretorio_inicial)
print("----------------------\n"+diretorio_inicial+"----------------------\n")

# novo_dir = "/home/app"
novo_dir = input("Qual o dir?: ")
atual_dir = change_directory(novo_dir)

print(atual_dir)

list_directories(atual_dir)
print()
print(get_files_in_directory(atual_dir))
print()
list_all(atual_dir)
print("*****"+os.getcwd()+"*****")
###
