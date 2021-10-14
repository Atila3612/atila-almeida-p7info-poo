class Pilha:
    def __init__(self):
        self.elementos = list()

    def adicionar_elemento(self,novo):
        self.elementos.append(novo)
    
    def remover_elemento(self):
        del self.elementos[-1]

    def mostrar(self):
        print(*self.elementos)

pilhadefilmes = Pilha()

pilhadefilmes.adicionar_elemento("Cristão/")
pilhadefilmes.adicionar_elemento("Comédia/")
pilhadefilmes.adicionar_elemento("Ação/")

pilhadefilmes.mostrar()

pilhadefilmes.remover_elemento()

pilhadefilmes.mostrar()