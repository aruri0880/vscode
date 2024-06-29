'''Definir una función que reciba como parámetro un número natural e imprima todos los números primos que hay hasta ese número. Utilice la función del ejercicio 4.10.'''

def es_primo(num):
    if num<=1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

def todos_primos():
    num= int(input('ingrse un numero natural: '))
    for elem in range(1, num+1):
        print (elem)
        print(es_primo(elem))