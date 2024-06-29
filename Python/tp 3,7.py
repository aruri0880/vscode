'''denominada “numero_pi”, que devuelva como resultado el valor redondeado del número PI: 3.14159. [Utilice el dato math.pi del módulo math y la función round(n, d) ]'''

import math

def numero_pi():
    return round(math.pi, 5)

'''con nombre apropiado, que reciba el radio de un círculo por parámetro y devuelva como resultado el valor del área respectiva. Utilice la función del ítem a).'''

def area():
    radio= int(input('ingrese el radio del circulo: '))
    area= numero_pi()*(radio**2)
    return area