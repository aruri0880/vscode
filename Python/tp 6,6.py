'''Definir una función “sustituye_chr” que, dados como parámetros una cadena de caracteres txt y dos caracteres c1 y c2, devuelva como resultado una cadena con la sustitución, en txt, de todos los caracteres iguales a c1, por el carácter c2. [Ej: pasados como argumentos el texto "mi primer modulo.py", el carácter " " y el carácter "_", debería devolver al programa principal "mi_primer_modulo.py" ]'''

def sustituye_chr():
    cadena= input('ingrese una cadena: ')
    caracter1= input('ingrese el caracter a remplazar: ')
    caracter2= input('ingrese el caracter que remplazara al primero: ')
    cadena_sustitucion= ''
    for ind in range(len(cadena)):
        if cadena[ind] in caracter1:
            cadena_sustitucion += caracter2
        else:
            cadena_sustitucion += cadena[ind]
    return cadena_sustitucion