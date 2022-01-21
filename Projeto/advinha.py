print(45*'=')
print('=========Seja bem vindo ao meu jogo!=========')
print(45*'=')
print('\n')
print('Temos aqui um número escondido, caso advinhe qual é, avançará para o próximo nível, Boa sorte Jogador!\n')

#Declaração da variável que seta o número resposta
numero = 43

#Declaração da variável que define quantas tentativas ainda restam pro usuário
numeroDeTentativas = 3

#Função que compara as duas variáveis(numero e resposta) e retorna se o usuário acertou ou não
def verificaNum(numero):

    #Input que recebe a reposta do usuário
    resposta = int(input('Chute um número:\n'))
    
    if numero == resposta:
        print('Parabéns, aperte enter para avançar ao próximo nível\n')
    elif numero > resposta:
        print('Tente chutar um pouco mais alto\n')
    elif numero < resposta:
         print('tente chutar um pouco mais baixo\n')

#Laço que permite novas tentativas
while numeroDeTentativas > 0:
    #Chamada da função que verifica o número digitado
    verificaNum(numero)
    numeroDeTentativas -= 1

    if numeroDeTentativas == 0:
        print('Tente novamente mais tarde')
