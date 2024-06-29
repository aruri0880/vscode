'''Para la siguiente porción de código Python 3.6, complete respectivamente el estado de la variable y la salida que se despliega en pantalla (sólo siésta ocurre):'''

tengo= 10

while tengo<25:
    print(f'{tengo} // 3: {tengo//3}')
    if tengo %3>0:
        print(f'{tengo} % 3: {tengo%3}')
    print('-' *(tengo//3))
    tengo= tengo+5