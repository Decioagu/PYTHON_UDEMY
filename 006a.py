texto = 'Decio Santana de Aguiar'
contador_do_loop = 0
letra_que_mais_aparece = 0
letra = ''


# loop para percorrer todo o texto
while contador_do_loop < len(texto):

    # pesquisa que percorre o texto[indece]
    pesquisa = texto[contador_do_loop]

    # contagem da palavra pesquisada
    contador_de_letra = texto.count(pesquisa)

    # pula espaço no texto
    if pesquisa == ' ':
        contador_do_loop +=1
        continue
    
    # armazena e atualiza letra que aparce com mair quantidade
    if letra_que_mais_aparece < contador_de_letra:
        letra_que_mais_aparece = contador_de_letra
        letra = pesquisa  

    # soma + 1 no final de cada loop  
    contador_do_loop +=1

# resposta armazenada
print(f'\n{letra=} => {letra_que_mais_aparece}x\n')