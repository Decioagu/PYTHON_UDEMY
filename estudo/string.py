# Metodos String

# 01. capitalize()
# Capitalizar uma palavra
name = "tERMINAL"
print(f'\n01. {name.capitalize()}\n') # Saída: Terminal

# 02.casefold()
# Converte para minúsculas
name = "tERMINAL"
print(f'02. {name.casefold()}\n' ) # Saída: terminal

# 03. center()
# Adicionar caractere no início e no final para totalizar uma quantidade
name = "Terminal"
print( f'03. {name.center(12, "-")}\n' ) # Saída: --Terminal--

# 04. count()
# Retorna a quantidade de vezes que um caractere se repete
name = "casa"
print( f'04. {name.count("a")}\n' ) # Saída: 2

# 05. endswith()
# Retorna True(Verdadeiro) se uma string terminal com uma string indicada
name = "Terminal"
print( f'05. {name.endswith("nal")}\n' ) # Saída: True

# 06. find()
# Retorna a 1º posição da letra/string desejada
name = "Terminal"
print( f'06. {name.find("i")}\n' ) # Saída: 4
