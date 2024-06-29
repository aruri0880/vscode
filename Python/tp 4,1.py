'''Definir (y documentar) dos funciones:'''

'''a) una función denominada “es_par” que, dado un número entero por parámetro, devuelva un valor booleano que indique si es par, o no. Dé ejemplos de invocación.'''

def es_par(num):
    if num%2 == 0:
        return False
    else:
        return True

'''una función denominada “es_par_sn0” que, dado un número entero por parámetro, devuelva como resultado “S” si es par, “N” si es impar o el carácter “0” si es cero. '''

def es_par_sn0(num):
    if  num == 0:
        return '0'
    elif num%2 == 0:
        return 'S'
    else:
        return 'N'