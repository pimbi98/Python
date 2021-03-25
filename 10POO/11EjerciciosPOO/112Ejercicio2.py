#Ejercicio 1. 
# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
#  Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e 
# imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    n1:int = 0
    n2:int = 0
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def suma(self):
        print(self.n1 + self.n2)

    def resta(self):
        print(self.n1 - self.n2)

    def multiplicación(self):
        print(self.n1 * self.n2)

    def division(self):
        print(self.n1 / self.n2)

a = Calculadora(60,20)

a.suma()
a.resta()
a.multiplicación()
a.division()

#Ejercicio2. 
# #Escribir una clase que se llame Areas(). 
# A partir de un constructor se deben pasar los valores de Base y Altura. 
# Luego, se debe calcular area de un cuadrado, triangulo y pentagono

class FormulaArea():
    B = 0.00
    H = 0.00
    Cuadrado    = 0.00
    Triangulo   = 0.00
    Pentagono   = 0.00 #Buscar formula Pentagono.
    def __init__(self, B, H):
        self.B = B
        self.H = H

    def FCuadrado(self):
        self.Cuadrado = pow(self.B, 2)
        return self.Cuadrado

    def FTriangulo(self):
        self.Triangulo = (self.B * self.H) /2
        return  self.Triangulo

    #def FPentagono(self):

b = FormulaArea(12,4)

print(b.FCuadrado())
print(b.FTriangulo())










