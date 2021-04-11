import turtle
import random

def DibujarCirculo(t, Diametro):
    t.circle(Diametro)


def DibujarCuadrado(t, Largo):
    for i in range(4):
        t.fd(Largo)
        t.rt(90)

def Marcan():
    J1.pendown()
    J2.pendown()    

def Desmarcan():
    J1.penup()
    J2.penup()

def Avanza(t, n):
    print(" Tu numero es: ", n, " . Avanzas: ", n * 20)
    t.fd(n * 20)

s = turtle.Screen()
s.bgcolor("black")

s.title("Carrera de tortugas con Random automático")

J1 = turtle.Turtle()
J2 = turtle.Turtle()

J1.hideturtle()
J1.shape("turtle")
J1.color("blue", "blue")
J1.shapesize(2,2,2)
J1.pensize(2)

J2.hideturtle()
J2.shape("turtle")
J2.color("yellow", "yellow")
J2.shapesize(2,2,2)
J2.pensize(2)
#Armamos primero las Metas.

Desmarcan()

J1.goto(200, 200)
J2.goto(200, 0)

Marcan()

DibujarCirculo(J1, 40)
DibujarCirculo(J2, 40)

Desmarcan()
#Fin armado Metas. Muestro tortugas en punto de partida. (-200, ... ) y Ahora van a marcar su recorrido. 
J1.goto(-200, 240)
J2.goto(-200, 40)

J1.showturtle()
J2.showturtle()

Marcan()
#Listo para iniciar Juego.

Dado = [1,2,3,4,5,6]

for i in range(40):
    if J1.pos() >= (200, 200) and  J2.pos() >= (200, 0):
        print("¡Empate!")
        break
    elif J1.pos() >= (200, 200): #Condicion para finalizar.
        print("Tortuga Azul ha ganado.")
        break
    elif J2.pos() >= (200, 0): #Condicion para finalizar.
        print("Tortuga Amarilla ha ganado.")
        break
    else:
        Marcan()
        Turno1 = input("Presiona tecla enter para avanzar la tortuga Azul: ")
        Turno1 = random.choice(Dado)
        Avanza(J1, Turno1)

        Turno2 = input("Presiona tecla enter para avanzar la tortuga Amarilla: ")
        Turno2 = random.choice(Dado)
        Avanza(J2, Turno2)

turtle.done()