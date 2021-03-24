
#Excepcion Simple:
while True:
    try:
        Edad = int(input("Ingrese edad: "))
        print("Tu edad es: ",Edad)
        break
    except:
        print("debe ingresar un valor numérico.")
    finally:
        print("Cierra Programa.")

while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        r = 100 / num1
        print(r)
        break
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("Haz colocado un valor erroneo.")
        break
    except KeyboardInterrupt:
        print("Haz cancelado tu operación.")
        break
    finally:
        print("Cierra Programa.")
