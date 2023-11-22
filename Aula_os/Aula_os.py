# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os

os.system('clear') # limpa o terminal
os.system('echo "Hello world"') # repete o texto como um print()
#-----------------------------------------------------------------------------------------------

# pasta
'''
A função os.path.join() é uma função embutida do Python que é usada para concatenar 
vários segmentos de caminho em um único caminho. Os segmentos de caminho são 
especificados como uma sequência de strings, separadas por vírgulas.

A função os.path.join() usa o separador de caminho da plataforma como delimitador 
para concatenar os segmentos de caminho. No Windows, o separador de caminho é "\", 
enquanto no Unix e no macOS é "/".
'''

import os

# unir o texto conforme sistema operacional
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
print(os.path.dirname(caminho)) # exibir diretório
print(os.path.basename(caminho)) # exibir arquivo


print('<==========================================================>')

# separar diretório do arquivo
diretorio, arquivo = os.path.split(caminho)
print(diretorio) # exibir diretório
print(arquivo) # exibir arquivo

print('<==========================================================>')

# separar nome do arquivo de sua extensão
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo)
print(extensao_arquivo)

print('<==========================================================>')

print(os.path.exists('Z:\REPOSITORIO\PUBLICO\PYTHON_UDEMY\Aula_os')) # caminho existe (True ou False)
print(os.path.abspath('.')) # mostrar caminho atual onde programa é executado
 
print('<==========================================================>')

#aula 283
'''
    A função listdir() em Python é usada para listar o conteúdo de um diretório. 
    Ela retorna uma lista de strings contendo os nomes dos arquivos e diretórios 
    no diretório especificado.

    A função isdir() do módulo os.path do Python é usada para verificar se um caminho 
    especificado é um diretório existente ou não. Ela retorna True se o caminho for um 
    diretório existente e False caso contrário.
'''

import os

caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os', 'exemplo')
# caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os')

for pasta in os.listdir(caminho): 
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for itens in os.listdir(caminho_completo_pasta):
        print('  ', itens)
    
print('<==========================================================>')

import os
from itertools import count

caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        
        # os.unlink(caminho_completo_arquivo) # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)