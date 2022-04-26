# Crie um programa que leia o nome completo de uma pessoa e exiba:
# 1 Nome com todas as letras maísculas
# 2 Nome com todas as letras minusculas
# 3 Quantas letras tem sem considerar espaços?
# 4 Quantas letras tem o primeiro nome?
import os
from time import sleep

nome = str(input('Digite seu nome por favor:'))

print('Seu nome em maísculo fica: {} '.format(nome.upper()))
print('Seu nome em mínusculo fica: {}'.format(nome.lower()))
print('Seu nome em tem {} letras sem os espaços: '.format(len(nome.replace(' ',''))))
novonome = nome.split()
print('Seu 1º nome tem {} letras: '.format(len(novonome[0])))

sleep(10)
os.system('cls')
