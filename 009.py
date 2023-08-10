"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import os # importar modulo "os"
os.system('cls') # limpa o terminal iniciando o programa (SISTEMA OPERACIONAL)

print()
print(' Calculadora de digito CPF '.center(60, '=').upper()) #  título centralizado
print()

# variáveis globais
contador_para_primeiro_digito = 10
contador_para_segundo_digito = 11
soma_de_valores = 0 
cpf_formatado = ''

# entrada do usuário com tratamento
cpf = input('Digite os primeiros (9) números do seu cpf: ').strip().replace('.', '').replace('-', '')

# garante que apenas os primeiros (9) dígitos seja armazenados
cpf = cpf[:9]


if cpf.isnumeric(): # testa se foi digitado apenas números

    # regra de negócio (1)
    for num in cpf:
        multiplicacao_de_valores = int(num) * contador_para_primeiro_digito # multiplica valores digitados com contador regressivo
        soma_de_valores += multiplicacao_de_valores # soma e armazena os valores da "multiplicacao_de_valores"
        contador_para_primeiro_digito -= 1 # subtrai valor do contador regressivo

    multiplica_por_10 = soma_de_valores * 10 # multiplica "soma_de_valores" por 10

    resultado_digito_1 = multiplica_por_10 % 11 # armazena resto da divisão "multiplica_por_10" por 11

    print()
    # resposta conforme valor obtido de "resultado_digito_1" 
    if resultado_digito_1 > 9:
        resultado_digito_1 = 0
        print(f'Primero digito = {resultado_digito_1}') 
    else:
        print(f'Primero digito = {resultado_digito_1}')

    cpf += str(resultado_digito_1) # concatena "resultado_digito_1" 

    soma_de_valores = 0 # zera o valor da variável global para segunda operação "regra de negócio (2)"
    
    # ----------------------------------------------------------------------------
    
    # regra de negócio (2)
    for num in cpf:    
        soma_de_valores += (int(num) * contador_para_segundo_digito) # soma e armazena dos valores multiplicados
        contador_para_segundo_digito -= 1 # subtrai valor do contador regressivo

    resultado_digito_2 = (soma_de_valores * 10) % 11 # armazena resto da divisão (soma_de_valores * 10) por 11

    print()
    # resposta conforme valor obtido
    if resultado_digito_2 > 9:
        resultado_digito_2 = 0
        print(f'Primero digito = {resultado_digito_2}')
    else:
        print(f'Primero digito = {resultado_digito_2}')

    cpf += str(resultado_digito_2) # concatena "resultado_digito_2"

    # ----------------------------------------------------------------------------

    # regra para formata exibição do cpf
    for enumer, c in enumerate(cpf, start=1):
        cpf_formatado += c
        if enumer == 3:
            cpf_formatado += '.'
        elif enumer == 6:
            cpf_formatado += '.'
        elif enumer == 9:
            cpf_formatado += '-'
    
    # exibir cpf em "string" formatado
    print(f'\nCPF = {cpf_formatado}\n') # resposta final ao usuário
   
else:
    # resposta de erro para usuário
    print('\nDigite apenas valores numéricos!!!\n')
