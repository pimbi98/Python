import turtle
import time
import random
def finalizaJuego():
    for i in Cuerpo:
        i.clear()
        i.hideturtle()
    Serpiente.home()
    Serpiente.direction = 'stop'
    Cuerpo.clear()
    marcador = 0
    string = "Marcador: " + str(marcador) + " \tMarcador más alto: " + str(marcador_Alto)
    texto.clear()
    texto._write(string, align="center", font=("comic sans", 24, "normal"))

def movimiento():
    if Serpiente.direction == "up":     #Suma en eje  Y.
        y = Serpiente.ycor()
        Serpiente.sety(y + 20)
    if Serpiente.direction == "down":   #Resta en eje  Y.
        y = Serpiente.ycor()
        Serpiente.sety(y - 20)
    if Serpiente.direction == "right":  #Suma en eje  X.
        x = Serpiente.xcor()
        Serpiente.setx(x + 20)
    if Serpiente.direction == "left":   #Resta en eje  X.
        x = Serpiente.xcor()
        Serpiente.setx(x - 20)
       
def arriba():
    Serpiente.direction = 'up'

def abajo():
    Serpiente.direction = 'down'

def derecha():
    Serpiente.direction = 'right'

def izquierda():
    Serpiente.direction = 'left'

s = turtle.Screen()
s.setup(650, 650)
s.bgcolor("black")
s.title("Serpiente loca.")

Serpiente = turtle.Turtle()
Serpiente.speed(1)
Serpiente.shape("square")
Serpiente.penup()
Serpiente.goto(0,0)
Serpiente.direction = "up" #Si programa termina, va al 0,0 y para.
Serpiente.color('green')


comida = turtle.Turtle()
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,100)
comida.speed(0)

s.listen() #Pantalla escucha entrada de teclado.
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

s.onkeypress(arriba, "w")
s.onkeypress(abajo, "s")
s.onkeypress(izquierda, "a")
s.onkeypress(derecha, "d")

retraso = 0.1
marcador = 0
marcador_Alto = 0
Cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("grey")
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto._write("Marcador: 0\tMarcador más alto: 0", align="center", font=("comic sans", 24, "normal"))
while True: #Siempre se cumple (Los videojuegos siempre tienen loops "infinitos hasta que pasa algo y se corta con break.")
    s.update()
    if Serpiente.xcor() > 300 or Serpiente.xcor() < -300 or Serpiente.ycor() > 300 or Serpiente.ycor() < -300:
        time.sleep(3)
        finalizaJuego()
        

    if Serpiente.distance(comida) <= 20: #Come.
        marcador += 1 
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)
        #Si come, cuerpo se agranda.
        CuerpoNuevo = turtle.Turtle()
        CuerpoNuevo.shape('square')
        CuerpoNuevo.color('green')
        CuerpoNuevo.penup()
        CuerpoNuevo.goto(0,0)
        CuerpoNuevo.speed(0)
        Cuerpo.append(CuerpoNuevo)
        
        if marcador > marcador_Alto:
            marcador_Alto = marcador
            texto.clear()
            string = "Marcador: " + str(marcador) + " \tMarcador más alto: " + str(marcador_Alto)
            texto._write(string, align="center", font=("comic sans", 24, "normal"))

    total = len(Cuerpo)
    for i in range(total -1,0,-1):
        x = Cuerpo[i-1].xcor()
        y = Cuerpo[i-1].ycor()
        Cuerpo[i].goto(x,y)

    if total > 0: #Mas de un elemento.
        x = Serpiente.xcor()
        y = Serpiente.ycor()
        Cuerpo[0].goto(x,y)

    movimiento()

    for i in Cuerpo: #Serpiente choca con Serpiente.
        if i.distance(Serpiente) < 20:
            finalizaJuego()
    time.sleep(retraso)

turtle.done()