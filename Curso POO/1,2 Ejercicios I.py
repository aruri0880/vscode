'''crear una clase 'estudiante' que tenga los atributos nombre, edad y grado, ademas agregar un metodo que se llame 'estudiar', que imprima el mensaje 'el estudiante (nombre) esta estudiando', el usuario debe dar los datos para los atributos '''

class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')

nombre= input('ingrese el nombre del estudiante: ')
edad= input('ingrese la edad del estudiante: ')
grado= input('ingrese el grado del estudiante: ')

estudiante1= Estudiante(nombre, edad, grado)

estudiante1.estudiar()
print(estudiante1.nombre)
print(estudiante1.edad)
print(estudiante1.grado)