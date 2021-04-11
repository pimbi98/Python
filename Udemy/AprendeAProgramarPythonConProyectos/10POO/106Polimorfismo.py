class Animales():
    def __init__(self, Nombre, Mensaje):
        self.Nombre     = Nombre
        self.Mensaje    = Mensaje

    def Hablar(self):
        print(self.Mensaje)

class Perro(Animales):
    def Hablar(self): #Objeto Perro puede modificar la funcion Hablar y para los perros toma este Hablar y no el superior.
        print("Los perros hacen: ",self.Mensaje)

class Pez(Animales):
    def Hablar(self):
     print("Yo no hablo")

#perro = Perro("Wilson", "Guau!")
#perro.Hablar()

animales = [Perro("Wilson", "Guau!"),Pez("Nemo", "Blob")]

for i in animales:
    print(i.Hablar())