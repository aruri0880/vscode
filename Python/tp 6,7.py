'''Definir una función "oculta_digitos" que, dada una cadena de caracteres como parámetro, devuelva como resultado la cadena con todos sus dígitos reemplazados por el carácter "*". [Ej: para el argumento "su clave es: 1540", debería devolver al programa principal "su clave es: ****" ]'''

def oculta_digitos():
    cadena= input('ingrese una cadena: ')
    caracter= input('ingrese el caracter a remplazar: ')
    cadena_sustitucion= ''
    for ind in range(len(cadena)):
        if cadena[ind] in ('0123456789'):
            cadena_sustitucion += caracter
        else:
            cadena_sustitucion += cadena[ind]
    return cadena_sustitucion