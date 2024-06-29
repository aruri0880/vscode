'''Definir y documentar una función “es_potencia_de_dos” que reciba como parámetro un número natural, y devuelva el valor booleano True si el número es una potencia de 2, y False en caso contrario.'''

def es_potencia_de_dos():
    num= int(input('ingrese un numero natural: '))
    if num%2 == 0:
        return True
    else:
        return False

es_potencia_de_dos()