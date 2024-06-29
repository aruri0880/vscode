'''Definir una función ‘producto_escalar’, que reciba como parámetros dos
tuplas, que representan vectores de igual dimensión, y devuelva como resultado el valor de
su producto escalar. [El producto escalar de los vectores (u1, u2, u3) y (v1, v2, v3), se puede
calcular como el valor numérico que resulta de sumar los productos de las componentes
homólogas: u1 * v1 + u2 * v2 + u3 * v3]
'''

def producto_escalar(tup1, tup2):
    tup_vacia= ()
    if len(tup1) != len(tup2):
        return tup_vacia
    elif len(tup1) == len(tup2):
        for ind in range(len(tup1)):
            tup_vacia += (tup1[ind] * tup2[ind],)
    return tup_vacia

producto_escalar((1,2,3,4),(5,6,7,8))