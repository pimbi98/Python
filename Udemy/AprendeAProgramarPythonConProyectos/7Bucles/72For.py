Nombres = ["Sebastian", "Juan", "José"]

for j in Nombres:
    print("Feliz navidad",j)

#Ejercicio 1. Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar 
# el rango de numeros entre ambas cifras
#aprovecho variable numeros.
Numeros = [1,2,3,4,5,6,7,8,9,10]

for i in Numeros: #Itera automaticamente sin incremento, pasa por cada index de la lista.
    print(i)

a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))

for i in Numeros:
    if ((a <= i) and (b >= i)) or ((a >= i) and (b <= i)):
        print(i)

#Ejercicio 2.
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


Palabra = input("ingrese algo que le gusta: ")

for i in Numeros:
    print(Palabra) #Aprovecho lista Numeros que ya tiene 10 posiciones. 