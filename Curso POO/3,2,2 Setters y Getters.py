class Persona:
    def __init__(self,nombre,edad):
        self.__nombre= nombre
        self.__edad= edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, new_nombre):
        self.__nombre= new_nombre
    
    def set_edad(self, new_edad):
        self.__edad= new_edad

uri= Persona('uriel', 18)

nombre= uri.get_nombre()
edad= uri.get_edad()
print(nombre)
print(edad)

uri.set_nombre('lean')
uri.set_edad(27)

nombre= uri.get_nombre()
edad= uri.get_edad()
print(nombre)
print(edad)