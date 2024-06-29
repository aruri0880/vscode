'''Definir una función que reciba una cadena de caracteres como parámetro y devuelva como resultado la cadena invertida. (Ej: para el argumento "Hola Undav!" debería devolver al programa principal "!vadnU aloH". No utilizar segmento de cadena [ : : -1 ] )'''

def cadena_invertida():
    cadena= input('ingrese una cadena: ')
    cadena_invertida= ''
    for ind in range(len(cadena)- 1, -1, -1):
        cadena_invertida += cadena[ind]
    return cadena_invertida