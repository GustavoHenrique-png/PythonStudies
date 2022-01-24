import advinha
print('Escolha o jogo desejado!')
print('(1)Forca (2)Advinha')

jogo = int(input('Escolha um jogo:'))

if jogo == 1:
    print('Joog forca')
elif jogo == 2:
    advinha.verificaNum()

