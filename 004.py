"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('\nQual é o seu nome? ')

if nome == '':
    print('\nO que foi? Não quer falar...\n')
elif 0 <len(nome) <= 4:
    print('\nSeu nome é curto!!!\n')
elif 5 <= len(nome) <= 6:
    print('\nSeu nome é normal!!!\n')
else:
    print('\nSeu nome é grande!!!\n')
