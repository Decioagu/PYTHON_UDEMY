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
caminho = ('Z:\\REPOSITORIO\\PUBLICO\\PYTHON_UDEMY\\Aula_os\\exemplo')


print('<==========================================================>')

# separar diretório do arquivo
arquivo = os.path.split(caminho)
print(arquivo) # exibir arquivo
