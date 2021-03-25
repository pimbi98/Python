#Trasmitir ciertos parametros, atributos y metodos.


class Animales():
    def __init__(self, Descripcion, Especie, Sonido):
        self.Descripcion    = Descripcion
        self.Especie        = Especie
        self.Sonido         = Sonido

    def Hablar(self):
        print("Yo hago: ", self.Sonido)
    
    def Describir(self):
        print("Soy de la especie: ", self.Especie)


class Perro(Animales):
    pass

class Abeja(Animales):
    def sonido(self, Ruido):
        self.Ruido = Ruido
        print(self.Ruido)

perro = Perro("Perro", "Mamífero", "Guau")
perro.Hablar()
perro.Describir()


abeja = Abeja("Abeja Africana", "Insectos", "Bzz Bzzz")

abeja.sonido("Bzz BzzZzZzZ")

