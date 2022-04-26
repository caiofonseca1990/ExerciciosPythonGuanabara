'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
   qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from itertools import count
import os
from random import randint, randint
from time import sleep

print('=_=_'*5)
print('   Vamos jogar ?')
print('=_=_'*5)
sleep(2)

print('Irei pensar em um número entre 0 e 10 e você terá que adivinhar, He He He!')

sleep(2)

sorteado = randint(0,10)

n = int(input('Digite o número que eu pensei: '))

if n == sorteado:
    sleep(2)
    print('O número que eu pensei foi exatamente este "{}", COMO VOCÊ ACERTOU???'.format(n))
else:
    sleep(2)
    print('Não foi dessa vez, ADEUS!! ')

print('O número sorteado foi {}'.format(sorteado))

sleep(5)
os.system('cls')

    