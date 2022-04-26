'''
Faça um programa que leia um ângulo qualquer, e de em tela o valor do seu
SENO, COSSENO e TANGENTE
'''
from math import hypot, cos, sin, tan,radians
from time import sleep
import os

ang = float(input('Digite o valor do ângulo: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'O Seno do ângulo informado é: {seno:.2f}')
print(f'O Cosseeno do ângulo informado é: {cosseno:.2f}')
print(f'A Tangente do ângulo informado é: {tangente:.2f}')

sleep(10)
os.system('cls')



