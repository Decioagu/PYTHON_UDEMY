'''
Desafio proposto é a criação de uma CACULADORA com "quatro oprações" para calcular duas variáveis.
'''

print('\n--- CAUCULADORA ---')
# continuar loop de operação
continuar_loop = True

# loop de operação matemática "CAUCULADORA"
while continuar_loop:
    # mensagem de opeções validas
    print('\nOPERADORES:')
    print('1 - MULTIPLICAÇÃO')
    print('2 - DIVISÃO')
    print('3 - SOMA')
    print('4 - SUBRITAÇÃO')

    # tente realizar operação conforme entrada do usuário
    try:
        # entrada de parametro do usuário
        operado_int = int(input('\nEscolha o número referente ao operador de sua escolha: '))
        primeiro_numero_float = float(input('\nEscolha o primeiro valor: '))
        segundo_numero_float = float(input('\nEscolha o segundo valor: '))
        print()

        # menu de "OPERADORES"
        if operado_int == 1:
            print(f'{primeiro_numero_float} * {segundo_numero_float} = {primeiro_numero_float * segundo_numero_float}')
        elif operado_int == 2:
            print(f'{primeiro_numero_float} / {segundo_numero_float} = {primeiro_numero_float / segundo_numero_float}')
        elif operado_int == 3:
            print(f'{primeiro_numero_float} + {segundo_numero_float} = {primeiro_numero_float + segundo_numero_float}')
        elif operado_int == 4:
            print(f'{primeiro_numero_float} - {segundo_numero_float} = {primeiro_numero_float - segundo_numero_float}')
        else:
            # mensagem de erro caso operação escolhida não exista "OPERADORES"
            print(f'Você digitou "{operado_int}".')
            print('O número do operador digitado não consta na lista "OPERADORES".\n')

        # opções para encerra loop e finalizar programa 
        while True:
            # entrada de parametro do usuário
            continuar_loop = input('\nDeseja realizar outra operação Sim = [s] ou Não = [n]:')
            continuar_loop = continuar_loop.lower()

            # resposta para usuário
            if continuar_loop == 's':
                continuar_loop = True
                break
            elif continuar_loop == 'n':
                continuar_loop = False
                break
            else:
                # mensagem de erro caso  a resposta não seja Sim [s] ou Não [n]
                continuar_loop = True
                print('\nOpeção invalida!!! \nDigite [s] para continuar outra operação ou [n] para saiar')

    except Exception as erro:
        # mesagem de erro para valores não validos
        print(f'\nErro de operação => ({erro.__class__} : {erro})')
        print('Verifique o valor digitado!!!')

print('\nPrograma finalizado...\n')