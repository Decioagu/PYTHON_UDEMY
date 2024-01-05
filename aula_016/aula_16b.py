# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
from pathlib import Path
from aula_16a import Pessoa, ver_arquivo_json

'''
    OBS: Tudo que não estiver envolvido dentro de uma função ou condição no modulo aula16a.py
    será executado o programa.
'''

# Caminhos para pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ARQUIVO = CAMINHO_RAIZ / 'aula_16a.json'
arquivo_json = CAMINHO_ARQUIVO # p:\REPOSITORIO\PUBLICO\PYTHON_UDEMY\aula_016\aula_16a.json
# print(arquivo_json)

ver_arquivo_json() # (importado "aula_16a")

# ler arquivo externo
with open(arquivo_json, "r") as texto:
    ver_arquivo_json = json.load(texto)
    p1 = ver_arquivo_json[0]
    p2 = ver_arquivo_json[1]
    p3 = ver_arquivo_json[2]

# simplificar valores do dicionario em listas
p1 = ([x for x in p1.values()])
p2 = ([x for x in p2.values()])
p3 = ([x for x in p3.values()])

# ver listas
print('LISTA:')
print(p1)
print(p2)
print(p3)
print()
print('-' * 30)
print()

# adicionar informações na class (importado "aula16a")
p1 = Pessoa(*p1)
p2 = Pessoa(*p2)
p3 = Pessoa(*p3)

# ver atributos das class p1, p2 e p3
print('CLASS:')
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)