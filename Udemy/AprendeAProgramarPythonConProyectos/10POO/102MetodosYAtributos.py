#Metodos son funciones, pero en poo se llaman metodos.
#Atributos son caracteristicas de los objetos.

class Persona():
    def __init__(Self):
        print("Haz creado un objeto Persona.")

    Nombre      = False
    Apellido    = "Robersino"
    Sexo        = "M"
    Edad        = 30
    def Presentarse(Self, Mensaje): #Self se refiere a la clase propio.
        return Mensaje
    def NombreCompleto(Self):
        return Self.Nombre + " " + Self.Apellido

Yo = Persona()

Yo.Nombre       = "Sebastian"
Yo.Apellido     = "Scozzatti"
Yo.Sexo         = "M"
Yo.Edad         = 23

MiNovia = Persona("Jazmín Belén", "Lopez", "F", 18)


print(Yo.Presentarse("Hola, soy "+ Yo.NombreCompleto()))
print(MiNovia.Presentarse("Hola, soy "+ MiNovia.NombreCompleto()))