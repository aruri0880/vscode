'''Definir una función "es_subcadena" que, dadas por parámetro dos cadenas de caracteres, devuelva un resultado booleano que indique si la primera cadena está contenida en la segunda. [Ej: la cadena "bandera" es subcadena de "abanderado".]'''

def es_subcadena():
    cadena1= input('ingrese una cadena: ')
    cadena2= input('ingrese otra cadena: ')
    if cadena1 in cadena2:
        return True
    else:
        return False