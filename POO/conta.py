#Criação da classe
from mailbox import NotEmptyError


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

    #Getter(metodo que pega o limite)
    #Sempre tem um return e nunca altera nada, recebe como paramentro apenas o self
    def getLimite(self):
        return self.__limite

    #Setter(metodo que define o nome)
    #Altera o valor de um atributo em questão
    def setLimite(self,__limite):
        self.__limite = __limite
    
    #@property, define uma propiedade em python(executa um metodo sem usar os parenteses)
    #substitui os getters?
    @property
    def nome(self):
        return self.__nome
    
    #Define que esse metodo será o setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    #conta.nome = 'Matheus'

#Chamando a função que cria a conta
conta = Conta(123,'horge',500,1000)
conta2 = Conta(321,'teo',20,1000)

#referencia.metodo()
print(conta.extrato())

conta.tranferencia(100,conta2)
conta.getNome()