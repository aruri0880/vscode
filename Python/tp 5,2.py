'''que contenga una contraseña de 4 caracteres inventada, que le pregunte al usuario la contraseña y no le permita continuar hasta que la haya ingresado correctamente.'''

def claveA():
    clave_oculta= int(1111)
    ingresar= '*'
    while ingresar == '*':
        clave_ingresada= int(input('ingrese una clave: '))
        if clave_ingresada == clave_oculta:
            ingresar= '+'
        elif clave_ingresada != clave_oculta:
            print('clave incorrecta')

'''Modificar el programa anterior para que solamente permita una cantidad fija de intentos. Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.'''

def claveB():
    clave_oculta= int(1111)
    cant_intentos= 3
    intentos= 0
    ingresar= '*'
    while ingresar == '*':
        clave_ingresada= int(input('ingrese una clave: '))
        if clave_ingresada != clave_oculta:
            intentos= intentos+1
            print('la clave es incorrecta, fallaste {} intentos de {}'.format(intentos, cant_intentos))
            if intentos >= cant_intentos:
                print('sin intentos restantes')
                ingresar= '+'
        elif clave_ingresada == clave_oculta:
            print ('eureka')
            ingresar= '+'

'''Modificar el programa anterior para que después de cada intento agregue una
pausa cada vez mayor, utilizando la función time.sleep(…) del módulo time'''

import time

def claveC():
    clave_oculta= int(1111)
    cant_intentos= 3
    intentos= 0
    t= 3
    ingresar= '*'
    while ingresar == '*':
        clave_ingresada= int(input('ingrese una clave: '))
        if clave_ingresada != clave_oculta:
            intentos= intentos+1
            print('la clave es incorrecta, fallaste {} intentos de {}'.format(intentos, cant_intentos))
            time.sleep(t)
            t= t+1
            if intentos >= cant_intentos:
                print('sin intentos restantes')
                ingresar= '+'
        elif clave_ingresada == clave_oculta:
            print('eureka')
            ingresar= '+'