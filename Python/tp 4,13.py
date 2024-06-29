'''Escribir un programa de dudosa astrología (con solo siete signos del zodíaco) que pida al usuario que ingrese el número de día y el número de mes correspondientes a su fecha de cumpleaños, e imprima en pantalla el signo del zodíaco al que pertenece, según el criterio de fechas que se describe a continuación:'''

def signos(dia, mes):
    if dia<=0 and dia>31:
        print('fecha invalida')
    elif mes<=0 and mes>12:
        print('fecha invalida')
    else:
        if (dia>=21 and mes==3) or (dia<=20 and mes==4):
            print('tu signo es aries')
        elif (dia>=21 and mes==4) or (dia<=20 and mes==5):
            print('tu signo es tauro')
        elif (dia>=21 and mes==5) or (dia<=20 and mes==6):
            print('tu signo es geminis')
        elif (dia>=21 and mes==6) or (dia<=21 and mes==7):
            print('tu signo es cancer')
        elif (dia>=22 and mes==7) or (dia<=22 and mes==8):
            print('tu signo es leo')
        elif (dia>=23 and mes==8) or (dia<=22 and mes==9):
            print('tu signo es virgo')
        elif (dia>=23 and mes==9) or (dia<=20 and mes==3):
            print('tu signo es desde libra hasta piscis')