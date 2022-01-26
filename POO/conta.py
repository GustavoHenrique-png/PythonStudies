#Criação da classe
class Conta(object):
    #Contrutor do objeto
    #Self é a referência na memória onde o objeto está
    def __init__(self, numero, nome, saldo,limite):
        #Acessando atributo numero do objeto
        # Uso de 2 underlines para 'privar a variavel' ocultando ela de outras classes 
        self.numero = numero
        self.nome = nome
        self.saldo = 500
        self.limite = 1000
