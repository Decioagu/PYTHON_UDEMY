# Exercício - sistema de perguntas e respostas

import os # importar modulo "os"
os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

# lista com dicionários
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2= ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5= ',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2= ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print()
print(' Perguntas e respostas '.center(100, '=')) # centralizar título

# acesso da lista "preguntas" com índice
for index1, p in enumerate(perguntas):

    # "Perguntas" esta sendo acessada na lista dentro do dicionário
    print(perguntas[index1]['Pergunta'])
    print()
    print('Escolha uma opção abaixo:')

    # "Opções" esta sendo acessada na lista dentro do dicionário
    for index2, o in enumerate(perguntas[index1]['Opções'], start=1):
        print(f'{index2}) {o}')
    print()
    
    resposta = input('Resposta: ') # resposta do usuário
    try:
    resposta -= 1
    # resposta ao usuário
    if resposta == perguntas[index1]['Resposta']: # Certo
        print('Certa a resposta!')
    else: # Errado
        print(f'Errouuuu... Resposta certa é',perguntas[index1]['Resposta'])
    print('-'*100)

print()
# mensagem final (termino do programa)
print('Programa finalizado!!!') 
print()