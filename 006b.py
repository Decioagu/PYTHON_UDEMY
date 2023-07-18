texto = 'Decio Santana de Aguiar'
letra_que_mais_aparece = 0
letra = ''


# loop para percorrer todo o texto
for loop in texto:

    # conta a quantidade de letra na palavra sem os espaços
    contador_de_letra = texto.strip().count(loop)

    # armazena e atualiza letra que aparce com mair quantidade
    if letra_que_mais_aparece < contador_de_letra:
        letra_que_mais_aparece = contador_de_letra
        letra = loop    

# resposta armazenada
print(f'\n{letra=} => {letra_que_mais_aparece}x\n')