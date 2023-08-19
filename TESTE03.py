"""
    Introdução à função lambda (função anônima de uma linha)
    A função lambda é uma função como qualquer
    outra em Python. Porém, são funções anônimas
    que contém apenas uma linha. Ou seja, tudo
    deve ser contido dentro de uma única
    expressão.
"""
def dobro(x):
    return x * 2
print(dobro(5))

dobro_com_lambda = lambda x: x * 2
print(dobro_com_lambda(5))
print()
# --------------------------------------------------------------------------------
'''
    A função map() em Python usa uma função e um iterável como seus argumentos 
    e retorna um iterador que aplica a função a cada elemento do iterável.

    Exemplo: nome = list(map(função, lista))
'''

lista_num_int = [1, 2, 3, 4, 5]

def quadrado1(x):
  return x * x
num_ao_quadrado1 = list(map(quadrado1, lista_num_int))
print(num_ao_quadrado1)


num_ao_quadrado2 = list(map(lambda x: x * x, lista_num_int))
print(num_ao_quadrado2)
print()
# --------------------------------------------------------------------------------
'''
    A sorted()função em Python é uma função interna que classifica os elementos de um iterável 
    em uma ordem específica (crescente ou decrescente) e os retorna como uma lista.

    A sorted()função recebe três parâmetros:

    iterable: O iterável a ser classificado.
    key: Uma função opcional que recebe um elemento do iterável como entrada e retorna um valor 
         a ser usado para classificação. O valor padrão é Nenhum, o que significa que os elementos 
         são classificados por sua ordem natural.
    reverse: Um valor booleano que indica se os elementos devem ser classificados em ordem decrescente (True) 
             ou crescente (False). O valor padrão é falso.
             
            Exemplo: 
            list1 = [3, 4, 5, 1, 2]
            print(sorted(list1))
            print(sorted(list1, reverse=True))

'''
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) # ordenar por nome
l2 = sorted(lista, key=lambda item: item['sobrenome']) # ordenar por sobrenome

exibir(l1)
exibir(l2)
print()
# --------------------------------------------------------------------------------