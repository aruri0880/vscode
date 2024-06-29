'''a) escribir una funcion que reciba dos tuplas de numeros enteros como numeros enteros:'''
'''si las tuplas tienen diferente longitud debera devolver una tupla vacia. en caso contrario debera devolver una tupla de la misma longitud, en el cual cada elemento estara relacionado a la suma de los respectivos elementos de cada tupla(elementos en la misma posicion de ambas tuplas):'''
'''*si la suma es multiplo de 3, el elemento de la tupla tiene que ser la cadena "tres"'''
'''*si la suma es multiplo de 5, el elemento de la tupla tiene que ser la cadena "cinco"'''
'''*si la suma es multiplo 3 y de 5, el elemento de la tupla tiene que ser la cadena"quince"'''
'''*si la suma no es multiplo de 3 ni de 5, el elemento de la tupla tiene que ser el resultado de la suma'''



def suma_tuplas_original():
    tup_vacia= ()
    tup1= (1, 9, 12, 10)
    tup2= (5, 6, 8, 1)
    if len(tup1) != len(tup2):
        return tup_vacia
    elif len(tup1) == len(tup2):
        for ind in range(len(tup1)):
            if (tup1[ind] + tup2[ind]) % 3 == 0:
                tup_vacia += ('tres',)
            elif (tup1[ind] + tup2[ind]) % 5 == 0:
                tup_vacia += ('cinco',)
            elif (tup1[ind] + tup2[ind]) % 3 == 0 and (tup1[ind] + tup2[ind]) % 5 == 0:
                tup_vacia += ('quince',)
            else:
                tup_vacia += ((tup1[ind] + tup2[ind]),)
        return tup_vacia

'''_____________________________________________'''
'''                                             '''

def suma_tuplas(tup1, tup2):
    tup_vacia= ()
    if len(tup1) != len(tup2):
        return tup_vacia
    elif len(tup1) == len(tup2):
        for ind in range(len(tup1)):
            if (tup1[ind] + tup2[ind]) % 3 == 0:
                tup_vacia += ('tres',)
            elif (tup1[ind] + tup2[ind]) % 5 == 0:
                tup_vacia += ('cinco',)
            elif (tup1[ind] + tup2[ind]) % 3 == 0 and (tup1[ind] + tup2[ind]) % 5 == 0:
                tup_vacia += ('quince',)
            else:
                tup_vacia += ((tup1[ind] + tup2[ind]),)
        return tup_vacia

'''escribir un programa para probar la funcion anterior'''

def probar_suma():
    tuplas=(
        ((1, 9, 12, 10), (5, 6, 8, 1)),
        ((10, 15, 20), (3, 6, 9)),
        ((7, 8), (2, 3, 4)),
        ((4, 6, 9), (2, 4, 6)),
        ((1, 2, 3), (4, 5, 6))
    )
    
    for tup1, tup2 in tuplas:
        resulta= suma_tuplas(tup1, tup2)
        print(f'tupla 1: {tup1}')
        print(f'tupla 2: {tup2}')
        print(f'resultado: {resulta}')
        print()