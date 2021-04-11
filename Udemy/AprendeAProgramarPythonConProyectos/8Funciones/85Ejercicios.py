#Ejercicio 1
# Crear un programa que tenga dos funciones, una que contenga el area de 
# un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

def AreaCuadrado(b, h):
    AreaCuad = b * h
    return AreaCuad


def AreaCirculo(r):
    AreaCirc:int = 3.1415 * pow(r, 2)
    return AreaCirc

Base = int(input("ingrese base: "))
Altura = int(input("ingrese altura: "))

print(AreaCuadrado(Base, Altura))
RadioCirculo = int(input("ingrese radio de circulo: "))
print(AreaCirculo(RadioCirculo))
#Ejercicio 2
# Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def LargoLista(lista):
    return len(lista)

a = int(input("ingrese a: "))
b = int(input("ingrese b: "))
c = int(input("ingrese c: "))

MiLista = []
MiLista.append(a)
MiLista.append(b)
MiLista.append(c)

print(LargoLista(MiLista))
