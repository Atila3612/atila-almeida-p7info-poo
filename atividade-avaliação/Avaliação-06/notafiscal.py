import datetime
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal
from bancodados import db

class NotaFiscal(db.Model):
    __tablename__ = 'TB_NOTA_FISCAL'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    idcliente = db.Column(db.Integer, db.ForeignKey("TB_CLIENTE.id"), nullable=False)
    data = db.Column(db.String, nullable=False)
    itens = db.relationship("ItemNotaFiscal", backref="NotaFiscal", lazy=True)

    def __init__(self, id, codigo, idcliente):
        self.id = id
        self.codigo=codigo
        self.idcliente=idcliente
        self.data=datetime.datetime.now()

    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor

    def imprimirNotaFiscal(self):
        pass