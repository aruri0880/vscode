'''C. Diseño de la solución 
En esta fase se va a describir cómo vamos a resolver el problema de “totofarma”. Lo primero que podemos hacer es estructurar el programa en distintas fases/funciones, las necesarias son las siguientes;'''
'''funciones para validar datos (mes, año, número de sucursal, fecha de corte, monto de ventas). Función para calcular el promedio diario de ventas y funciones principales para interactuar con el usuario y manejar los datos.'''
'''Luego vamos a ver el logaritmo propuesto y lo que tendría que hacer, lo primero sería el inicio, donde se solicite el mes y el año del informe de ventas. Lo segundo es el ingreso de datos por sucursal, hay que iterar para cada sucursal; número, nombre, fecha de corte y monto acumulado. Hay que validar cada dato ingresado hasta que sea correcto y calcular el promedio diario de ventas. Y como tercero, hacer las estadísticas finales, las cuales son mostrar la cantidad total de sucursales, calcular y mostrar el monto total de ventas de todas las sucursales y encontrar el promedio diario más bajo y más alto. 
El diseño que vamos a proponer se basa en el uso de funciones claras y bien moduladas, lo que va a hacer que facilite la validación de datos, el mantenimiento y la estabilidad del programa. 
Con este diseño detallado y estructurado, podremos implementar el programa en Python, asegurando que cumpla con todas las expectativas del proyecto en cuestión.'''

def sucursal():
    
    ingresar = '*'
    
    while ingresar == '*' :
        
        num_ingresado = int(input('ingrese el numero de sucursal(entre 100 y 199): '))
        
        if num_ingresado < 100 and num_ingresado > 199:
            print ('numero de sucursar incorrecto ingrese otro(entre 100 y 199)')
        
        elif num_ingresado >= 100 and num_ingresado <= 199:
            print ('numero de sucursal correcto.')
            ingresar = '+'
    
    num_sucursal = num_ingresado

sucursal()