"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('\nDigite um número inteiro: ')
# Tente converter "numero_str" em um número inteiro "numero_int"
try:
    # converter para número inteiro
    numero_int = int(numero_str)
    
    if numero_int % 2 == 0:
        print(f'"{numero_str}" é PAR.\n')
    else:
        print(f'"{numero_str}" é IMPAR.\n')      
except:
    print(f'"{numero_str}" NÃO É um NÚMERO INTEIRO.\n')


