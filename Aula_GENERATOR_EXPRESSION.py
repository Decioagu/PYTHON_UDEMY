import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(100)] # lista
generator = (n for n in range(100)) # compacta range em um local na memória (economiza memória)

# getsizeof() é uma função em Python retorna o tamanho de um objeto em bytes
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator) # não é possível acesso direto dos itens
print(next(generator))
print(next(generator))
print(next(generator))

# OU 

# for n in generator:
#     print(n)

# --------------------------------------------------------------
'''
    A yield palavra-chave em Python é usada para criar geradores. Geradores são iteradores 
    que podem ser usado para produzir uma sequência de valores, um de cada vez.
'''
def gerador():
  yield 1
  yield 2
  yield 3

gerador = gerador()

print(next(gerador))
print(next(gerador))
print(next(gerador))

# --------------------------------------------------------------
# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)
# --------------------------------------------------------------