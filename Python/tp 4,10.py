'''Ejercicio 4.10. Definir una función denominada “es_primo”, que reciba un número natural por parámetro y devuelva un resultado booleano que indique si es primo, o no. [A diferencia de cualquier otro natural mayor que 1, un número primo solamente es divisible por sí mismo y por 1].'''

def es_primo():
    num= int(input('ingrese un numero para saber si es primo: '))
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        if (num%1 == 0 and num%num == 0) and (num%2 == 0):
            return False
        elif num%1 == 0 and num%num == 0:
            return True