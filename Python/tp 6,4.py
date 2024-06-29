'''Definir una función que reciba una cadena de caracteres como parámetro e imprima la cadena original yuxtapuesta a la cadena invertida. [Ej: para el argumento "espejo" debería imprimir "espejoojepse" ]. ¿Qué función debería invocar?'''

def yuxtapuesta():
    cadena= input('ingrese una cadena: ')
    cadena_yuxtapuesta= (cadena)+''
    for ind in range(len(cadena)-1 , -1, -1):
        cadena_yuxtapuesta += cadena[ind]
    return cadena_yuxtapuesta

yuxtapuesta()