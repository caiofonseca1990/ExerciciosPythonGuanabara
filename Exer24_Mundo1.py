#Crie um programa que leia uma frase e mostre
'''
1 - Quantas vezes aparece a letra "A"
2 - Em que posição ela aparece pela primeira vez
3 - Em que posição aparece a ultima vez

'''
import os
from time import sleep

frase = str(input('Digite uma frase qualquer: ')).strip().upper()

print('A letra "A" aparece: {} vez(es) na frase'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')))

sleep(3)
os.system('cls')
