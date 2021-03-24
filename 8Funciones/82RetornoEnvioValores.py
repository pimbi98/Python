def entero():
    return 12345

print (entero())


def valores():
    return 1,2,3,4,5 #Retorna una lista de valores.


a, b, c, d, e = valores()
print(a)
print(b)  
print(c) 
print(d) 
print(e) 


#Ejercicio 1
#Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar 
# el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

def Comparador(n1,n2):
    if n1 == n2:
        r = 0
    elif n1 < n2:
        r = -1
    elif n1 > n2:
        r = 1
    return r

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

print(Comparador(a,b))

#Ejercicio 2
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
# devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

def AplicaIVA(Importe, IVA=0.21): 
    ImporteFactura = Importe * (1 + IVA)
    return ImporteFactura


Importe = int(input("ingrese importe a abonar SIN IVA: "))
IVA     = float(input("ingrese % de recargo IVA: "))

if IVA < 0:
    print(AplicaIVA(Importe, IVA))
else:
    print("IVA DEFAULT: " , AplicaIVA(Importe))




