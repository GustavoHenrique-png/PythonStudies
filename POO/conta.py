#Criação da classe
class Conta(object):
    #Contrutor do objeto
    #Uma classe, uma responsabilidade
    #Self é a referência na memória onde o objeto está
    def __init__(self, numero, nome, saldo,limite):
        #__init__ é o que marca o construtor da função
        #Acessando atributo numero do objeto
        # Uso de 2 underlines para 'privar a variavel' ocultando ela de outras classes 
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print('O saldo do: {} é de: ${}'.format(self.__nome,self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def tranferencia(self, valor, contaDestino):
        self.saque(valor)
        contaDestino.deposito(valor)

conta = Conta(123,'horge',500,1000)
conta2 = Conta(321,'teo',20,1000)

#referencia.metodo()
print(conta.extrato())

conta.tranferencia(100,conta2)