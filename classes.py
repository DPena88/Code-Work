# # CLASSES
# #Class and object creation

# class pina():
#     color = "amarillo"
#     sabor = "dulce"
#     forma = "puntiaguda"

# pinia = pina()

# print(pina.color)
# print(pina.sabor)
# print(pina.forma)


class Vehiculo():

    def __init__(self, ruedas, motores, pasajeros, marca, color):
        self.ruedas = ruedas
        self.pasajeros = pasajeros
        self.motores = motores
        self.marca = marca
        self.color = color
    
    def move(self):
        print("me movi bro")

print("A Pokemon has been created")

class Pokemon():
    def __init__(self, tipo, weight, level, name):
        self.tipo = tipo
        self.weight = weight
        self.level = level
        self.name = name

    def attack(self):
        print("I have attacked")

    def flee(self):
        print("I fled")
    
    def __del__(self):
        print("I have been deleted")

    
charmander = Pokemon("Fire", 16, 12, "Charmander")

charmander.attack()

charmander.flee()

del charmander



        
# carro1 = Vehiculo (4,1,5, "Mercedes", "Blanco")

# print(carro1.marca)
# print(carro1.color)
# carro1.move()

# carro2 = Vehiculo(4, 5, 2, "Koi", "Negro")

# print(carro2.color)
# print(carro2.marca)

# carro2.move()




    # ruedas = 0
    # motores = 0
    # pasajeros = 0
    # marca = "No tiene marca definida"
    # color = "No tiene color definido"

# carro = vehiculo()
# barco = vehiculo()


# print(carro.ruedas)
# carro.ruedas = 4
# print(carro.ruedas)
# print(barco.ruedas)

# pasola = vehiculo()
# pasola.ruedas = 2






