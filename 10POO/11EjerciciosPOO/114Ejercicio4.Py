#Ejercicio 1
# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". 
# Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". 
# Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje 
# y que muestre ese mensaje como parametro.


class Marino():
    def Hablar(self):
        print("Hola...")


class Pulpo(Marino):
    def Hablar(self):
        print("Soy un pulpo...")

class Foca(Marino):
    def __init__(self, Mensaje):
        self.Mensaje = Mensaje
    def Hablar(self):
        print(self.Mensaje)

foca = Foca("hola")
foca.Hablar()

pulpo = Pulpo()
pulpo.Hablar()

marino = Marino()
marino.Hablar()
