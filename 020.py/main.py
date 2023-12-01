import uma_linha # importar modulo

print('===================================================================')
print(dir(uma_linha)) # retorna uma lista de todos os atributos e métodos de um objeto.
print('===================================================================')
print(uma_linha.__file__) # acesso ao caminho do módulo
print('===================================================================')
print(uma_linha.__name__) # acesso ao nome do módulo
print('===================================================================')
print(uma_linha.__doc__) # acesso descrição do módulo "se houver"
print('===================================================================')
print(uma_linha.variavel) # acessa variável dentro do módulo uma_linha 
print('===================================================================')
print(uma_linha.funcao()) # acessa função dentro do módulo uma_linha
print('===================================================================')
help(uma_linha) # descreve informações do módulo
