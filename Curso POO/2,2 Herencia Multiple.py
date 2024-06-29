class Persona:
    
    def __init__(self, nombre, edad, nacionalidad):
        
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
    
    def hablar(self):
        print('hola, estoy hablando un poco')

class Artista:
    
    def __init__(self, habilidad):
        
        self.habilidad= habilidad
    
    def mostrar_habilidad(self):
        return f'la habilidad del artista es {self.habilidad}'

class EmpleadoArtista(Persona,Artista):
    
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario= salario
        self.empresa= empresa
    
    def presentarse(self):
        print (f'hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}')

roberto= EmpleadoArtista('roberto', 34, 'Argentina', 'cantar', 10000, 'google')

herencia= issubclass(Artista, Persona)
instancia= isinstance(roberto, Artista)

print(instancia)