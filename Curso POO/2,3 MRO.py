class A:
    
    def hablar(self):
        print('hola desde A')

class B(A):
    
    def hablar(self):
        print('hola desde B')

class F:
    
    def hablar(self):
        print('hola desde F')

class C(F):
    
    def hablar(self):
        print('hola desde C')

class D(B, C):
    
    def hablar(self):
        print('hola desde D')

d= D()

D.hablar(d)