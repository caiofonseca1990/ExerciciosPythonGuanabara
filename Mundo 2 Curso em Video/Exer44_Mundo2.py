'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

import cmath
from time import sleep

n = 11
for c in range (0,n):
    c+=1
    c = n - c 
    sleep(1)
    print(c)

sleep(1)    
print('FELIZ ANO NOVOOO PUM PUIM PUM')
