'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.

'''
from random import randint

print('-='*20)
print('           Jogo da adivinhação !')
print('-='*20)
print('\n')

tentativa = 0
vitoria = False
computador = randint(0,10)
chute = int(input('Digite um número para tentar adivinhar: '))

while not vitoria:
    tentativa += 1
    print('Ops, não é o certo, vamos denovo...{}ª tentativa. '.format(tentativa))
    chute = int(input('Chute mais uma vez: '))
    if chute == computador:
        tentativa += 1
        vitoria = True
        print('Seu número foi {}'.format(chute))
        print('Você acertou o jogo com {} tentativas, o número sorteado foi {}.'.format(tentativa, computador))

print('Acertou')