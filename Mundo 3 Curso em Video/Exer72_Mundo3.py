'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique 
o MENOR e o MAIOR valor que estão na tupla.
'''
from random import randint

numero = (randint(1,20), randint(1,20),randint(1,20),randint(1,20),randint(1,20))

print(f'Os números sorteados foram: {numero}')
print(f'Os números sorteados em ordem é: {sorted(numero)}')
print(f'O MENOR número da lista é: {min(numero)}')
print(f'Os MAIOR número da lista é: {max(numero)}')






