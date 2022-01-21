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

