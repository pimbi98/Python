Diccionario = {1:"Pipo",2:"Nwn",3:"Tanque"}

print(Diccionario[1])


#Ejercicio Pais que no esta en Diccionario. 
#En el siguiente diccionario se encuentran capitales de los paises en el mundo, #
# debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
# en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no
#  se encuentra.

Paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}


Pais = input("Ingrese País para ver la capital: ")




HayPais = Pais.capitalize() in Paises
if (HayPais == True):
    print("La capital de ", Pais, " es ", Paises[Pais.capitalize()])
else:
    print("No se encuentra el pais: " + Pais.capitalize())



#Ejercicio 2. Con el siguiente diccionario, 
# debes crear un programa que pregunte al usuario por un número;
#  el programa debe imprimir el jugador al que hace referencia ese número

Jugadores = {1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

NumeroJugador = int(input("Ingrese numero de jugador deseado: "))

ExisteJugador = NumeroJugador in Jugadores

if ExisteJugador == True:
    print("El jugador con la remera ", NumeroJugador, " es ", Jugadores[NumeroJugador])
else:
    print(NumeroJugador, " no pertenece a ningun jugador de la lista.")


