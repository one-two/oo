
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.limite = limite

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
