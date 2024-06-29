''' Implementar dos algoritmos que resuelvan los siguientes problemas:'''

'''a) Dado un número natural n, imprimir su tabla de multiplicar desde 0 hasta n. '''

def multiplicacion():
    num= int(input('ingrese un numero que quiera ver su tabla de multilicar: '))
    for i in range(0, num+1):
        print(f'la multiplicacion de {i} y {num} es {num*i}')

'''b) Dado un número natural n, imprimir la suma total de los naturales de 1 a n'''

def suma():
    num= int(input('ingrese un numero que quiera ver sus sumas: '))
    for i in range(1, num+1):
        print(f'la suma de {i} y {num} es {num+i}')