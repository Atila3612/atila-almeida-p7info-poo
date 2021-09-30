class ContaBancaria():
    def __init__(self, saldo):
        self.__saldo = saldo #Atributo privado

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, novo):
        self.__saldo = novo

conta1 = ContaBancaria(3500)

conta1.depositar(300)
print("Valor da conta após o depósito:",conta1.getSaldo())

conta1.sacar(1000)
print("Valor da conta após o saque:",conta1.getSaldo())

print("Isso para casos em que o depósito seja realizado primeiro e o saque em seguida")