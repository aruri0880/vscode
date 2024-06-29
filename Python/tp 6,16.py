''' Definir una función ‘binario_a_decimal’ que reciba por parámetro una
cadena de unos y ceros (es decir, un número en representación binaria) y devuelva
como resultado el valor decimal correspondiente. [Ej: para el argumento ‘0111’ debería
devolver al programa principal el valor 7, para ‘1000’ el valor 8, etc.]
'''

def binario_a_decimal():
    argumento= int(input('ingresa un numero binario: '))
    resultado= chr(argumento)
    return resultado

binario_a_decimal()