import turtle
s = turtle.Screen()
t = turtle.Turtle()

def DibujarCirculo(Diametro):
    t.circle(Diametro)


def DibujarCuadrado(Largo):
    for i in range(4):
        t.fd(Largo)
        t.rt(90)

DibujarCuadrado(100)


Diametro = int(input("Ingrese diametro: "))
while Diametro >= 0:
    DibujarCirculo(Diametro)
    Diametro = Diametro - 10



turtle.done()
