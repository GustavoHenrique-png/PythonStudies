#Função print
#sep=""(parametro separador no print)
print('Hello World!') 

#Tipagem de dados
#As variaveis em python são dinâmicamente tipadas, ou seja, definida pelo valor guardado na variável
pais = 'Brasil'
type(pais)

#Input recebe dados do usuário
#Todo input recebido é consideraado pelo python como uma string 
#portanto sendo necessário transforma-lo (declarando o tipo desejado) caso preciso
input()

#Estruturas condicionais são de tomadas de decisão pelo pragrama
if condicao:
    print('feito')
elif outraCondicao:
    print('outroFeito')
else:
    print('Não feito')
    
print('texto'if condicao else naoCondicao)

#Estruturas de repetição são usadas quando precisa-se que um bloco de código seja executado mais de uma vez
#for é usado quando se quer iterar sobre um bloco de código um número determinado de vezes
for numeroDeRodadas in range(1,10):
    print('Faça algo')

#while é usado quando queremos que o bloco de código seja repetido até que uma condição seja satifeita
while numeroDeRodadas <= numeroDeTentativas:
    print('Faça algo')

#def é om que sinaliza uma função em python na qual são passados paramentros os quais quais a função usa pra executar operações
def rodadasDaPartida(numeroDeRodadas):
    print(numeroDeRodadas)


#Declaração de uma classe a qual são definidos os atributos do objeto
class jogador(object):
    #__init__ simboliza o método contrutor de uma classe ou seja, determina quais açoes devem ser tomadas dentro da classe
    def __init__(self, identificacao,player):
        self.player = player
        #Colocar __ antes de uma variavel "priva" ela, ocultando a mesma
        self.__identificacao = identificacao
        pass #pass pra indicar que em algum momento eu vou fazer algo aqui

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