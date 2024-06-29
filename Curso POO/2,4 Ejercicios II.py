'''Ejercicio 1'''

'''crear un sistema para una escuela. en este sistema, vamos a tener dos clases principales: 'persona' y 'estudiante'. la clase persona tendra los atributos de nombre y edad y un metodo que imprima el nombre y edad de la persona. la clase estudiante heredara de la clase persona y tambien tendra un atributo adicional: grado y un metodo que imprima el grado del estudiante.'''

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

class Estudiante(Persona):
    
    def __init__(self, nombre, edad, grado):
        
        super().__init__(nombre, edad)
        self.grado= grado
    
    def mostrar_grado(self):
        print(f'Grado: {self.grado}')

'''deberas utilizar super en el metodo de inicializacion (init) para reutilizar el codigo de la clase padre (Persona). luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funciona correctamente.'''

estudiante1= Estudiante('uriel', 18, 1)

estudiante1.mostrar_datos()
estudiante1.mostrar_grado()

'''Ejercicio 2'''

'''imagina que estas modelando animales en un zoologico. crea tres clases: 'Animal', 'Mamifero' y 'Ave'. la clase animal debe tener el metodo 'comer'. la clase mamifero debe tener el metodo 'amamantar' y la clase ave debe tener el metodo 'volar'.'''

class Animal:
    def comer(self):
        print('el animal esta comiendo')

class Mamifero(Animal):
    def amamantar(self):
        print('el animal esta amamantando')

class Ave(Animal):
    def volar(self):
        print('el animal esta volando')

'''ahora crea una clase 'murcielago que herede de mamifero y ave en ese orden y por lo tanto debe ser capaz de amamantar y volar ademas de comer'''

class Murcielago(Mamifero, Ave):
    pass

'''finalmente juega con el orden de herencia de la clase murcielago y observa como cambia el MRO y el comportamiento de los metodos al usar super().'''

print('animal:')
animal= Animal()

animal.comer()

print('ave:')
ave= Ave()

ave.comer()
ave.volar()

print('mamifero:')
mamifero= Mamifero()

mamifero.comer()
mamifero.amamantar()

print('murcielago:')
murcielago= Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()

print('orden de MRO:')

print(Murcielago.mro())