"""
    Exercício
    Crie uma função que encontre duplicata e as separe em uma nova lista.
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> [1, 2, 3] são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> []
        [1, 2, 4, 9, 8, 9, 4, 8] -> [4, 9, 8]
"""

# identificar itens duplicados na lista 
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# filtro para itens duplicado na lista
def encontra_numeros_duplicado(lista_de_inteiros):
    numeros_checados = set() # uso de set para não haver valor repetido na "nova lista"
    contador = 0

    # percorre a lista e compara números
    for numero1 in lista_de_inteiros: 
        for numero2 in lista_de_inteiros:
            if numero1 == numero2:
                contador += 1 

            if contador == 2:  # contador = 0 (número apareceu 2 vezes na lista)
                numeros_checados.add(numero1) # armazene o número
                contador = 0 # zerar contador
        contador = 0 # zerar contador apos o "for" (numero2)
        
    return list(numeros_checados) # "nova lista"

# desempacota "lista_de_listas_de_inteiros" e envia lista individual a função "encontra_numeros_duplicado"
for lista in lista_de_listas_de_inteiros:
    print(
        f"{lista=}\t", # exibi a lista
        f"Números que se repetiram {encontra_numeros_duplicado(lista)}"  # resposta função "encontra_numeros_duplicado"
    )