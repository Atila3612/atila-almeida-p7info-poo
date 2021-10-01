class Conta():
    def __init__(self, id, *itens):
        self.id = id
        self.itens = list(map(lambda x : x.__dict__, itens))

    def pagamento(self):
        print("Pratos pedidos:")
        for a in self.itens:
            print(a["nome"])
        print("Total a pagar:", sum(list(map(lambda x : x["preco"], self.itens))))


class itemPedido():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

conta1 = Conta(1, itemPedido("Lasanha", 40), itemPedido("Sorvete",15))
conta1.pagamento()