"""
Exercício:
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
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

# filtro para item duplicado na lista
def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = []
    primeiro_duplicado = -1

    for numero in lista_de_inteiros: # ler itens da lista
        
        # item da (lista = "lista_de_inteiros") consta na (lista = "numeros_checados")
        if numero in numeros_checados: # se sim
            primeiro_duplicado = numero # armazene este numero número
            break # interrompe "for"

        numeros_checados.append(numero) # adiciona todos os novos elementos na lista "numeros_checados"

    return primeiro_duplicado # resposta

# desempacota "lista_de_listas_de_inteiros" e envia cada lista individual a função "encontra_primeiro_duplicado"
for lista in lista_de_listas_de_inteiros:
    print(
        f"{lista=}\t", # exibi cada lista individualmente
        f"Primeira repetição {encontra_primeiro_duplicado(lista)}"  # resposta função "encontra_primeiro_duplicado"
    )