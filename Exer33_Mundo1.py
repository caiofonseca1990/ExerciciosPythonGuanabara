'''
Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.
'''
from time import sleep
import os

l1 = float(input('Digite o valor do 1º lado do triângulo: '))
l2 = float(input('Digite o valor do 2º lado do triângulo: '))
l3 = float(input('Digite o valor do 3º lado do triângulo: '))

if l1 <  l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores FORMAM um TRIÂNGULO')
else:
    print('Os valores NÃO FORMAM um TRIÂNGULO')    


sleep(7)
os.system('cls')    
