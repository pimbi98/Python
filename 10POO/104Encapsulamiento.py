class A():
    contador = 0
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

    #def restar(self):                      #Diseñar un futuro restador.
    #    self.contador = self.contador - 1

a = A()
a.incrementar()
a.incrementar()

print(a.cuenta())
print(a.contador)
#Clase B. Encapsulada.
class B():
    __contador = 0
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

    #def restar(self):                      #Diseñar un futuro restador.
    #    self.contador = self.contador - 1

b = B()
b.incrementar()
b.incrementar()

print(b.cuenta())
#print(b.__contador) #Al tener "__" no puede trabajarse fuera de la clase o objeto.
print(b._B__contador)#Esta sería la forma correcta de llamarlo.