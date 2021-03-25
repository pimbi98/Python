class A():
    def mensaje(self):
        print("Esto es clase A")
    def primera(self):
        print("ESTAS DENTRO DE CLASE A")

class B():
    def mensaje(self):
        print("Esto es clase B")
    def segunda(self):
        print("ESTAS DENTRO DE CLASE B")

class C(A,B):
    pass

c = C()
c.mensaje() #Toma la primer clase declarada. En este caso sería A.
c.primera() #Me situo en clase A.
c.segunda() #Paso a tomar la herencia segunda de la clase B.