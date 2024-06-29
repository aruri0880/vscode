'''Un usuario, nos pide que desarrollemos un programa para convertir a grados Celsiusalgunos valores de temperaturas expresadas en grados Fahrenheit. Se espera que elprograma pregunte al usuario cuántos valores de temperaturas desea convertir y, en base aese dato, que le solicite el ingreso de los valores expresados en grados Fahrenheit paramostrarlos ya convertidos a grados Celsius. Para realizar la transformación entre unidadesde medida, el usuario nos dice que la fórmula para conversión de grados Celsius a grados Fahrenheit es:'''

'''F = 9 / 5 x C + 32'''

'''Por último, el usuario nos pide, que el programa muestre un saludo de despedida para dejar en claro la finalización de su ejecución.'''

def temperatura():
    F= int(input('ingrese la temperatura en grados Fahrenheit: '))
    C= int(input('ingrese la temperatura en grados Celsius: '))
    gradosC= (F-32)*5/9
    gradosF= (C*9/5)+32
    print('los grados Fahrenheit {} covetirdos a Celsius son {}.'.format(F, gradosC))
    print('los grados Celsius {} convertidos a Fahrenheit son {}.'.format(C, gradosF))
    print('con esto concluye el progama, saludos cordiales.')