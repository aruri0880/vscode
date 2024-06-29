''' Definir una función “intercala_chr” que, dados como parámetros una cadena de caracteres y un carácter, devuelva como resultado la cadena con el carácter insertado entre sus caracteres originales. [Ej: para los argumentos "veamos" y "-", debería devolver al programa principal "v-e-a-m-o-s" ]'''

def intercala_chr():
    cadena= input('ingrese una cadena: ')
    caracter= input('ingrese un caracter: ')
    resultado= ''
    for ind in range(len(cadena)):
        resultado += cadena[ind]
        if ind != len(cadena) -1:
            resultado += caracter
    return resultado

intercala_chr()