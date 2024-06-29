'''Escribir un programa que elija un número al azar, entre 1 y 99, y lo mantenga
en secreto (utilice la función random.randrange (1,100) del módulo random). El programa
debe solicitar al usuario que adivine el número. Si el número que ingresa el usuario es
mayor, el programa debe responder "Incorrecto, mi número es menor"; si el número
ingresado es menor, el programa debe responder "Incorrecto, mi número es mayor". En
ambos casos deberá solicitar otro número hasta que el usuario acierte el correcto. Mostrar la
cantidad de intentos realizados para adivinar.'''

import random

def numero_al_azar():
    num_adivinar= random.randrange(1, 100)
    intentos= 0
    jugar= '*'
    while jugar=='*':
        num_elejido= int(input('ingresa un numero del 1-100: ' ))
        if num_elejido != num_adivinar:
            if num_elejido > num_adivinar:
                intentos= intentos+1
                print ('incorrecto, mi numero es menor.')
            else:
                intentos= intentos+1
                print('incorrecto, mi numero es mayor.')
        elif num_elejido == num_adivinar:
            print('numero correcto, felicidades, haz realizado {} intentos'.format(intentos))
            jugar= '+'

numero_al_azar()