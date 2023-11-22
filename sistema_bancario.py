deposito = 0
saque = 0
extrato = []
saldo = 0
LIMITE_DE_SAQUE = 500
LIMITE_DE_SAQUE_DIARIO = 3
loop = True

apresentacao = ' SISTEMA BANCÁRIO '

print(apresentacao.center(50, '*'))

while loop:
    menu =  '''\n
            Menu de opções:
            [d] DEPOSITO
            [s] SAQUE
            [e] EXTRATO
            [f] FINALIZAR\n
            '''
    print(menu)
    opcao = input('Escolha uma opção:')

    if opcao == 'd':
        try:
            deposito = float(input('Digite o valor de deposito'.strip()))
            if deposito == '':
                print('Deposito não realizado, valor nulo.')
            elif deposito < 0:
                print('Deposito não realizado, valor não pode ser negativo.')
            else:
                saldo = deposito
                extrato = extrato.append(f'Deposito = R$:{deposito:.2f}')


        except Exception as erro:
            # mesagem de erro para valores não validos
            print(f'\nErro de operação => ({erro})')
            print('Verifique o valor digitado!!!')

    elif opcao == 's':
        break
    elif opcao == 'e':
        break
    elif opcao == 'f':
        # opções para encerra loop e finalizar programa
        while True:
            # entrada de parametro do usuário
            loop = input('\nDeseja realizar outra operação Sim = [s] ou Não = [n]:')
            loop = loop.lower()

            # resposta para usuário
            if loop == 's':
                loop = True
                break
            elif loop == 'n':
                loop = False
                break
            else:
                # mensagem de erro caso  a resposta não seja Sim [s] ou Não [n]
                loop = True
                print('\nOpeção invalida!!! \nDigite [s] para continuar outra operação ou [n] para saiar')
    else:
        # caso usuário digite qualquer opção não existente no "Menu de opções" 
         print('\nOpção invalida, digite a letra correspondente ao menu de opções:\n')

print('\nSistema finalizado com sucesso!!!\n')
