''' Definir una función ‘suma_vectores’ que, dadas por parámetro dos tuplas que representan vectores de igual dimensión, devuelva como resultado la tupla que representa su suma. [La suma de vectores ( u1, u2, u3 ) y ( v1, v2, v3 ), se puede calcular como el vector que resulta de sumar sus componentes homólogas: ( u1 + v1 , u2 + v2 , u3 + v3 ) ].'''

def suma_vectores(tup1, tup2):
    tup_vacia= ()
    if len(tup1) != len(tup2):
        return tup_vacia
    elif len(tup1) == len(tup2):
        for ind in range(len(tup1)):
            tup_vacia += (tup1[ind] + tup2[ind],)
    return tup_vacia