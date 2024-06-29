'''Implementar tres algoritmos, cuyos objetivos respectivos sean:'''

'''a) Obtener el perímetro de un rectángulo, dada su base y su altura'''

def perimetro():
    base= int(input('ingrese el valor de la base: '))
    altura= int(input('ingrese el valor de la altura: '))
    print('el perimetro del rectangulo es de base {} por altura {}'.format(base, altura))

'''b) Obtener el área de un rectángulo, dada su base y su altura.'''

def area():
    base= int(input('ingrese el valor de la base: '))
    altura= int(input('ingrese el valor de la altura: '))
    area= base*altura
    print('el area del rectangulo por la base de {} y la altura de {} es de {}'.format(base, altura, area))

'''c) Dados dos números n1 y n2, mostrar la suma, resta, multiplicación, división y división entera de ambos. Analizar el resultado, con los números: 5 y 2 ; 2 y 5 ; 5 y 0.'''

def calculos():
    n1= int(input('ingrese un numero entero: '))
    n2= int(input('ingrese otro numero entero: '))
    suma= n1+n2
    multiplicacion= n1*n2
    division= n1/n1
    division_entera= n1//n2
    print('la suma de {} y {} es de {}'.format(n1, n2, suma))
    print('la multiplucacion de {} y de {} es de {}'.format(n1, n2, multiplicacion))
    print('la division de {} y {} es de {}'.format(n1, n2, division))
    print('la division entera de {} y {} es de {}'.format(n1, n2, division_entera))