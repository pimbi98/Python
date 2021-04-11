def EmitirMensaje(mensaje):
    print(mensaje)

EmitirMensaje("Hola")

EmitirMensaje("Esta es mi primer Función")



def suma(n1,n2): #Variables definidas dentro de la funcion, estan ENCAPSULADAS, A menos que se declare como global.
    global resultado
    resultado = n1 + n2
    print(resultado)

suma(3,4)


print("El resultado es ", resultado)
#Ejercicio 1 
# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al 
# usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los
#  numeros pares e impares dentro de dos listas nuevas
def Añadir(x, Alista):
    Alista.append(x)
    

def OrdenarParImpar(Olista):
    listaPar    = []
    listaImpar  = []
    for n in Olista:
        resto = n % 2
        if (resto == 0):
            listaPar.append(n)
        else:
            listaImpar.append(n)
    print("Par: ", listaPar)
    print("Impar: ", listaImpar)


lista = [1,2,3,4,5,6,7,8,9,10]

n1 = int(input("ingrese valor 1: "))
n2 = int(input("ingrese valor 2: "))
n3 = int(input("ingrese valor 3: "))

Añadir(n1,lista)
Añadir(n2,lista)
Añadir(n3,lista)


OrdenarParImpar(lista)

#Ejercicio 2 
# Escribir una función que reciba un número entero positivo y devuelva su factorial.
from math import factorial

def GetFactorial(n):
    global Factorial
    Factorial = factorial(n)
valor1 = int(input("Ingresa valor 1: "))

GetFactorial(valor1)

print(Factorial)



