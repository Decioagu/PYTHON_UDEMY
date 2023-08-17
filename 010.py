# Exercício - sistema de perguntas e respostas

import emoji # importar modulo "emoji"
import os # importar modulo "os"
os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

contador_de_acertos = 0

# lista com dicionários
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
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
    for index2, o in enumerate(perguntas[index1]['Opções'], start=1): # enumera índice a partir de 1 (OBS: somente para exibição)
        print(f'{index2}) Resposta = {o}')
    print()
    
    # tente
    try:
        # resposta ao usuário
        resposta = int(input('Escolha uma opção: '))
        resposta -= 1 # corrige resposta do usuário conforme posição no índice na lista "Opções"
        
        print()
        if perguntas[index1]['Opções'][resposta] == perguntas[index1]['Resposta']: # mensagem de acreto
            print('Certa a resposta!', emoji.emojize(':thumbs_up:'))
            contador_de_acertos += 1
        else: # mensagem de erro
            print('Errouuuu...', emoji.emojize(':face_with_symbols_on_mouth:'), f'\nResposta certa é', perguntas[index1]['Resposta'])

        print('-'*100)

    except IndexError: # mensagem de erro quando número digitado não esta no range da lista 
        print(f'"{resposta + 1}" NÃO consta na lista de opções')
        print('Escolha um número de 1 à 4 conforme lista de opções')
        print('-'*100)
    except ValueError: # mensagem de erro quando o que foi digitado não for um número inteiro
        print(f'\nDigite um valor dentro das opções numéricas de 0 à 3')
        print('-'*100)
    except Exception as erro: # informa algum tipo de erro não previsto
        print(erro.__class__, erro) 

print()
# mensagem final para usuário (termino do programa)
print(f'Você teve {contador_de_acertos} acerto!!!', emoji.emojize(':face_with_steam_from_nose:')) if contador_de_acertos <= 1 else print(f'Parabéns, você teve {contador_de_acertos} acertos!!!', emoji.emojize(':smiling_face_with_hearts:'))
print()
print('Programa finalizado!!!')
print()