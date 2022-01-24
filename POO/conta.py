#Criação da classe
class Conta(object):
    #Contrutor do objeto
    #Self é a referência na memória onde o objeto está
    def __init__(self):
        #Acessando atributo numero do objeto
        # Uso de 2 underlines para 'privar a variavel' ocultando ela de outras classes 
        self.__numero = 123
        self.nome = 'Jorge'
        self.saldo = 500
        sel.limite = 1000
