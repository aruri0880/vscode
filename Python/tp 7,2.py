'''Definir una función …
a) que reciba como parámetro una tupla tup con nombres, y para cada nombre imprima el mensaje “Estimado <nombre>, vote por mí “.'''

def voto():
    nombre= input('ingrese un nombre: ')
    tup_vacia= ()
    for ind in range(len(nombre)):
        tup_vacia += (nombre,)
    print ('estimado ', tup_vacia[ind], ', vote por mi ')

'''b) modificar la solución anterior, para que el mensaje distinga el género del destinatario, considerando que tup es una tupla integrada por tuplas de la forma (nombre, género). [ Valores de género: ‘M’ → masculino; ‘F’ → femenino; ‘O’ → otres ]'''

def voto_con_genero():
    nombre= input('ingrese un nombre: ')
    genero= input('ingrese su genero <M-F-O>')
    tup_nombres= ()
    tup_generos= ()
    for elem in range(len(genero)):
        tup_generos += (genero,)
    for ind in range(len(nombre)):
        tup_nombres += (nombre,)
    tup_mensaje= tup_nombres[ind], tup_generos[elem]
    print ('estimado ', tup_mensaje, ', vote por mi ')