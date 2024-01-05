# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

'''
    OBS: Caso o modulo aula16b.py for executado tudo que estiver envolvido dentro de uma 
    função ou condição será executado.
'''

import json

arquivo_json = "p:\\REPOSITORIO\\PUBLICO\\PYTHON_UDEMY\\aula_016\\aula_16a.json"


# (inicio) execução no modulo aula16b.py
class Pessoa:
    ano_atual = 2023 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # uso do atributo da classe


p1 = Pessoa('Décio', 42)
p2 = Pessoa('Luana', 39)
p3 = Pessoa('Ana', 5)

p = [vars(p1),vars(p1),vars(p3)]

with open(arquivo_json, "w", encoding='utf8') as criar_arquivo_json:
    json.dump(p, criar_arquivo_json) # criar arquivo json 
# (fim) execução no modulo aula16b.py

''' bloco envolvido em uma função para não ser ativado na importação do modulo aula16b.py '''
def ver_arquivo_json(): 
    with open(arquivo_json, "r") as texto:
        ver_arquivo_json = json.load(texto)

    print()
    print('DICIONARIO:')
    print(*ver_arquivo_json, sep='\n')
    print('-' * 30)
    print()

'''
A variável especial __name__ em Python é usada para determinar se o módulo atual está sendo 
executado como um programa principal ou sendo importado por outro módulo.

    # Quando o módulo atual está sendo executado como um programa principal, 
    o valor de __name__ é __main__.
    # Quando o módulo atual está sendo importado por outro módulo, o valor de 
    __name__ é o nome do módulo.

    exemplo:

def main():
    print('Este módulo está sendo executado como um programa principal.')

if __name__ == '__main__':
    main()

'''
if __name__ == '__main__': # só é ativado executando diretamente este arquivo Python
    print()
    print('Realizado com sucesso!')
    print()

