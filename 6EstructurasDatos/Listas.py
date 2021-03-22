MiLista = ["Tomate", "Cebolla", "Huevos", "Arroz"]


MiLista2 = [1,2,3,4,5,6,7]
MiLista3 = [8,9,10]


print(MiLista)
print(MiLista[3])
print("Leche" in MiLista) #False.


print(MiLista2[2:4])
del MiLista[3]
print(MiLista2 + MiLista3) #Concatena listas.

MiLista.append("Atún")
print(MiLista)
MiLista2.extend(MiLista3)
print(MiLista2)

MiLista.remove("Tomate")
print(MiLista)

#Ejercicio 1 de la siguiente Lista. hacer un programa que muestre los valores al user.
#A su vez, pedir dos datos y esos, sustituirlos en el primer y seegundo lugar.

Ejercicio1 = [20,50,"Curso", "Python", 3.14]
print(Ejercicio1)

Valor1 = input("Ingrese valor 1.")
Valor2 = input("Ingrese valor 2.")

Ejercicio1[0] = Valor1
Ejercicio1[1] = Valor2
print(Ejercicio1)

#Ejercicio2 
#Lista que tenga numeros del 1 al 10. Luego a los datos de posicion 4, 7, 9 Multiplicar x 2. Mostrar nueva Lista.
Ejercicio2 = [1,2,3,4,5,6,7,8,9,10]
print(Ejercicio2)
Ejercicio2[4] = Ejercicio2[4] * 2
Ejercicio2[7] = Ejercicio2[7] * 2
Ejercicio2[9] = Ejercicio2[9] * 2
print(Ejercicio2)
