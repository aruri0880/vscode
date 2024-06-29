class Persona:
    def __init__(self, nombre, edad):
        self.__nombre= nombre
        self._edad= edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre= new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre

uri= Persona('uriel', 18)

nombre= uri.nombre
print(nombre)

uri.nombre= 'pepe'

nombre= uri.nombre
print(nombre)

del uri.nombre

print('que haces maquina')