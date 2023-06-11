from pathlib import Path
import os
from typing import List

# funções relacionadas a dietórios

def get_user_directory():
    home_dir = str(Path.home())
    return home_dir

def change_directory(directory_path):
    if directory_path.startswith('/') or directory_path.startswith('.') or directory_path.startswith('\\'):
        directory_path = os.path.join(os.getcwd(), directory_path)
    try:
        os.chdir(directory_path)
        print(f"Diretório alterado para: {os.getcwd()}")
        return os.getcwd()
    except FileNotFoundError:
        print("O diretório não foi encontrado.")
    except NotADirectoryError:
        print("Caminho fornecido não é um diretório válido.")

def list_directories(directory_path: str) -> None:
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

from colorama import init, Fore, Style

def list_all(directory_path: str) -> None:
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