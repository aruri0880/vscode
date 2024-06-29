'''Definir una función "separa_miles" que, dada por parámetro una cadena de caracteres que contiene un largo número entero, devuelva como resultado la cadena con las separaciones de miles incluidas en el número. [Ej: para el argumento "1234567890" debería devolver al programa principal "1.234.567.890" ]'''

def separa_miles():
    cadena= input('ingrese una cadena: ')
    cadena_sustitucion= ''
    if cadena[0] == '-':
        cadena_sustitucion += '-'
        cadena = cadena[1:]
    for ind in range(len(cadena)):
        cadena_sustitucion += cadena[ind]
        if (len(cadena) - ind -1) % 3 == 0 and ind != len(cadena) - 1:
            cadena_sustitucion += '.'
    return cadena_sustitucion