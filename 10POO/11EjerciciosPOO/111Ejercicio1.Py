#Ejercicio 1
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre 
# y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, 
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    Nombre  = "Nombre de Alumno"
    Nota    = 0
    def __init__(self, Nombre, Nota):
        self.Nombre = Nombre
        self.Nota   = Nota
    
    def Informe(self):
        print("Alumno: ", self.Nombre, "Obtuvo un: ", self.Nota)
        if (self.Nota >= 6):
            print("Aprobado")
        else:
            print("Reprobado.")


Pepito          = Alumno("Pepito", 7)
#Pepito.Nombre   = 
#Pepito.Nota     = 7
Pepito.Informe()

Mariel          = Alumno("Mariela", 5)
#Mariel.Nombre   = 
#Mariel.Nota     = 5
Mariel.Informe()


#Ejercicio 2
#Escribir una clase en python que calcule pow(x, n)


class Potencia():
    x = 0
    n = 0
    def __init__(self, x, n):
        self.x = x
        self.n = n
        print(pow(x, n))


a = int(input(" Ingrese Valor A: "))
b = int(input(" Ingrese Valor B: "))

Potencia(a,b)