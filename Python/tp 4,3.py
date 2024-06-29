'''Ejercicio 4.3. Definir una función denominada “mayor_de_3” que devuelva como resultado el mayor de tres números dados por parámetro. Pruebe la función con 6 ternas de valores.'''

def mayor_de_3(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3