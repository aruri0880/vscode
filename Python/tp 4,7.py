'''Definir una función “fecha_valida” que, dada por parámetros una fecha en
números (día, mes, año), devuelva un resultado booleano que indique si es válida o no.
¿Qué función debería invocar?'''

def es_bisiesto(año):
    if (año%4==0 and año%100!=0) or (año%400==0):
        return True
    else:
        return False

def cant_dias_mes(mes, año):
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 29
    elif mes==2:
        if es_bisiesto(año):
            return 29
        else:
            return 28
    else:
        return -1

def fecha_valida(dias, mes, año):
    if mes<1 or mes>12:
        return False
    if dias<1 or dias>cant_dias_mes(mes, año):
        return False
    return True

dias= int(input('ingrese el dia: '))
mes= int(input('ingrese el mes: '))
año= int(input('ingrese el año: '))

if fecha_valida(dias, mes, año):
    print(True)
else:
    print(False)