#Bucle while. Mientras se cumple condicion.
Cuenta = 5

while Cuenta > 0:
    print(Cuenta)       #Iteración.
    Cuenta = Cuenta - 1 

print("Despegue!!")     #Fin.


#Bucle while. Mientras se cumple condicion. Pero aplicamos un break.
Cuenta = 5

while Cuenta > 0:
    print(Cuenta)       #Iteración.
    if Cuenta == 3:
        print("Houston, tenemos un problema.") #Corta en 3.
        break

    if Cuenta == 0:             #Nunca se daria este if == true porque se corta en 3.
        print("Despegue!!")     #Fin. #Corta en 0.
    Cuenta = Cuenta - 1 
#Ejercicio 1.
# Escribir un programa que pida un numero al usuario y
#  muestre las tablas de multiplicar de ese numero


Numero = int(input("Ingrese Numero: "))

NumeroMultiplicador = 0
while NumeroMultiplicador <= 10:
    Producto = Numero * NumeroMultiplicador
    print(NumeroMultiplicador, " x ", Numero, " = ", Producto)
    NumeroMultiplicador = NumeroMultiplicador + 1


#Ejercicio 2. 
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido.
# (desde 1 hasta su edad).

Edad = int(input("Ingrese su Edad: "))
Años = 1
while Años <= Edad:
    print(Años)
    Años = Años + 1