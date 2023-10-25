# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor

class Carro:
    def __init__(self, nome_carro):
        self.nome_carro = nome_carro
        self.lista_de_motores = []
    
    def motor_carro(self, nome_motor):
        self.lista_de_motores.append(nome_motor)

    def ver_lista_carro_motores(self):
        for motor in self.lista_de_motores:
            # print(motor.nome_motor)
            print('Carro:', self.nome_carro, motor.nome_motor)

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante
        self.lista_de_carros = []

    def modelo_carro(self, nome_carro, lista_de_motor):
        temporario = [ nome_carro, lista_de_motor]
        self.lista_de_carros.append(temporario)
    
    def ver_lista_fabricante(self):
        for carro in self.lista_de_carros:
            print('Fabricante:', self.nome_fabricante, ', Carro:',*carro)
        
        



m1 = Motor('Motor 1.0')
m2 = Motor('Motor 1.4')
m3 = Motor('Motor 1.6')
m4 = Motor('Motor 2.0')
m5 = Motor('Motor V8')
m6 = Motor('Motor W')
m7 = Motor('Motor refrigeração a ar')

carro1 = Carro('Gol')
carro1.motor_carro(m1)
carro1.motor_carro(m2)

carro2 = Carro('Fusca')
carro2.motor_carro(m7)

carro3 = Carro('Ferrari')
carro3.motor_carro(m5)

carro1.ver_lista_carro_motores()
carro2.ver_lista_carro_motores()
carro3.ver_lista_carro_motores()

print('-' * 30)
fabricante1 = Fabricante("VW")
fabricante1.modelo_carro(carro1.nome_carro, [motor.nome_motor for motor in carro1.lista_de_motores])
fabricante1.ver_lista_fabricante()


