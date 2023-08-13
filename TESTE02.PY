# ALTERAR "valor" e "chave" de dicionario
print()
dicionario = {"Nome": "Décio", "Sobre_Nome": "Aguiar"}
print(dicionario)
dicionario["Sobre_Nome"] = "Santana" # alterar valor
print(dicionario)
dicionario["Primeiro_Nome"] = dicionario.pop("Nome") # alterar chave
print(dicionario)
dicionario.update({
    "Sobre_Nome": "Santana de Aguiar",
    "Sexo": "Masculino"
})
print(dicionario)
dicionario.update(idade=41)
print(dicionario)
