edad = int(input("Ingresa tu edad: "))
nombre = input("Ingresa nombre: ")
direccion = input("Ingresa direccion: ")


print("Tu nombre es: {}, , tu edad es: {} y vives en: {}".format(nombre, edad, direccion))


print("Ejercicio 1")
#Programa que solicite al usuario una vocal en minuscula y una letra en mayuscula. Programa debe convertir letra en minuscula y vocal en mayuscula. Al final
#concatenar ambas y print.

Vocal = input("ingrese una vocal en minuscula: ")
Letra = input("ingrese una letra en mayuscula: ")


Resultado = Vocal.upper() + Letra.lower()
print(Resultado)