num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))

if num1 < num2:
    print(str(num2) + " mayor a :" + str(num1))
else:
    print(str(num1) + " mayor a : " + str(num2))
#Ejercicio 1
Letra = input("Ingrese una letra: ")
if Letra in "aeiou":
    print("es una Vocal.")
else:
    print("es una Letra.")


#Ejercicio2
#Programa que pida dos palabras y diga si riman o no.
#Si las dos palabras son mas largas de 3 char, tiene que coincidir ultimas 3 letras.
#Si alguna es menor a 3 chaar o igual, solo debe coincidir 2.


pal1 = input("Ingrese primera palabra: ")
pal2 = input("Ingrese segunda palabra: ")

if len(pal1) < 3 or len(pal2) < 3:
    if (pal1[-2:] == pal2[-2:]):
        print("riman!")
    else:
        print("NO riman")
else:
    if (pal1[-3:] == pal2[-3:]):
        print("riman!")
    else:
        print("NO riman")  


