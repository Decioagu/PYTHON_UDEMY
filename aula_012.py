'''
    # copy, sorted, produtos.sort

    # Exercícios:

    # Aumente os preços dos produtos a seguir em 10%
    # Gere novos_produtos por deep copy (cópia profunda)

    # Ordene os produtos por nome decrescente (do maior para menor)
    # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

    # Ordene os produtos por preco crescente (do menor para maior)
    # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''

from operator import itemgetter # biblioteca

# lista
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# regra de criação de nova lista
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)} # regra
    for produto in produtos # percorrer iterável criando nova lista conforme regra
]

produtos_ordenados_por_nome = sorted(novos_produtos, key=itemgetter('nome'), reverse=True) # ordenar nova lista por nome

produtos_ordenados_por_preco = sorted(novos_produtos, key=itemgetter('preco')) # ordenar nova lista por preco

# imprimir todas as listas
print('=' * 60)
print('Lista produtos')
print(*produtos, sep='\n')
print('_' * 60)
print('Lista novos produtos')
print(*novos_produtos, sep='\n')
print(produtos == novos_produtos) # testar se litas é igual ou é uma nova lista
print('_' * 60)
print('Lista novos produtos ordenados por nome "decrescente"')
print(*produtos_ordenados_por_nome, sep='\n')
print(produtos_ordenados_por_nome == novos_produtos) # testar se litas é igual ou é uma nova lista
print('_' * 60)
print('Lista novos produtos ordenados por preco "crescente"')
print(*produtos_ordenados_por_preco, sep='\n')
print(produtos_ordenados_por_preco == novos_produtos)
print('=' * 60)
print(produtos_ordenados_por_nome == produtos_ordenados_por_preco) # testar se litas é igual ou é uma nova lista


