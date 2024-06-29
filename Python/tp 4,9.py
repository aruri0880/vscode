'''. Para la siguiente secuencia de código Python 3.6, complete respectivamente el estado de las variables y la salida que se despliega en pantalla (sólo si ésta ocurre):'''

equis = 10
zeta = 20
for y in range (5, 35, 10):
    b_1 = y < equis and y < zeta
    if b_1:
        print ('--[DEBUG]:', y, 'es menor')
    elif equis < y and zeta < y:
        print ('--[DEBUG]:', y, 'es mayor')
    else:
        print ('--[DEBUG]:', y, 'en medio')
    for b_2 in (True, False):
        print (b_1, 'y', b_2, '=', b_1 and b_2)
        print (b_1, 'o', b_2, '=', b_1 or b_2)
        print ('-' * 10)

print ( 'y:', y, 'b_1:', b_1, 'not b_1:', not b_1)