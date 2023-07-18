texto = 'Decio Santana de Aguiar'
letra_que_mais_aparece = 0
letra = ''


# loop para percorrer todo o texto
for loop in texto:

    # contagem da palavra pesquisada
    contador_de_letra = texto.count(loop)

    # pula espaço no texto
    if loop == ' ':
        continue

    # armazena e atualiza letra que aparce com mair quantidade
    if letra_que_mais_aparece < contador_de_letra:
        letra_que_mais_aparece = contador_de_letra
        letra = loop    

# resposta armazenada
print(f'\n{letra=} => {letra_que_mais_aparece}x\n')