'''Definir una función, denominada “menor_mayor”, que reciba como parámetros (que no se deben validar) un número binario (“bi”) y dos números enteros (“x” e “y”). La función debe devolver el mayor de los dos enteros si el valor del binario es 1, o el menor de los enteros si el valor del binario es 0.'''

def menor_mayor(x, y, bi):
    if bi==1:
        if x>y:
            return x
        else:
            return y
    elif bi==0:
        if x<y:
            return x
        else:
            return y