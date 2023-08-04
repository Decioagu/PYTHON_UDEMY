"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

# variáveis globais
palavra_secreta = 'Decio'.upper()
letras_da_palavra_secreta_descobertas = ''
contador_de_tentativas = 0
loop = True

os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

print()
print(' Palavra secreta '.center(30, '=')) # centralizar título

# corpo principal do programa (loop infinito) 
while loop:
    print('-' * 30)
    # entrada do usuário
    digito = input('Digite uma letra: ').upper()
    contador_de_tentativas += 1
    # variavel local
    palavra_formada = ''

    print()
    # condição verdadeira 'digito'
    if len(digito) <= 1:
        
        # armazena letras contida na palavra secreta
        if digito in palavra_secreta:
            letras_da_palavra_secreta_descobertas += digito

        # percorre as letras da 'palavra_secreta'
        for letra in palavra_secreta:
            # se letra existir exiba a letra
            if letra in letras_da_palavra_secreta_descobertas:
                print(letra,end='')
                palavra_formada += letra # auxilia na comparação da 'palavra_secreta'
                # condição para finalizar (loop infinito)
                if palavra_formada == palavra_secreta:
                    loop = False
            # se letra NÂO existir exiba '*'
            else:
                print('*', end='')   
    # condição falsa 'digito'
    else:
        # mensagem de erro
        print('Digite apenas uma letra por vez.')
    # mensagem ao final do loop
    print()
    print(f'\n{contador_de_tentativas}ª tentativa')

# mensagem final (termino do programa)
print('-' * 30) 
print(f'\nParabéns você descobriu a palavra secreta!\n')

