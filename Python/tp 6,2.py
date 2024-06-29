'''Definir una función “segm_3_txt” que, dados como parámetros una cadena de caracteres y un carácter (que denominaremos selector),
a) imprima los tres primeros caracteres de la cadena, si el valor del selector es la letra "P", o los tres últimos caracteres si el valor del selector es "U", o el mensaje "Error en el selector" si el valor del selector no es "P" ni "U".'''

def segm_3_txt():
    cad= input('ingrese una cadena de caracteres: ' )
    sel= input('ingrese un selector <p-u>: ' )
    if (sel != 'p') and (sel != 'u'):
        print ('error en el selector')
    elif sel == 'p':
        print (cad)
        print (cad[:3])
    elif sel == 'u':
        print (cad)
        print (cad[-3:])

'''b) agregar instrucciones a la solución anterior, para que sólo imprima el primero o el último carácter, respectivamente, cuando la longitud de la cadena sea menor que 3. '''

def segm_1_txt():
    cad= input('ingrese una cadena de caracteres: ' )
    sel= input('ingrese un selector <p-u>: ' )
    if len(cad)<3:
        if (sel != 'p') and (sel != 'u'):
            print ('error en el selector')
        elif sel == 'p':
            print (cad)
            print (cad[:1])
        elif sel == 'u':
            print (cad)
            print (cad[-1:])
    else:
        if (sel != 'p') and (sel != 'u'):
            print ('error en el selector')
        elif sel == 'p':
            print (cad)
            print (cad[:3])
        elif sel == 'u':
            print (cad)
            print (cad[-3:])