usuario = []

def cadastro_usuario():
    try:
        cpf = input('Digite o seu CPF: ').strip().replace('.', '').replace('-', '')
        if len(cpf) != 11:
            print('\nErro de operação "CPF INVALIDO"')
            print('Todo CPF possui 11 digitos!')
            cadastro_usuario()
    except Exception as erro:
        print(f'\nErro de operação => ({erro})')
        print('Digite apenas numeros')
        cadastro_usuario()
    
    # nome =''
    # data_de_nacimento = ''
    # endereco = {'logradouro': '', 'numero': '', 'bairro': '', 'cidade': '', 'estado': ''}

cpf = cadastro_usuario()
print(cpf)

