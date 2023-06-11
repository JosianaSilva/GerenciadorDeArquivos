# funções relacionadas a arquivos

import os
import stat
import pwd
import grp
import datetime
from tabulate import tabulate
import getpass
import subprocess
from ScriptLeitorDeArquivos import get_files_in_directory


def display_file_info(file_name: str, directory_path: str = os.getcwd()) -> None:
    assert file_name in get_files_in_directory(directory_path), f"O arquivo {file_name} não foi encontrado no diretório!"
    file_path = os.path.join(directory_path)
    try:
        file_stat = os.stat(file_path)

        # Proprietário e Grupo
        uid = file_stat.st_uid
        gid = file_stat.st_gid
        owner = pwd.getpwuid(uid).pw_name
        group = grp.getgrgid(gid).gr_name

        # Permissões
        permissions = stat.filemode(file_stat.st_mode)

        # Datas de Criação, Acesso e Modificação
        created_at = datetime.datetime.fromtimestamp(file_stat.st_ctime)
        accessed_at = datetime.datetime.fromtimestamp(file_stat.st_atime)
        modified_at = datetime.datetime.fromtimestamp(file_stat.st_mtime)

        # Tamanho em Disco
        size = file_stat.st_size

        # Trunca o nome do arquivo se for maior que 25 caracteres
        truncated_file_name = file_name if len(
            file_name) <= 25 else file_name[:22] + "..."

        # Monta os dados em formato de tabela
        table = [
            ["Arquivo", truncated_file_name],
            ["Proprietário", owner],
            ["Grupo", group],
            ["Permissões", permissions],
            ["Data de Criação", created_at],
            ["Data de Acesso", accessed_at],
            ["Data de Modificação", modified_at],
            ["Tamanho em Disco", f"{size} bytes"]
        ]

        # Exibe a tabela
        headers = ["Informação", "Valor"]
        print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except AssertionError:
        print("O arquivo não está no diretório indicado.")        


def change_owner(file_name: str, owner: str, directory_path: str = os.getcwd()) -> None:
    assert file_name in get_files_in_directory(directory_path), f"O arquivo {file_name} não foi encontrado no diretório!"
    
    if directory_path:
        os.chdir(directory_path)
    file_path = os.path.abspath(file_name)
    try:

        if os.access(file_path, os.W_OK):
            os.chown(file_path, -1, -1)
            print(
                f"O proprietário do arquivo {file_name} foi alterado para {owner}.")
        else:
            if ask_root_password():
                change_owner_with_root(file_path, owner)
    except KeyError:
        print(f"O usuário {owner} não foi encontrado.")


def change_group(file_name: str, group: str, directory_path: str = os.getcwd()) -> None:
    assert file_name in get_files_in_directory(directory_path), f"O arquivo {file_name} não foi encontrado no diretório!"
    
    if directory_path:
        os.chdir(directory_path)
    file_path = os.path.abspath(file_name)
    
    try:
        gid = grp.getgrnam(group).gr_gid
        if os.access(file_path, os.W_OK):
            os.chown(file_path, -1, gid)
            print(f"O grupo do arquivo {file_name} foi alterado para {group}.")
        else:
            if ask_root_password():
                change_group_with_root(file_path, group)
    except KeyError:
        print(f"O grupo {group} não foi encontrado.")


def change_permissions(file_name: str, permissions: int, directory_path: str = os.getcwd()) -> None:
    assert file_name in get_files_in_directory(directory_path), f"O arquivo {file_name} não foi encontrado no diretório!"
    
    if directory_path:
        os.chdir(directory_path)
        file_path = os.path.join(file_name, directory_path)
    try:
        os.chmod(file_path, permissions)
        print(
            f"As permissões do arquivo {file_name} foram alteradas para {permissions:o}.")
    except FileNotFoundError:
        print(f"O arquivo {file_path} não foi encontrado.")

def ask_root_password() -> bool:
    password = getpass.getpass("Digite a senha de administrador (root): ")
    try:
        sudo_cmd = ["sudo", "-v"]
        proc = subprocess.Popen(sudo_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = proc.communicate(input=password + '\n')
        if proc.returncode == 0:
            return True
        else:
            print("Senha de administrador incorreta.")
            return False
    except subprocess.CalledProcessError:
        print("Erro ao executar o comando 'sudo'.")
        return False

def change_owner_with_root(file_path: str, owner: str) -> None:
    try:
        uid = pwd.getpwnam(owner).pw_uid
        subprocess.check_call(['sudo', 'chown', f"{0}:{uid}", file_path])
        file_name = os.path.basename(file_path)
        print(f"O proprietário do arquivo {file_name} foi alterado para {owner} (com permissões de administrador).")
    except KeyError:
        print(f"O usuário {owner} não foi encontrado.")


def change_group_with_root(file_path: str, group: str) -> None:
    try:
        gid = grp.getgrnam(group).gr_gid
        subprocess.check_call(['sudo', 'chown', f"{0}:{gid}", file_path])
        file_name = os.path.basename(file_path)

        print(
            f"O grupo do arquivo {file_name} foi alterado para {group} (com permissões de administrador).")
    except KeyError:
        print(f"O grupo {group} não foi encontrado.")


# Exemplo de uso:
# change_owner("menu.txt", "josianasouzasilva")
# change_group("menu.txt", "josianasouzasilva")
# display_file_info("menu.txt")
change_permissions("menu.txt", 755)