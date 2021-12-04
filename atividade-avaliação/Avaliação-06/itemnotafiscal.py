from bancodados import db

from produto import Produto

class ItemNotaFiscal(db.Model):
    __tablename__ = 'TB_ITEM_NF'

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    idproduto = db.Column(db.Integer, db.ForeignKey("TB_PRODUTO.id"), nullable=False)
    idnotafiscal = db.Column(db.Integer, db.ForeignKey("TB_NOTA_FISCAL.id"), nullable=False)

    def __init__(self,id,sequencial,quantidade,idproduto,idnotafiscal):
        self.id=id
        self.sequencial=sequencial
        self.quantidade=quantidade
        self.idproduto=idproduto
        self.idnotafiscal=idnotafiscal

        produtos = Produto.query.all()
        for produto in produtos:
            self.descricao = produto.descricao
            self.valorUnitario = produto.valorUnitario
            self.valorItem=float(self.quantidade * self.valorUnitario)

    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(self.valorItem, self.valorUnitario, self.descricao, self.quantidade, self.sequencial, self.id)
        return string

if __name__ == '__main__':
    it1 = ItemNotaFiscal(1, 1, 10, 1, 0)
    print(it1.str())