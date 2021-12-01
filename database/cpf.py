## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'  # Preto
Ired = '\033[1;31m'  # Vermelho
Dgreen = '\033[1;32m'  # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'  # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'  # Ciano
Twhite = '\033[1;37m'  # Branco
VRCRM = '\033[0;0m'  # Remover

import os
import requests


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## #################### ##########')
    print('########## ### Consulta CPF ### ##########')
    print('########## #################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            cpf_input = str(input(f'\n{Hcyan}Digite o CPF para consulta: ')).strip().lower()
            if len(cpf_input) > 11:
                print(f'{Ired}!!! {Nyellow}CPF Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'http://ghostcenter.xyz/api/cpf/{cpf_input}')
        rjson = request.json()
    
        if rjson['status'] == 404:
            restart = str(input(
                f'{Ired}==> CPF NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> CPF ENCONTRADO <=={Nyellow} '))
            ordem = 0
            i = rjson['dados']
            ordem += 1
            print(f'\n{Dgreen}{ordem} PESSOA:{Nyellow}')
            print(f" CPF        >>> {i['cpf']}")
            print(f" Nome       >>> {i['nome']}")
            print(f" Nascimento >>> {i['nascimento']}")
            print(f" Sexo       >>> {i['sexo']}\n")
    
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
