'''Definir y documentar una función denominada “val_abs”, que reciba un número por parámetro y devuelva como resultado su valor absoluto.'''

def val_abs(num):
    if num>=0:
        return num
    else:
        return -num

def val_abs_alt(num):
    return abs(num)