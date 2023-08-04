'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebe com
erros de ídices inexistentes na lsiata.
'''
import os

lista = ['Arroz', 'Feijão', 'Macarrão', 'Leite']
loop = True

os.system('cls')
print()
print(' Lista de compra '.center(60, '='))
print()

while loop:
    menu = '''
            Menu de opções:
            [1] INSERIR ITEM NA LISTA
            [2] APAGAR ITEM DA LISTA
            [3] VER LISTA
            [4] SAIR
           '''

    print('-' * 60)
    print(menu)

    opcao = input('Digite opção no menu: ')

    if opcao == '1':
        print()
        adicionar = input('Adicione um item à lista: ').capitalize()
        print()
        lista.append(adicionar)
        print(f'Adicionado "{adicionar}" na lista')
    elif opcao == '2':
        print()
        print(' Lista de compra '.center(60, '-'))
        print()
        print(lista)
        print()
        remover = input('Digite o nome do item para remover da lista: ').capitalize()
        try:
            lista.remove(remover)
            print()
            print(f'Removido "{remover}" da lista')
        except Exception as erro:
            print()
            print(f'Não possui "{remover}" na lista.')
    elif opcao == '3':
        print()
        print(' Lista de compra '.center(60, '-'))
        print()
        print(lista)
        print()
    elif opcao == '4':

        while True:
            op = input('Deseja sair do programa Sim [s] ou Não [n]: ').strip().upper()
            if op in 'S':
                loop = False
                print()
                break
            elif op in 'N':
                print()
                break
            else:
                print()
                print(f'Opção invalida!')
                print(f'Digite [s] para Sair ou [n] para CONTINUAR.')
                print()
    else:
        print()
        print('Opção escolhida invalida, tente novamente.')
        print()

print('-' * 60)
print()
print('Programa finalizado!!!')
print()