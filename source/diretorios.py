from pathlib import Path
import os
from typing import List
from colorama import init, Fore, Style
import datetime
import pwd
import stat


# funções relacionadas a dietórios


def escrever_path_em_arquivo(caminho, arquivo):
    try:
        with open(arquivo, 'w') as f:
            f.write(caminho)
        print("Caminho gravado com sucesso no arquivo.")
    except IOError:
        print("Ocorreu um erro ao escrever o caminho no arquivo.")


def ler_path_do_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as f:
            caminho = f.read()
        return caminho
    except IOError:
        print("Ocorreu um erro ao ler o caminho do arquivo.")

def get_user_directory() -> os.PathLike:
    home_dir = str(Path.home())
    return home_dir

def change_directory(directory_path: str = os.getcwd()) -> os.PathLike:

    if directory_path.startswith('/') or directory_path.startswith('.') or directory_path.startswith('\\'):
        directory_path = os.path.join(os.getcwd(), directory_path)
    try:
        os.chdir(directory_path)
        print(f"Diretório alterado para: {os.getcwd()}")
        return directory_path
    except FileNotFoundError:
        print("O diretório não foi encontrado.")
        return os.getcwd()
    except NotADirectoryError:
        print("Caminho fornecido não é um diretório válido.")
        return os.getcwd()

def display_dir_info(path: os.PathLike) -> None:
    folder_info = os.stat(path)

    owner = pwd.getpwuid(folder_info.st_uid).pw_name
    size = folder_info.st_size
    permissions = stat.filemode(folder_info.st_mode)
    num_links = folder_info.st_nlink
    name = os.path.basename(path)
    full_path = os.path.abspath(path)
    modification_time = datetime.datetime.fromtimestamp(folder_info.st_mtime).strftime('%y-%m-%d %H:%M:%S')
    creation_time = datetime.datetime.fromtimestamp(folder_info.st_ctime).strftime('%y-%m-%d %H:%M:%S')

    print(f"Nome: {name}\nTamanho: {size} bytes\nProprietário: {owner}\nPermissões: {permissions}\n" \
           f"Número de links: {num_links}\nCaminho completo: {full_path}\nData de criação: {creation_time}\n" \
           f"Data de modificação: {modification_time}")


def list_directories(directory_path: str = ler_path_do_arquivo("path.txt")) -> None:
    try:
        with os.scandir(directory_path) as entries:
            directories: List[str] = [entry.name for entry in entries if entry.is_dir()]
            print(f"Diretórios em {directory_path} :")
            if directories:
                for directory in directories:
                    print(directory, end=" ")
                print(end="\n")
            else:
                print(". ..")
    except FileNotFoundError:
        print("O diretório não foi encontrado.")


def list_files(directory_path: str = ler_path_do_arquivo("path.txt")) -> None:
    try:
        with os.scandir(directory_path) as entries:
            files: List[str] = [entry.name for entry in entries if entry.is_file()]
            print(f"Arquivos em {directory_path} :")
            if files:
                for file in files:
                    print(file, end=" ")
                print(end="\n")
            else:
                print(". ..")
    except FileNotFoundError:
        print("O diretório não foi encontrado.")

def list_all(directory_path: str = os.getcwd()) -> None:
    init()  # Inicializa o colorama

    try:
        with os.scandir(directory_path) as entries:
            content_directory: List[str] = [entry.name for entry in entries]
            print(f"Conteúdo do diretório {directory_path}:")

            if content_directory:
                for c in content_directory:
                    path = os.path.join(directory_path, c)
                    if os.path.isdir(path):
                        print(Fore.BLUE + c + "/" + Style.RESET_ALL, end=" ")
                    else:
                        print(Fore.MAGENTA + c + Style.RESET_ALL, end=" ")
                print()
            else:
                print(". ..")

    except FileNotFoundError:
        print("O diretório não foi encontrado.")