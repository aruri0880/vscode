'''Examine el resultado de ejecutar en Python 3 la función main() y elabore conclusiones: señale definiciones e invocaciones de función, distinga formas de invocación, señale argumentos y parámetros. Comente con “#” invocaciones a la función print () que incluyan la palabra Debug y pruebe la ejecución. Ejecute la instrucción comentada con “#”:'''

def triplica(param):
    """ Recibe valor en param y devuelve el valor de resulta """
    print ('----[Debug] valor de param es:', param)
    resulta = param * 3
    return resulta

def prueba_triplica(zapatos, sombrero):
    """ Recibe valores en zapatos y sombrero.
    Muestra resultados de invocaciones """
    print ('--[Debug] valores de parámetros:',zapatos,'/',sombrero)
    print ('--[Debug] valor del argumento:', zapatos)
    salida = triplica(zapatos)
    print ('La salida con', zapatos, 'es ==>', salida)
    print ('\n--[Debug] valor del argumento:', sombrero)
    salida = triplica(sombrero)
    print ('La salida con', sombrero, 'es ==>', salida)
    print ('\nError de invocacion sin paréntesis ==>', triplica )

def main():
    prueba_triplica(40, 'paño')
    print ('\n-[ Debug ] valor del argumento:', 200 )
    print ('La salida de', 200, 'es ==>', triplica(200) )
    #print ('Error: invoca sin argumentos ==>', triplica())