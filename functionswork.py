# #Diego Peña

# # Instructions
# # Make an example script  or program that applies the concepts seen on today's class:

## Functions with and without return values.

def yesreturn(a, b):
    return (a + b)

num1 = 8

num2 = 9

print(yesreturn(num1, num2))


def noreturn():
    print("Hello. This function has no return values.")

noreturn()



### Functions with and without parameters.

def noparam():
    print("Hello, this is a function without parameters")

def yesparam(param1, param2):
    print(f"este es {param1} y este es {param2}")

eluno = "el parametro 1 de la funcion"

eldos = "el parametro 2 de la funcion"

yesparam(eluno, eldos)



# Functions with positional arguments.

def positional_argument(*args):
    for i in args:
        print(i,)
positional_argument(1,2,3,4,"HOLA",True,[2,4,6],(1,2,3,), "Diego")



# Functions with keyword arguments.

def kwfunction(**kwargs):
    print(f"Hola {kwargs["tunombre"]}, soy {kwargs["minombre"]}")
kwfunction(tunombre = "Fulano", minombre = "Diego")



# Functions with default values.

def letsplay(game = "Mario Kart", where = "after school"):
    print(f"Let's play {game} {where}!")
letsplay(game = "Zelda", where = "at my house")
letsplay()
letsplay("basketball", "during recess")

