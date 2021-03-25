class Persona():
    Nombre          = "Nombre"
    Apellido        = "Apellido"
    Edad            = 99
    Sexo            = "M"
    NombreCompleto  = "Nombre Apellido"
    def __init__(self, Nombre, Apellido, Edad, Sexo):
        self.Nombre     = Nombre
        self.Apellido   = Apellido
        self.Edad       = Edad
        self.Sexo       = Sexo
        self.NombreCompleto  = self.Nombre + " " + self.Apellido
        print("Nueva persona creada. Su nombre es: ",  self.Nombre," ",self.Apellido)

    def GetNombreCompleto(self):
        return self.Nombre + " " + self.Apellido

    def __del__(self):
        print("Persona eliminada.")

    def __str__(self):
        return self.Nombre,"\n",self.Apellido,"\n",self.Edad,"\n", str(self.Sexo)

Yo = Persona("Sebastian", "Scozzatti", 23, "M")


print(str(Yo))
