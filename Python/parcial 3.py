'''escribir una funcion que oculte digitos, que dados como parametors una cadena de caracteres y un caracter, devuelva como salida una tupla con los siguientes elementos:'''
'''la cadena original'''
'''la cadena original sin los caracteres que representan los digitos del 0 a 9, estos remplazados por el caracter parametro de entrada.'''

def oculta_digitos (cad,car):
    cad_remp= ''
    cad_tup= (cad, )
    for ind in range(len(cad)):
        if cad[ind] in ('0123456789'):
            cad_remp += car
        else:
            cad_remp += cad[ind]
    cad_tup += (cad_remp,)
    return cad_tup