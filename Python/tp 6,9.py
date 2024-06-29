'''Definir una función que, dadas dos cadenas de caracteres como parámetros, devuelva como resultado la cadena que sea anterior en orden alfabético. [Ej: para los argumentos "kde" y "gnome" debería devolver al programa principal "gnome" ]'''

def anterior_alfabetico():
    argumento1= input('ingrese una cadena: ')
    argumento2= input('ingrese otra cadena: ')
    if argumento1 > argumento2:
        return argumento2
    else:
        return argumento1 