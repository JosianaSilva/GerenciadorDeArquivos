import os
from arquivos import *
from diretorios import *
from ScriptLeitorDeArquivos import *
import platform

class GerenciadorDeArquivos:
    def __init__(self, f):
        self.diretorio = f


def main():
    escrever_path_em_arquivo(get_user_directory(), "path.txt")
    print("Bem-vindo ao gerenciador de arquivos!")
    while True:
        print(f"Você está em.................{ler_path_do_arquivo('path.txt')}")
        print("Opções:")
        print("1. Mudar diretório")
        print("2. Listar (arquivos ou/e diretórios)")
        print("3. Informações")
        print("4. Alterar algo do arquivo")
        print("5. Operações com arquivos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            mudar_diretorio()

        elif opcao == "2":
            listar_arquivos()
        elif opcao == "3":
            informacoes()
        elif opcao == "4":
            alterar_arquivo()
        elif opcao == "5":
            operacoes_arquivos()
        elif opcao == "0":
            print("Saindo do gerenciador de arquivos...")
            break
        else:
            print("Opção inválida")


def mudar_diretorio():
    novo_dir = input("Digite o caminho completo do novo diretório: ")
    try:
        
        diretorio = change_directory(novo_dir)
        escrever_path_em_arquivo(diretorio, "path.txt")
        continuar()
    except OSError:
        print("Erro: Diretório não encontrado")

def listar_arquivos():
    limpar_tela()
    opcao = input("Listar arquivos (a), diretórios (d) ou ambos (ad)? ")
    if opcao == "a":
        list_files()
        continuar()
    elif opcao == "d":
        list_directories()
        continuar()
    elif opcao == "ad":
        list_all()
        continuar()
    else:
        print("Opção inválida")

def informacoes():
    limpar_tela()
    path = input("Digite o caminho completo do arquivo ou diretório: ")
    if os.path.exists(path):
        if os.path.isfile(path):
            display_file_info(path)
            continuar()
        else :
            display_dir_info(path)
            continuar()
    else:
        print("Erro: Arquivo ou diretório não encontrado")

def alterar_arquivo():
    limpar_tela()
    path = input(f"""Nota: Para alterar informações de um arquivo você deve estar nesse diretório.\n
                 {[str(f) for f in get_files_in_directory()]}\n\nDigite o nome do arquivo: """)
    if(path[0]=="."):
        path = os.path.join(os.getcwd(),path[1:])
    
    if os.path.exists(path):
        print(f"Informações de {path}:")
        print(f"Proprietário: {get_owner(path)}")
        print(f"Grupo: {get_group(path)}")
        print(f"Permissões: {get_permissions(path)}")
        
        opcao = input("O que deseja alterar? (p)roprietário, (g)rupo ou per(m)issões? ")
        if opcao == "p":
            try:
                novo_proprietario = input("Digite o nome do novo proprietário: ")
                change_owner(path, novo_proprietario, ler_path_do_arquivo)
                print("Proprietário alterado com sucesso")
            except:
                print("Erro: Não foi possível alterar o proprietário")
        elif opcao == "g":
            novo_grupo = input("Digite o nome do novo grupo: ")
            try:
                os.chown(path, new_grp=novo_grupo)
                print("Grupo alterado com sucesso")
                continuar()
            except OSError:
                print("Erro: Não foi possível alterar o grupo")
        elif opcao == "m":
            novas_permissoes = input("Digite as novas permissões na notação -rwxrwxrwx: ")
            change_permissions(path, novas_permissoes, os.getcwd())

        else:
            print("Opção inválida")
    else:
        print(f"Erro: {path} não encontrado")

def operacoes_arquivos():
    limpar_tela()
    opcao = input("O que deseja fazer? (c)riar, (a)pagar, (co)piar, (m)over ou (l)inks simbólicos? ")
    if opcao == "c":
        nome_arquivo = input("Digite o nome do arquivo: ")
        try:
            open(nome_arquivo, "w").close()
            print("Arquivo criado com sucesso")
        except OSError:
            print("Erro: Não foi possível criar o arquivo")
    elif opcao == "a":
        nome_arquivo = input("Digite o nome do arquivo: ")
        if os.path.exists(nome_arquivo):
            try:
                os.remove(nome_arquivo)
                print("Arquivo apagado com sucesso")
                continuar()
            except OSError:
                print("Erro: Não foi possível apagar o arquivo")
        else:
            print("Erro: Arquivo não encontrado")
    elif opcao == "co":
        origem = input("Digite o caminho completo do arquivo de origem: ")
        destino = input("Digite o caminho completo do arquivo de destino: ")
        if os.path.exists(origem):
            try:
                with open(origem, "rb") as f_origem, open(destino, "wb") as f_destino:
                    f_destino.write(f_origem.read())
                print("Arquivo copiado com sucesso")
                continuar()
            except OSError:
                print("Erro: Não foi possível copiar o arquivo")
        else:
            print("Erro: Arquivo de origem não encontrado")
    elif opcao == "m":
        origem = input("Digite o caminho completo do arquivo de origem: ")
        destino = input("Digite o caminho completo do arquivo de destino: ")
        if os.path.exists(origem):
            try:
                os.rename(origem, destino)
                print("Arquivo movido com sucesso")
                continuar()
            except OSError:
                print("Erro: Não foi possível mover o arquivo")
        else:
            print("Erro: Arquivo de origem não encontrado")
    elif opcao == "l":
        nome_link = input("Digite o nome do link simbólico: ")
        destino = input("Digite o caminho completo do arquivo de destino: ")
        if os.path.exists(destino):
            try:
                os.symlink(destino, nome_link)
                print("Link simbólico criado com sucesso")
                continuar()
            except OSError:
                print("Erro: Não foi possível criar o link simbólico")
        else:
            print("Erro: Arquivo de destino não encontrado")
    else:
        print("Opção inválida")





def limpar_tela():
    sistema_operacional = platform.system()

    if sistema_operacional == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def continuar():
    input("Pressione ENTER para continuar...")
    limpar_tela()

if __name__ == '__main__':
    main()      