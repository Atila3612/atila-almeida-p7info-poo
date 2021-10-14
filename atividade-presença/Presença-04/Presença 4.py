class Fila:
    def __init__(self):
        self.elementos = list()

    def adicionar_elemento(self,novo):
        self.elementos.append(novo)
    
    def remover_elemento(self):
        del self.elementos[0]
    
    def mostrar(self):
        print(*self.elementos)

filaDeProdutosNaEsteira = Fila()

filaDeProdutosNaEsteira.adicionar_elemento("Frutas/")
filaDeProdutosNaEsteira.adicionar_elemento("Escova de dentes/")
filaDeProdutosNaEsteira.adicionar_elemento("Material escolar/")

filaDeProdutosNaEsteira.mostrar()

filaDeProdutosNaEsteira.remover_elemento()

filaDeProdutosNaEsteira.mostrar()