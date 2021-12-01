## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import requests

error = f'{Twhite}[{Ired}ERROR{Twhite}]';
warning = f'{Twhite}[{Nyellow}!{Twhite}]';
info = f'{Twhite}[{Dgreen}i{Twhite}]'
result = os.popen('figlet MID-PAINEL').read()


os.system('clear')

print(f'Painel de Consultas básicas by Dr Midnight')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
import os, sys, time, json, subprocess, platform

try:
    import requests, random, json, phonenumbers
except:
    install = input(
        f'{Twhite}{Dgreen}[i]{Twhite} Ola! Vejo que esta é sua primeira vez aqui...'
        f'\nDeseja instalar o software necessário?\n1-Sim\n2-Não\n_').strip().upper()[0]
    if install == 'S' or install == '1':
        os.system("apt install figlet -y")
        os.system('python3 -m pip install --upgrade pip')
        os.system('pip3 install requests pytube phonenumbers netifaces')
        clear()
    else:
        print(f'Ok... Tente realizar a instalação manual ou Adeus');
        exit()
    restart()


try:
    from database import cep, covid19, ip, placa, banner, root, meuip, cnpj, nome
except Exception as error:
    print(f'{Twhite}{Ired}[*]{Twhite} Erro: ' + error)
    exit()

def dialog(text='', tiled='='):
    clear();
    print(os.popen('figlet MID-PAINEL').read())
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    for txt in text:
        print(str(warning) + ' ' + txt)
    print(str(Twhite) + str(Dgreen) + tiled + tiled + tiled * maior + tiled + tiled + str(Twhite))
    time.sleep(3)

def error_dialog(text='', tiled='='):
    clear();
    print(os.popen('figlet MID-PAINEL').read())
    text = text.split('\n')
    maior = 0
    for txt in text:
        tamanho = len(txt)
        if tamanho > maior:
            maior = tamanho
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    for txt in text:
        print(str(error) + ' ' + txt + ' ' + str(error))
    print(str(Twhite) + str(Ired) + tiled * 8 + tiled * maior + tiled * 8 + str(Twhite))
    time.sleep(3)


requests = requests.Session();result = os.popen('figlet MID-PAINEL').read()

try:
    if __name__ == '__main__':
        dialog('Buscando atualizações ...')
        update = subprocess.check_output('git pull', shell=True)
        if 'Already up to date' not in update.decode():
            dialog('Atualização instalada.\nReiniciando o painel.')
            restart()
        else:
            print(f'{Twhite}[{Nyellow}i{Twhite}] Nenhuma atualização disponivel.')
            time.sleep(2)
except:
    if os.path.exists('.git'):
        pass
    else:
        error_dialog('Falta de repositório GIT local')

try:
    subprocess.check_output('apt update -y', shell=True)
    os.system("apt install figlet curl -y")
except:
    os.system("pacman -Sy figlet curl")

Sair = False
while Sair == False:
    try:
        banner.menu()
        opc = int(input(f'{Dgreen}Digite o numero da opção que deseja: \n>>>'))
    except:
        error_dialog('Caracteres não reconhecidos');
        op = None
    clear()

    if opc == 1:     # NOME
        nome.consultar()
    if opc == 2:   # CPF
        cpf.consultar()
    elif opc == 3:   # CEP
        cep.consultar()
    elif opc == 4:   # Placa
        placa.consultar()
    elif opc == 5:   # CNPJ
        cnpj.consultar()
    elif opc == 6:   # IP
        ip.consultar()
    elif opc == 7:   # Meu IP
        meuip.consultar()
    elif opc == 8:   # Covid Info
        covid19.consultar()
    elif opc == 9:   # Root Checker
        root.consultar()
    elif opc == 10:   # Atualizar painel
        os.popen('cd database && bash update.sh');
        dialog('Reiniciando o painel...');
        restart()
    elif opc == 11:  # Sair
        Sair = True
    elif opc == 12:  # Criador
        os.system('termux-open-url https://wa.me/5512988789266')
    elif opc == 13:  # Grupo
        os.system('termux-open-url https://discord.gg/kgXhZzGJDY')
    elif opc == None:
        pass
    else:
        error_dialog('Opção incorreta')
