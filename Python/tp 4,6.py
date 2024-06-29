'''Definir una función “cant_dias_mes” que, dados por parámetro dos números, que representan el mes y el año, devuelva como resultado la cantidad de días correspondientes al mes. En la definición se debe invocar a la función del enunciado 4.5. '''

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

def probar():
    mes= int(input('introduce un numero del mes(1-12): '))
    año= int(input('introduce el año: '))
    cantidad_dias= cant_dias_mes(mes, año)
    if cantidad_dias != -1:
        print(f'el mes {mes} del año {año} tiene {cantidad_dias} dias')
    else:
        print('el mes introducido no es valido')