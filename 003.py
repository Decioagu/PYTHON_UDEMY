"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print("\nBom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.\n")
hora_str = input('Que horas são? ')

try:
    hora_int = int(hora_str) 
    if hora_int < 0:
        print('\nNão existe hora negativa.\n')
    elif 0 <= hora_int <= 11 :
        print('\nBom dia!!!\n')
    elif 12 <= hora_int <= 17 :
        print('\nBoa tarde!!!\n')
    elif 18 <= hora_int <= 23 :
        print('\nBoa noite!!!\n')
    else:
        print('\nPassou das 23...\n')
except:
    print('\nFavor digite um NÚMERO INTEIRO!\n')