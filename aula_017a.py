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
    
    # setter (motores)
    def motor_carro(self, nome_motor):
        self.lista_de_motores.append(nome_motor)

    # getter (motores)
    def ver_lista_carro_e_motores(self):
        for motor in self.lista_de_motores:
            print('Carro:', self.nome_carro, motor.nome_motor)

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_fabricante = nome_fabricante
        self.lista_carro_e_motores = []

    # setter (carros)
    def modelo_carro(self, nome_carro, lista_de_motor):
        lista_carro_e_motores_temporario = [ nome_carro, lista_de_motor]
        self.lista_carro_e_motores.append(lista_carro_e_motores_temporario)
    
    # getter (carros)
    def ver_lista_fabricante(self):
        for carro in self.lista_carro_e_motores:
            print('Fabricante:', self.nome_fabricante, ', Carro:',*carro) 


# tipos de motores
m1 = Motor('Motor: 1.0')
m2 = Motor('Motor: 1.4')
m3 = Motor('Motor: 1.6')
m4 = Motor('Motor: 2.0')
m5 = Motor('Motor: V8')
m6 = Motor('Motor: W')
m7 = Motor('Motor: Refrigeração a ar')

# tipos de carros
carro1 = Carro('Gol')
carro1.motor_carro(m1)
carro1.motor_carro(m2)
carro1.motor_carro(m3)
carro1.motor_carro(m4)

carro2 = Carro('Fusca')
carro2.motor_carro(m7)

carro3 = Carro('Ferrari SF90')
carro3.motor_carro(m5)

carro1.ver_lista_carro_e_motores()
carro2.ver_lista_carro_e_motores()
carro3.ver_lista_carro_e_motores()
print('-' * 95)

# tipos de fabricantes
fabricante1 = Fabricante("Volkswagen")
fabricante1.modelo_carro(carro1.nome_carro, [motor.nome_motor for motor in carro1.lista_de_motores])
fabricante1.modelo_carro(carro2.nome_carro, [motor.nome_motor for motor in carro2.lista_de_motores])
fabricante1.ver_lista_fabricante()

print('-' * 95)
fabricante2 = Fabricante("Ferrari")
fabricante2.modelo_carro(carro3.nome_carro, [motor.nome_motor for motor in carro3.lista_de_motores])
fabricante2.ver_lista_fabricante()
print()


