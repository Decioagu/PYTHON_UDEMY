# mensagem de boas vindas
apresentacao = ' SISTEMA BANCÁRIO '
print()
print(apresentacao.center(60, '*'))
print()

def depositar(saldo_depositar, extrato_depositar):
    try:
        print()
        # entrada de parametro do usuário
        deposito = float(input('Digite o valor de deposito: '))

        # tomada de desisão (regrade negócio)
        if deposito <= 0:
            print('Deposito NÃO realizado, deposito menor ou igual a R$:0.00.')
            return saldo_depositar
        else:
            saldo_depositar += deposito
            texto = str(f'Deposito = R$:{deposito:.2f}')
            extrato_depositar.append(texto)
            print('Deposito realizado com sucesso!!!')
            return saldo_depositar
            

    # mesagem de erro para valores não validos
    except Exception as erro:
        print(f'\nErro de operação => ({erro})')
        print('Verifique o valor digitado!!!')
        return saldo_depositar


def sacar(saldo_sacar, extrato_sacar, limite_de_saque_diario_sacar, LIMITE_DE_SAQUE_sacar):
    try:
        print()
        # entrada de parametro do usuário
        saque = float(input('Digite o valor de saque: '))

        # tomada de desisão (regrade negócio)
        if limite_de_saque_diario_sacar >= 3:
            print('Saque NÃO realizar, já foi atigindo limite diario de (3 saques diário).\n')
            return saldo_sacar, limite_de_saque_diario_sacar
        elif saque > LIMITE_DE_SAQUE_sacar:
            print('Saque NÃO realizar seu limite para saque é de R$:500,00.\n')
            return saldo_sacar, limite_de_saque_diario_sacar
        elif saque > saldo_sacar:
            print('Saque NÃO realizar, saldo insuficiente.\n')
            return saldo_sacar, limite_de_saque_diario_sacar
        elif saque <= 0:
            print('Saque NÃO realizar, saque menor ou igual a R$:0.00.\n')
            return saldo_sacar, limite_de_saque_diario_sacar
        else:
            limite_de_saque_diario_sacar += 1
            saldo_sacar -= saque
            texto = str(f'  Sacado = R$:{saque:.2f}')
            extrato_sacar.append(texto)
            print('Saque realizado com sucesso!!!')
            return saldo_sacar, limite_de_saque_diario_sacar

    # mesagem de erro para valores não validos
    except Exception as erro:
        print(f'\nErro de operação => ({erro})')
        print('Verifique o valor digitado!!!')
        return saldo_sacar, limite_de_saque_diario_sacar

def extrato_bancario(saldo_extrato, extrato_extrato):
    print()
    print(' Exetrato bancario '.center(25, '#'))
    print('-' * 25)
    if extrato_extrato == []:
        print('Saldo total R$:0.00')
    else:
        for i in extrato_extrato:
            print(i)
        print('-' * 25)
        print(f'Saldo total R$:{saldo_extrato:.2f}')

def cadastro_usuario():
    cpf = ''
    nome =''
    data_de_nacimento = ''
    endereco = {'logradouro': '', 'numero': '', 'bairro': '', 'cidade': '', 'estado': ''}

def op(loop_op):
    # opções para encerra loop e finalizar programa
    while True:
        # entrada de parametro do usuário
        loop_op = input('\nDeseja finalizar Sim = [s] ou Não = [n]:').lower()

        # resposta para usuário
        if loop_op == 's':
            loop_op = False
            break
        elif loop_op == 'n':
            loop_op = True
            break
        else:
            # mensagem de erro caso  a resposta não seja Sim [s] ou Não [n]
            loop_op = True
            print('\nOpeção invalida!!! \nDigite [s] para FINALIZAR ou [n] RETORNAR')
    return loop_op

def main():
    # Variaveis globais
    deposito = 0
    saque = 0
    extrato = []
    saldo = 0
    LIMITE_DE_SAQUE = 500
    limite_de_saque_diario = 0
    loop = True
    usuario = []
    conta_usuario = []
    
    # loop do sistema bancário
    while loop:
        menu =  '''
============================================================
                    Menu de opções:
                    [1] DEPOSITO
                    [2] SAQUE
                    [3] EXTRATO
                    [4] CADASTRO CLIENTE
                    [5] ABRIR CONTA 
                    [6] LISTAR DE CLENTE
                    [7] FINALIZAR
                '''
        # exibir menu de opções
        print(menu)

        # entrada de parametro do usuário
        opcao = input('Escolha uma opção:').lower()
        print('=' * 60)

        # Menu de opções = DEPOSITO
        if opcao == '1':
            # retorna "saldo" pela função "deposito"
            saldo = depositar(saldo, extrato)
            
        # Menu de opções = SAQUE
        elif opcao == '2':
            # retorna "saldo" e "limite_de_saque_diario" pela função "sacar"
            resposta_funcao_sacar = sacar(saldo, extrato, limite_de_saque_diario, LIMITE_DE_SAQUE)

            # função "sacar" retorna uma Tupla, "saldo" e "imite_de_saque_diario" necessário tratar p/ alimenta variaval
            for indice, res in enumerate(resposta_funcao_sacar):
                if indice == 0:
                    # alimentar "saldo" com retorno da função "sacar"
                    saldo = res
                else:
                    # alimentar "limite_de_saque_diario" com retorno da função "sacar"
                    limite_de_saque_diario = res


        # Menu de opções = EXTRATO
        elif opcao == '3':
            # retorna "extrato" da função "extrato_bancario"
            extrato_bancario(saldo, extrato)



        # Menu de opções = FINALIZAR
        elif opcao == '7':
            loop = op(loop)
            
        else:
            # caso usuário digite qualquer opção não existente no "Menu de opções" 
            print('Opção invalida, digite a letra correspondente ao menu de opções:')

main()

print('\nSistema finalizado com sucesso!!!\n')
