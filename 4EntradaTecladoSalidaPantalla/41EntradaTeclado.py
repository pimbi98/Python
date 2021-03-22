edad = int(input("Ingresa tu edad: "))
nombre = input("Ingresa nombre: ")


print(nombre)
print(edad)

#Ejercicio 1.
#Realizar un programa que haga el proceso de formula general para la reslucion de ecuaciones, sabiendo que la formula general 
#es la que esta en la imagen, el usuario debe ingresar valores a, b y c y el programa debe hacer el proceso para que al final
#muestre el mensaje " la solucion es: solucion"
from math import sqrt

a = int(input("ingrese A: "))
b = int(input("ingrese B: "))
c = int(input("ingrese C: "))

x1 = 0
x2 = 0


if ((b**2) - (4*a*c)) < 0:
    print("No se puede realizar")
else:
    x1 = (-b + sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2) - (4*a*c))) / (2*a)
    print("La solucion es: ", x1, " y tambien: ", x2)
