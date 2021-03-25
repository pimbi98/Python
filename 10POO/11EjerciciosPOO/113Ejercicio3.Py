class Fabrica():
    Ruedas  = 4
    Color   = "Rojo"   
    Precio  = 150000
    def InformaRuedas(self):
        print("Tiene: ", self.Ruedas)
    def InformaColor(self):
        print("Color: ", self.Color)
    def InformaPrecio(self):
        print("Cuesta: ", self.Precio)

class Moto(Fabrica):
    Ruedas = 2
    Color = "Negro"
    Precio = 67500


class Auto(Fabrica):
    Ruedas = 4
    Color = "Gris"
    Precio = 240000

F = Fabrica()
F.InformaRuedas()
F.InformaColor()
F.InformaPrecio()

M = Moto()
M.InformaRuedas()
M.InformaColor()
M.InformaPrecio()

A = Auto()
A.InformaRuedas()
A.InformaColor()
A.InformaPrecio()

