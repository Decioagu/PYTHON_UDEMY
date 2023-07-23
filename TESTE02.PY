while True:
    entrada_num = num
    num = num.replace(',', '.')
    teste = num
    if num == '':
        print(end='')
        num = input(f'Digite um valor numérico: ').strip()
    else:
        if teste.count('-') <= 1:
            teste = teste.replace('-', '')
            if teste.count('.') <= 1:
                teste = teste.replace('.', '')
                if teste.isnumeric() == True:
                    if teste == '0':
                        num = teste
                        num = float(num)
                        break
                    else:
                        num = float(num)
                        break
                else:
                    print()
                    print(f'Erro...')
                    print(f'Caractere "{entrada_num}" não é valido.')
                    num = input(f'Digite um valor numérico: ').strip()
            else:
                print()
                print(f'Erro...')
                print(f'Caractere "{entrada_num}" não é valido.')
                num = input(f'Digite um valor numérico: ').strip()
        else:
            print()
            print(f'Erro...')
            print(f'Caractere "{entrada_num}" não é valido.')
            num = input(f'Digite um valor numérico: ').strip()
    return num if not formatação else f'{num}'.replace('.', ',')
real = input('Número = ').strip()
real = teste_float(real)
print(f'Número real = {real}')
print(f'{type(real)}')