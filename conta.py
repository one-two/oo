
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def saque(self, valor):
        self.__saldo -= valor
        return self.__saldo

    def deposita(self, valor):
        self.__saldo += valor
        return self.__saldo

    def extrato(self):
        print("O saldo de {0} é {1}".format(self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite: str):
        self.__limite = limite
