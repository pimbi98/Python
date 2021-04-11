print((12+3)*10)
#150 porque 12 + 3 = 15*10 = 150-
print(12+3*10)
#42 porque 3*10 = 30 + 12 = 42


print("Ejercicio 1")
#Ejercicio 1.
#Escribir un programa que realice la siguiente operacion ariitmetica.
#(3+2)**2
#------
#2.5


resultado = pow((3+2)/(2*5),2)
resultado = ((3+2)/(2*5))**2
#Tambien para potencia se puede usar pow(x,y)
print("El resultado es: " + str(resultado))

print("Ejercicio 2")
#Ejercicio 2.
#Una Jugueteria tiene exito en dos de sus productos. Payasos y muñecas. Suele enviar por correo y la logistica les cobra por el peso
#del paquete a demanda.
#Payaso pesa 112 gramos
#Muñeca pesa 75 gramos
#1 cliente pide frecuentemente 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de la venta.


PesoPayaso = 112
PesoMuñeca = 75
PedidoPayaso = 23
PedidoMuñeca = 54

PesoVenta = PesoPayaso * PedidoPayaso + PesoMuñeca * PedidoMuñeca
print("El peso total de la venta es " + str(PesoVenta) + " gramos.")

