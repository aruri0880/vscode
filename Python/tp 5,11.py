'''Modificar el programa del enunciado 5.3, para que el usuario pueda dar por terminado el juego, ingresando el valor 0.'''

import random

def numero_al_azar():
    num_adivinar= random.randrange(1, 100)
    intentos= 0
    jugar= input('desea jugar a adivinar? <si-no>')
    while jugar=='si':
        num_elejido= int(input('ingresa un numero del 1-100: ' ))
        if num_elejido == 0:
            return 'juego finalizado'
        elif num_elejido != num_adivinar:
            if num_elejido > num_adivinar:
                intentos= intentos+1
                print ('incorrecto, mi numero es menor.')
            else:
                intentos= intentos+1
                print('incorrecto, mi numero es mayor.')
        elif num_elejido == num_adivinar:
            return 'numero correcto, felicidades, haz realizado {} intentos'.format(intentos)