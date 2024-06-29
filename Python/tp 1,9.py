'''Reescribir el programa del ejercicio 1.3 para que pida al usuario que ingrese la cantidad de agua inicial del tanque y la pileta, y que muestre los cambios, al transvasar un balde, luego otros dos, luego otros tres, luego otros cuatro, otros cinco y otros seis.'''

def main():
    tanque = int(input('ingrese la cantidad de litros que contiene el tanque: '))
    pileta = int(input('ingrese la cantidad de litros que contiene la pileta: '))
    balde = 10
    print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
    cant_baldes = 1 # Esta variable representa la cantidad de veces que cargo el balde
    print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
    tanque = tanque - cant_baldes * balde
    pileta = pileta + cant_baldes * balde
    print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
    cant_baldes = cant_baldes + 1
    print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
    tanque = tanque - cant_baldes * balde
    pileta = pileta + cant_baldes * balde
    print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )
    cant_baldes = cant_baldes + 1
    print ( 'Transvasa', cant_baldes, 'baldes de agua de:', balde, 'litros' )
    tanque = tanque - cant_baldes * balde
    pileta = pileta + cant_baldes * balde
    print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros' )