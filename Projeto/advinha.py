from webbrowser import Elinks


print(45*'=')
print('=========Seja bem vindo ao meu jogo!=========')
print(45*'=')
print('\n')
print('Temos aqui um número escondido, caso advinhe qual é, avançará para o próximo nível, Boa sorte Jogador!\n')

#Declaração da variável que seta o número resposta
numero = 43

#Input que recebe a reposta do usuário
resposta = int(input('Chute um número:\n'))

#Função que compara as duas variáveis(numero e resposta) e retorna se o usuário acertou ou não
def verificaNum(resposta,numero):
    if numero == resposta:
        print('Parabén, aperte enter para avançar ao próximo nível\n')
    else:
        print('Tente...um outro valor\n')

#Chamada da função que verifica as respostas
verificaNum(resposta,numero)
    
