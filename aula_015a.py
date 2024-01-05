'''
    # Exercício - Lista de tarefas com desfazer e refazer
    # Música para codar =)
    # Everybody wants to rule the world - Tears for fears
    # todo = [] -> lista de tarefas
    # todo = ['fazer café'] -> Adicionar fazer café
    # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
    # desfazer = ['fazer café',] -> Refazer ['caminhar']
    # desfazer = [] -> Refazer ['caminhar', 'fazer café']
    # refazer = todo ['fazer café']
    # refazer = todo ['fazer café', 'caminhar']
'''
import json
import os # importar modulo "os"
os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

# variáveis globais
lista_auxiliar = [] # lista auxiliar
lista_usuario = [] # lista principal
loop = True

#-------------------------------------------------------------
# (função) adicionar itens nas listas "lista_auxiliar" e "lista_usuario"
def adicionar(t):

    if t == '': # se "t" for vazio ou nulo
        print('Favor adicionar uma tarefa na lista.')
    else:
        if t not in lista_auxiliar: # se "t" não estiver na lista "lista_auxiliar"
            lista_auxiliar.append(t)
        if t not in lista_usuario: # se "t" não estiver na lista "lista_usuario"
            lista_usuario.append(t)
            print('Tarefa adicionada com sucesso.')
        else: # se "t" ja estiver na lista "lista_usuario"
            print()
            print(f'Esta tarefa já esta na lista.')
    print('-' * 40)

#-------------------------------------------------------------
# (função) excluir itens da "lista_usuario" 
def  excluir(t):

    try:
        lista_usuario.remove(t) # exclui itens pelo nome da "lista_usuario"
    except ValueError: # se "t" não estiver na "lista_usuario"  mostra lista 
        print()
        print(f'LISTA DE TAREFA:')
        print('* ', end='')
        print(*lista_usuario, sep='\n* ')
        print()
        print(f'Tarefa digitada não consta na lista => "{t}"')
    else:
        print('Tarefa eliminada com sucesso.')
    finally:
        print('-' * 40)

#-------------------------------------------------------------
# (função) desfazer utilizar "lista_auxiliar" para reintegras itens excluídos na "lista_usuario"
def desfazer():
    
    confirmacao = True # variável auxilia na verificação do conteúdo das listas "lista_usuario" e "lista_auxiliar"

    for index, item in enumerate(lista_auxiliar):
        # OBS: lista_auxiliar[(len(lista_auxiliar)-1) faz interação da lista "lista_auxiliar" de trás para frente
        if lista_auxiliar[(len(lista_auxiliar)-1)- index] not in lista_usuario:
            # adiciona um elemento da "lista_auxiliar" para "lista_usuario" se houver diferença
            lista_usuario.append(lista_auxiliar[(len(lista_auxiliar)-1)- index])
            print(f'Adicionada novamente tarefa => "{lista_auxiliar[(len(lista_auxiliar)-1)- index]}"')
            confirmacao = False
            break # interrompe o loop "for"

    if confirmacao: # se conteudo das lista "lista_auxiliar" e "lista_usuario" forem iguais
        print('Não existe tarefa para retornar')
    print('-' * 40)
#-------------------------------------------------------------
# (função) sair do programa
def opcao_saida(msg):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar os valores "S" ou "N" para variável "op"
    
    :msg : texto descrito pelo usuário 
    :op: Variável recebe somente os valores "S" ou "N"
    :return: Retorna True ou False
    """
    while True:
        op = input(msg).strip().upper()
        if op == 'S':
            print('-' * 40)
            return False
        elif op == 'N':
            print('-' * 40)
            return True
        else:
            print()
            print(f'Opção invalida!')
            print(f'Digite [s] para SAIR ou [n] para CONTINUAR.')
    
#-------------------------------------------------------------
# corpo principal
print('\t     LISTA DE TAREFA')
while loop:

    menu = '''
    ************* MENU *************
    [1] = Ver lista de tarefa
    [2] = Adicionar lista de tarefas
    [3] = Excluir ultima tarefa
    [4] = Refazer ultima tarefa
    [5] = Limpar tela
    [6] = Sair
    ********************************
        '''
    print(menu)
    print('-' * 40)
    opcao = input('Escolha uma opção do menu acima:')

    # "MENU" de opções
    if opcao == '1': # Ver lista de tarefa
        print()
        print(f'LISTA DE TAREFA:')
        if lista_usuario == []:
            print('Lista esta vazia...')
        else:
            print('* ', end='')
            print(*lista_usuario, sep='\n* ')
        print('-' * 40)

    elif opcao == '2': # Adicionar lista de tarefas
        print()
        tarefa = input('Digite sua tarefa: ')
        adicionar(tarefa.upper().strip())

    elif opcao == '3': # Excluir ultima tarefa
        print()
        tarefa = input('Informe o nome da tarefa a excluir: ')
        excluir(tarefa.upper().strip())

    elif opcao == '4': # Refazer ultima tarefa
        print()
        desfazer()

    elif opcao == '5': # Limpar tela
        os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

    elif opcao == '6': # Sair
        print()
        loop = opcao_saida(f'Deseja sair? [S/N]')
        
    else: # Qualquer outra escolha que não há na lista 
        print()
        print('Opção invalida.')
        print('-' * 40)


print()
print('PROGRAMA FINALIZADO COM SUCESSO')