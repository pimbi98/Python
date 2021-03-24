def suma(num1, num2):
    return num1 + num2

print(suma(10,21))

def resta(num1 = None, num2 = None):
    if num1 == None:
        print("falta n1.")
        return
    if num2 == None:
        print("falta n2.")
        return 
    
    return num1 - num2


print(resta(21))