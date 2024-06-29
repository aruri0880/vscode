'''Definir dos funciones. Una función denominada…
a) ‘interseccion’ que reciba por parámetro dos listas, que representan conjuntos, y
devuelva como resultado otra lista que incluya, sin repeticiones, los elementos
comunes a ambas listas pasadas como argumentos.'''

def interseccion(list1, list2):
    lista= []
    for elem in list1:
        if elem in list2 and elem not in lista:
            lista.append(elem)
    return lista

'''b) ‘union’ que reciba por parámetro dos listas, que representan conjuntos, y devuelva
como resultado otra lista que incluya, sin repeticiones, los elementos que
pertenezcan a una u otra lista pasadas como argumentos.
'''

def union():
    