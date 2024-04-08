# Diego Peña

# Encapsulation

class carro():
    def __init__(self, marca, velocidad):
        self.__marca = marca
        self.__velocidad = velocidad
    
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

car1 = carro("audi", 300)
print(car1.get_marca())
car1.__marca = "toyota"

car1.set_marca("toyota")
print(car1.get_marca())

# Inheritance and Abstraction

class animales():
    def sonido():
        print("raaaaa soy un animal")
    def correr():
        ("Estoy corriendo")
    

        
class canidae(animales):
        def __init__(self):
            super().__init__()
    
class perro(canidae):
    def __init__(self):
        super().__init__()

class labrador(perro):
    def __init__(self):
        super().__init__()
    def sonido():
        print("guao soy un labrador")

class chihuahua(perro):
    def __init__(self):
        super().__init__()
    def sonido():
        print("wao wao wao soy un chihuahua")
    
    

labrador.sonido()
chihuahua.sonido()
    
# Polymorphism

class dog():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def run(self):
        print("Woof, i am running")


class cat():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def run(self):
        print("Meow, i am running")

dog1 = dog("max", "woof")
cat1 = cat("kit", "meow")

dog1.run()
cat1.run()


