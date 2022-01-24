import random

#Função que compara as duas variáveis(numero e resposta) e retorna se o usuário acertou ou não
def verificaNum():
    print(45*'=')
    print('=========Seja bem vindo ao meu jogo!=========')
    print(45*'=')
    print('\n')
    print('Temos aqui um número escondido, caso advinhe qual é, avançará para o próximo nível, Boa sorte Jogador!\n')

    #Declaração da variável que seta o número resposta
    #numero = 43

    #Declaração da variavável que seta o numero aleatóriamente
    numero = random.randint(1,50)

    #Declaração da variável que define quantas tentativas ainda restam pro usuário
    numeroDeTentativas = 3

    #Declaração da variável a qual define o número de pontos
    pontos = 100
    
    for numeroDeRodadas in range(1,numeroDeTentativas+1):
        #Exibição de rodadas para situar o usuário
        print('\nRodada {} de {}\n'.format (numeroDeRodadas,numeroDeTentativas))

        #Input que recebe a reposta do usuário
        resposta = int(input('Chute um número:\n'))

        #condições que checam a vitória ou derrota do usuário
        if numero == resposta:
            print('Parabéns, Acertaste! fez {} pontos\n'.format(pontos))
            break
            
        elif numero > resposta:
            print('Tente chutar um pouco mais alto\n')
        elif numero < resposta:
            print('tente chutar um pouco mais baixo\n')
    
    #Conta de número perdidos
    pontosPerdidos = abs(numero - resposta)
    pontos -= pontosPerdidos 


#Chama da função
if(__name__ == '__main__'):
    verificaNum()


#Laço que permite novas tentativas
# while numeroDeRodadas <= numeroDeTentativas:

#     #Chamada da função que verifica o número digitado
#     verificaNum(numero)

#     #Decremeto do número de tentativas
#     #numeroDeTentativas -= 1

#     #Acréscimo do número de rodadas
#     numeroDeRodadas += 1
