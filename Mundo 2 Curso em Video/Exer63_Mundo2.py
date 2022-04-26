'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
from time import sleep
import os

contador = n = soma = 0
n = int(input('Digite o número, [999] para encerrar: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite o número, [999] para encerrar: '))
    #if n == 999:
     #   soma = soma - 999
        
print('vc digitou: {} números até agora, a soma total é: {} '.format(contador,soma,end=' '))
print('Programa encerrado !!')
sleep(5)
os.system('cls')