#Diego Peña

# Make a script that does the following requirements:
# Create a class of something abstract of your election (say for example, vehicle, fruit, person etc.)
# The class must have at least 5 properties.

class perro ():
    def __init__(self, nombre, raza, color, patas, genero):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.patas = patas
        self.genero = genero

    # Each class must have at least 2 methods (functions) that resemble the classes in real file (for example, a car goes forward, backwards, parks, etc.).

    def ladrar(self):
        print("El perro ladró")
    
    def correr(self):
        print("El perro corrió")

# Create 2 objects of that class with their respective properties.

perro1 = perro("Max", "Labrador", "negro", 4, "masculino" )

perro2 = perro("Lili", "Chihuahua", "blanco", 4, "femenino")

print(perro1.nombre)
print(perro1.raza)
print(perro1.color)
print(perro1.patas)
print(perro1.genero)

print(perro2.nombre)
print(perro2.raza)
print(perro2.color)
print(perro2.patas)
print(perro2.genero)

perro1.ladrar()

perro2.correr()

# Change 2 properties of one of the objects created.

perro1.raza = "golden retriever"
perro1.color = "blanco"

print(perro1.nombre)
print(perro1.raza)
print(perro1.color)
print(perro1.patas)
print(perro1.genero)

# Delete the objects at the end.

del perro1
del perro2



# Execute all the methods you created for the class, with both objects.


