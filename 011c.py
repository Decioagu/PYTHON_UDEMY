
# identificar itens NÃO duplicados na lista 
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

# filtro para itens NÃO duplicado na lista
def encontra_numeros_nao_duplicado(lista_de_inteiros):
    numeros_checados = []
    contador = 0

    # percorre a lista e compara
    for numero1 in lista_de_inteiros: 
        for numero2 in lista_de_inteiros:
            if numero1 == numero2:
                contador += 1

        if contador == 1: # contador = 1 (armazena)
            numeros_checados.append(numero1)
            contador = 0
        contador = 0

    return numeros_checados

# desempacota "lista_de_listas_de_inteiros" e envia lista individual a função "encontra_primeiro_duplicado"
for lista in lista_de_listas_de_inteiros:
    print(
        f"{lista=}\t", # exibi a lista
        f"Primeira repetição {encontra_numeros_nao_duplicado(lista)}"  # resposta função "encontra_primeiro_duplicado"
    )