"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

# função zip() é uma função integrada que permite combinar duas ou iteráveis (lista, tupla, etc)
zipper = zip(lista_a, lista_b)

for item in zipper:
    #print(item)
    lista_soma.append(sum(item))

print(lista_soma)


'''
    # Solução do professor:
    lista_a = [10, 2, 3, 40, 5, 6, 7]
    lista_b = [1, 2, 3, 4]
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)
'''