class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'estas haciendo una llamada desde un {self.marca} {self.modelo}')
    
    def cortar(self):
        print(f'cortaste la llamada con tu {self.marca} {self.modelo}')

celular1= Celular('motorola', 'g23', '24MP')
celular2= Celular('samsung', 'S24', '48MP')

celular1.llamar()
celular1.cortar()

celular2.llamar()
celular2.cortar()