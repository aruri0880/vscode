'''Escribir un programa que reciba, una a una, las calificaciones del usuario, preguntando a cada paso si desea ingresar más notas; finalmente, el programa debe imprimir el promedio correspondiente y el valor de la calificación más baja'''

def calificaciones():
    
    notas= ()
    ingresar= '*'
    
    while ingresar == '*':
        
        nota_ingresada= input('ingrese una calificacion(para salir ingrese un numero negativo): ')
        
        if nota_ingresada > 0:
            notas += (nota_ingresada,)
        
        elif nota_ingresada < 10:
            notas += (nota_ingresada,)
        
        elif nota_ingresada < 0:
            ingresar= '+'
        
        print(f'el promedio de las notas es de {sum(notas)/len(notas)}')
        print(f'la nota mas baja es de {min(notas)}')