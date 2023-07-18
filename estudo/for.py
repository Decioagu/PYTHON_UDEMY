print()
texto = 'Décio Santana de Aguiar'
for t in texto:
    print(t, end='-')
print('\n')
# posição , letra do texto
for e, t in enumerate(texto):
    print(f'{e}={t}', end='  ')
print('\n')
# range(inicio, parada, etapa)
for r in range(0, 10, 2):
    print(r, end='-')
print('\n')