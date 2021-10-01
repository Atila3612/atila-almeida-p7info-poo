class Filme():
    def __init__(self, id, nome, diretor):
        self.id = id
        self.nome = nome
        self.diretor = diretor

class Diretor():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.obras = list()

    def adicionarFilme(self, filme):
        self.obras.append(filme)

    def mostrarFilmes(self):
        for a in self.obras:
            print("ID:", a[0])
            print("Nome:", a[1])
            print()

diretorABC = Diretor(1, "Diretor ABC")

filmeA = [1, "A paixão de Cristo"]
filmeB = [2, "Jurassic Park"]

diretorABC.adicionarFilme(filmeA)
diretorABC.adicionarFilme(filmeB)

diretorABC.mostrarFilmes()