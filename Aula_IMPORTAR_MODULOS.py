import pprint
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 50, },
    {'nome': 'p5', 'preco': 5, },
]

print(*produtos, sep='\n') # desempacotar lista
print()
print(produtos, sep='\n') # desempacotar lista
print()
pprint.pprint(produtos) # desempacotar lista

# -------------------------------------------------------------------------