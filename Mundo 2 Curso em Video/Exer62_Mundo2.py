'''
Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
'''
from operator import contains
from time import sleep
import os
from turtle import end_fill

n = int(input('Quantos termos ira exibir?: '))

n1 = 0
n2 = 1
print('{} -> {}'.format(n1,n2), end='')
contador = 3
while contador <= n:
    n3 = n1 + n2
    print(' -> {}'.format(n3),end='')
    n1 = n2
    n2 = n3
    contador += 1
  

print(' -> Fim !')

sleep(20)
os.system('cls')