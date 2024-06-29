class Persona:
    
    def __init__(self, nombre, edad, nacionalidad):
        
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
    
    def hablar(self):
        print('hola, estoy hablando un poco')

class Empleado(Persona):
    
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo= trabajo
        self.salario= salario

class Estudiante(Persona):
    
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        
        super().__init__(nombre, edad, nacionalidad)
        self.notas= notas
        self.universidad= universidad

class Jefe(Persona):
    
    def __init__(self, nombre, edad, nacionalidad, empresa, ganancias):
        super().__init__(nombre, edad, nacionalidad)
        self.empresa= empresa
        self.ganancias= ganancias

roberto= Empleado('Roberto', 43, 'Argentina', 'programador', '$5000')

roberto.hablar()