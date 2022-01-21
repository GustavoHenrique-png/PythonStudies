print(45*'=')
print('=========Seja bem vindo ao meu jogo!=========')
print(45*'=')
print('\n')
print('Temos aqui um número escondido, caso advinhe qual é, avançará para o próximo nível, Boa sorte Jogador!\n')

#Declaração da variável que seta o número resposta
numero = 43

#Declaração da variável que define quantas tentativas ainda restam pro usuário
numeroDeTentativas = 3

#Declaração da variável que define a rodada na qual o usuário está
numeroDeRodadas = 1

#Função que compara as duas variáveis(numero e resposta) e retorna se o usuário acertou ou não
def verificaNum(numero):
    
    for numeroDeRodadas in range(1,numeroDeTentativas+1):
        #Exibição de rodadas para situar o usuário
        print('\nRodada {} de {}\n'.format (numeroDeRodadas,numeroDeTentativas))

        #Input que recebe a reposta do usuário
        resposta = int(input('Chute um número:\n'))

        #condições que checam a vitória ou derrota do usuário
        if numero == resposta:
            print('Parabéns, aperte enter para avançar ao próximo nível\n')
            break
            
        elif numero > resposta:
            print('Tente chutar um pouco mais alto\n')
        elif numero < resposta:
            print('tente chutar um pouco mais baixo\n')


#Laço que permite novas tentativas
# while numeroDeRodadas <= numeroDeTentativas:

#     #Chamada da função que verifica o número digitado
#     verificaNum(numero)

#     #Decremeto do número de tentativas
#     #numeroDeTentativas -= 1

#     #Acréscimo do número de rodadas
#     numeroDeRodadas += 1
