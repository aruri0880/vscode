'''escribir un programa que solicite al usuario el ingreso de varias notas numeriacas de 0 a 10, el ingreso se terminara cuando el usuario ingrese un numero negativo.'''
'''el programa debera inprimir de forma descriptiva:'''
'''la cantidad de notas ingresadas, la mayor de las notas ingresadas, la cantidad de desaprobados(nota menor que 4) y el promedio de las notas'''

def notas_numericas():
    notas= ()
    notas_desaprobados= ()
    ingresar= input('quiere ingresar una nota? <si-no>')
    while ingresar == 'si':
        nota_ingresada= int(input('ingrese una nota del 0 al 10(para salir ingrese un numero negativo) ' ))
        if nota_ingresada >= 4:
            notas += (nota_ingresada,)
        elif nota_ingresada < 4 and nota_ingresada > 0:
            notas += (nota_ingresada,)
            notas_desaprobados += (nota_ingresada,)
        else:
            print(f'la cantidad de notas ingresadas son {len(notas)}')
            print(f'la cantidad de desaprobados es de {(len(notas_desaprobados))}')
            print(f'la nota mas alta es {max(notas)}')
            print(f'el promedio de las notas es de {(sum(notas))/(len(notas))}')
            print(notas)
            return