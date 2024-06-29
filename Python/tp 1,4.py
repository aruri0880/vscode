''' Exprese las situaciones abajo enunciadas, mediante cambios de estado (asignación) y salidas en pantalla (función “print”). Utilice únicamente cuatro variables cuyos identificadores son dinero, paraguas, precio_unitario y cant_parag_venta:'''

''' Escriba instrucciones para pedir al usuario que ingrese la cantidad inicial de dinero en caja, la cantidad inicial de paraguas y el precio_unitario de cada paraguas; mostrar en pantalla con descripciones claras, los valores de esas tres variables.'''

def ventasA():
    dinero= int(input('ingrese la cantidad de dinero inicial: '))
    paraguas= int(input('ingrese el stock inicial de paraguas: '))
    precio_unitario= int(input('ingrese el valor al que se va a vender cada paraguas: '))
    print(f'el dinero en caja inicial es de ${dinero}')
    print(f'el stock de paraguas es de {paraguas}')
    print(f'el precio de cada paraguas es de ${precio_unitario}')

'''Agregue instrucciones para describir los cambios de estado que resultan de la venta de la quinta parte (entera) de los paraguas; mostrar en pantalla las consecuencias de la venta (cuántos paraguas vendió, cuántos quedan y cuánto dinero hay en caja).'''

def ventasB():
    dinero= int(input('ingrese la cantidad de dinero inicial: '))
    paraguas= int(input('ingrese el stock inicial de paraguas: '))
    precio_unitario= int(input('ingrese el valor al que se va a vender cada paraguas: '))
    print(f'el dinero en caja inicial es de ${dinero}')
    print(f'el stock de paraguas es de {paraguas}')
    print(f'el precio de cada paraguas es de ${precio_unitario}')
    print()
    print('post venta')
    print()
    cant_parag_venta= paraguas//5
    print(f'la cantidad de paraguas que se vendieron es de {cant_parag_venta}')
    print(f'el stock de paraguas despues de vender la quinta parte del stock es de {paraguas-cant_parag_venta}')
    print(f'el dinero en caja despues de la venta es de ${dinero+(precio_unitario*cant_parag_venta)}')

''' Agregue instrucciones para representar y mostrar la venta de la tercera parte (entera) de paraguas restantes (cuántos paraguas vendió, cuántos quedan y cuánto dinero hay)'''

def ventasC():
    dinero= int(input('ingrese la cantidad de dinero inicial: '))
    paraguas= int(input('ingrese el stock inicial de paraguas: '))
    precio_unitario= int(input('ingrese el valor al que se va a vender cada paraguas: '))
    print(f'el dinero en caja inicial es de ${dinero}')
    print(f'el stock de paraguas es de {paraguas}')
    print(f'el precio de cada paraguas es de ${precio_unitario}')
    print()
    print('post venta')
    print()
    cant_parag_venta= paraguas//3
    print(f'la cantidad de paraguas que se vendieron es de {cant_parag_venta}')
    print(f'el stock de paraguas despues de vender la tercera parte del stock es de {paraguas-cant_parag_venta}')
    print(f'el dinero en caja despues de la venta es de ${dinero+(precio_unitario*cant_parag_venta)}')