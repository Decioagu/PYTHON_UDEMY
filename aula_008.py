'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
'''
import os # importar modulo "os"

# variavel global
lista = ['Arroz', 'Feijão', 'Macarrão', 'Leite']
loop = True

os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

print()
print(' Lista de compra '.center(60, '=')) #  título centralizado
print()

# corpo principal do programa (loop infinito) 
while loop:
    # mensagem "Menu de opções"
    menu = '''
            Menu de opções:
            [1] INSERIR ITEM NA LISTA
            [2] APAGAR ITEM DA LISTA
            [3] VER LISTA
            [4] SAIR
           '''

    print('-' * 60)
    print(menu) # exibir "Menu de opções"

    opcao = input('Digite opção no menu: ') # entrada do usuário

    # regras de negócio
    if opcao == '1': # "Menu de opções" = [1] INSERIR ITEM NA LISTA
        print()
        adicionar = input('Adicione um item à lista: ').capitalize() # entrada do usuário
        print()
        lista.append(adicionar) # adicionar na lista
        print(f'Adicionado "{adicionar}" na lista') # mensagem de confirmação para usuário

    elif opcao == '2':  # "Menu de opções" = [2] APAGAR ITEM DA LISTA
        print()
        print(' Lista de compra '.center(60, '-')) #  título centralizado
        print()
        print(lista) # exibir lista
        print()
        remover = input('Digite o nome do item para remover da lista: ').capitalize() # entrada do usuário
        # tente executar
        try:
            lista.remove(remover) # remover item da lista pelo nome
            print()
            print(f'Removido "{remover}" da lista') # mensagem de confirmação para usuário
        except ValueError:
            print()
            print(f'Não possui "{remover}" na lista.') # mensagem de erro para usuário

    elif opcao == '3': # "Menu de opções" = [3] VER LISTA
        print()
        print(' Lista de compra '.center(60, '-')) #  título centralizado
        print()
        print(lista) # exibir lista
        print()

    elif opcao == '4': # "Menu de opções" = [4] SAIR

        while True:
            op = input('Deseja sair do programa Sim [s] ou Não [n]: ').strip().upper() # entrada do usuário
            # regras de negócio
            if op in 'S':
                loop = False
                print()
                break
            elif op in 'N':
                print()
                break
            # mensagem de erro para usuário
            else:
                print()
                print(f'Opção invalida!')
                print(f'Digite [s] para Sair ou [n] para CONTINUAR.')
                print()
    else:
        print()
        print('Opção escolhida invalida, tente novamente.') # mensagem de erro para usuário
        print()

# mensagem final (termino do programa)
print('-' * 60)
print()
print('Programa finalizado!!!') 
print()