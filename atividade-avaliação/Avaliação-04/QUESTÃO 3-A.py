#Herança
class Residencia():
    def __init__(self, quartos, salas, banheiros):
        self.quartos = quartos
        self.salas = salas
        self.banheiros = banheiros
    def mostrar(self):
        print("Quartos:", self.quartos)
        print("Salas:", self.salas)
        print("Banheiros:", self.banheiros)
    
class Casa(Residencia):
    def __init__(self, quartos, salas, banheiros, cozinhas):
        super(Casa, self).__init__(quartos,salas,banheiros)
        self.cozinhas = cozinhas

    def mostrar(self):
        super(Casa, self).mostrar()
        print("Cozinhas:", self.cozinhas)
    

minha = Casa(3, 2, 1, 1)
minha.mostrar()