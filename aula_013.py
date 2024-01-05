'''Exercício - Adiando execução de funções'''
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def aguardar_funcao(funcao, x):
    def espera(y):
        return funcao(x,y)
    return espera # retorna função sem executar -> (aguarda segundo argumento (y) para executar)

soma_com_cinco = aguardar_funcao(soma, 5) # executa "aguardar_funcao" + valor de x
multiplica_por_dez = aguardar_funcao(multiplica, 10) # executa "aguardar_funcao" + valor de x

print(soma_com_cinco(10)) # executa "aguardar_funcao" + valor de y
print(multiplica_por_dez(10)) # executa "aguardar_funcao" + valor de y