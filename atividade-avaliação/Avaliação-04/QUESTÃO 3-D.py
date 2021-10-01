#Variável de Instância

class ContaBancaria():
    saldoBanco = 200 #Variável de classe, que faz parte de todos os objetos dessa classe e pode ser alterada por qualquer instância

    def __init__(self, saldo):
        self.__saldo = saldo #Variável de instância, então todas as instâncias possuirão esse valor
        ContaBancaria.saldoBanco += saldo

    def sacar(self, valor):
        self.__saldo -= valor
        ContaBancaria.saldoBanco -= valor

    def depositar(self, valor):
        self.__saldo += valor
        ContaBancaria.saldoBanco -= valor

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, novo):
        self.__saldo = novo

    

conta1 = ContaBancaria(200)

conta1.depositar(3700)
print("Valor da conta após o deposito:",conta1.getSaldo())

conta1.sacar(800)
print("Valor da conta após o saque:",conta1.getSaldo())

print("A subtração entre a diferença do valor inicial e o saque realizado após o depósito, pelo somatório dos valores de todas as variáveis:",ContaBancaria.saldoBanco)