class Ponto():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def setX(self,novo):
        self.x = novo
    
    def setY(self,novo):
        self.y = novo
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Reta():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def setP1(self, novo):
        self.p1 = novo

    def setP2(self, novo):
        self.p2 = novo
    
    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2

    def distancia(self):
        parteX = (self.getP2().getX() - self.getP1().getX())**2
        parteY = (self.getP2().getY() - self.getP1().getY())**2
        resultado = (parteX + parteY) ** 0.5
        
        return resultado


pontoA = Ponto(10, 0)
pontoB = Ponto(15, 20)

retaA = Reta(pontoA,pontoB)

print("A distância entre os pontos é", retaA.distancia())