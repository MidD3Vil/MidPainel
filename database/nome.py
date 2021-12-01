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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## ##################### ##########')
    print('########## ### Consulta Nome ### ##########')
    print('########## ##################### ##########')
    restart = 'S'
    while restart == 'S':
        while True:
            nome_input = str(input(f'\n{Hcyan}Digite o Nome para consulta: ')).strip().lower()
            if '0' in nome_input:
                print(f'{Ired}!!! {Nyellow}Nome Inválido {Ired}!!!')
            else:
                break
        request = requests.get(f'http://ghostcenter.xyz/api/nome/{nome_input}')
        rjson = request.json()
    
        if rjson['status'] == 404:
            restart = str(input(
                f'{Ired}==> NOME NÃO ENCONTRADO <== \n\n\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
            clear()
        else:
            print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> NOME ENCONTRADO <=={Nyellow} '))
            print('\nINFO:')
            print(f'Nomes Encontrados: {rjson["total"]}\n')
    
            campos = ['nome', 'cpf', 'nascimento', 'sexo']
            ordem = 0
            # para cada item do arquivo json
            for i in rjson['dados']:
                ordem += 1
                print(f'{Dgreen}{ordem} PESSOA:{Nyellow}')
                print(f" Nome       >>> {i['nome']}")
                print(f" Nascimento >>> {i['nascimento']}")
                print(f" CPF        >>> {i['cpf']}")
                print(f" Sexo       >>> {i['sexo']}\n")
    
            print('')
            print(f'\033[1;33m-' * 48)
            restart = str(input(
                f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
                0]
            clear()
