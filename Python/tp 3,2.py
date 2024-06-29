'''Definir (y documentar) con nombre apropiado, dos funciones:'''

'''a) Una función que reciba por parámetros dos números, que representan la base y el exponente, y devuelva como resultado la potencia de la base elevada al exponente'''

def base_elevada(numero, exponente):
    numero_elevado= numero**exponente
    print(numero_elevado)

'''Una función que compruebe el funcionamiento de la función del ejercicio a) mostrando en pantalla, con descripciones claras, los resultados que devuelve para los valores: 2 0, 2 1, 2 2, 2 3, 2 4, 2 5 y 36 0.5.'''

base_elevada(2, 0)
base_elevada(2, 1)
base_elevada(2, 2)
base_elevada(2, 3)
base_elevada(2, 4)
base_elevada(2, 5)
base_elevada(36, 0.5)