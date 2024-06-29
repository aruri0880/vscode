class Miclase:
    def __init__(self):
        self._atributo_privado = 'valor'

class Miclase2:
    def __init__(self):
        self.__atributo_privado = 'valor ultra secreto'

objeto= Miclase()
print(objeto._atributo_privado)

objeto2= Miclase2()
print(objeto2.__atributo_privado)

''' un '_' significa privado y '__' significa muy privado y no se puede acceder sencillamente '''