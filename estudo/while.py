'''
Com o loop while, podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.
'''

linha = 0
coluna = 0

# controla quantidade de coluna
while coluna < 3:
    coluna += 1
    # controla quantidade de linha
    while linha < 6:
        print(linha, end='')
        linha += 1
    linha = 0
    print()