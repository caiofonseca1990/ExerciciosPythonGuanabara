'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from time import sleep
import os

n = int(input('Digite o ano por favor: '))

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano é Bissexto')

else:
    print('O ano não é Bissexto')    
    
sleep(4)
os.system('cls')