import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.begin_fill()

t.circle(100)
t.end_fill()
t.begin_fill()

t.color("white", "white")
t.circle(10)
t.end_fill()

t.color("blue", "yellow")
t.penup()
t.fd(100)
t.pendown()
t.rt(90)
t.fd(100)
t.stamp()

t.undo()
t.clear()
t.reset()



turtle.done()