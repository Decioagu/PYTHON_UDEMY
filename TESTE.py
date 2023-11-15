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