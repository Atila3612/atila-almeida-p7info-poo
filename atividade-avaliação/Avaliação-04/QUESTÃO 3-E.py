#Metódo Construtor
class Animal():

    def __init__(self, nome, locomocao, alimentacao): #Metódo construtor, o intuito é atribuir valores às variáveis da instância
        self.nome = nome
        self.locomocao = locomocao
        self.alimentacao = alimentacao

    

tigre = ("Tigre", "Terrestre", "Carnivoro")