# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~') # resposta => C:\Users\decio
TESTE_PY = os.path.join(HOME, 'TESTE_PY') # unir "C:\Users\decio" com "\TESTE_PY" 
# OBS: (pasta deve esta previamente criada)
NOVA_PASTA_1 = os.path.join(TESTE_PY, 'NOVA_PASTA_1') # já existe
NOVA_PASTA_2 = os.path.join(TESTE_PY, 'NOVA_PASTA_2') # já existe
NOVA_PASTA = os.path.join(TESTE_PY, 'NOVA_PASTA_3') # caminho (novo)

print(HOME)
# caso as pastas não exista não haverá erro
print(TESTE_PY)
print(NOVA_PASTA_1)
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True) # cria nova pasta (ver linha 11)


for rota, pastas, arquivos in os.walk(NOVA_PASTA_2):
    #the_counter = next(HOME)
    for arq in arquivos:
        print(arq)
    #print(the_counter, 'Rota:', rota)



# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminnho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminnho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminnho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminnho_novo_arquivo)