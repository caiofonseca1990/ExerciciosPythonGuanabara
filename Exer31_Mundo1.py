'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
n1 = int(input('Digite o 1º número por favor: '))
n2 = int(input('Digite o 2º número por favor: '))
n3 = int(input('Digite o 3º número por favor: '))

menor = maior = n1

if n2 < menor and  n2 <n3:
    menor = n2
if n3  < menor and n3 < n1:
    menor = n3    
if n2  > maior and n2 > n3:
    maior = n2
if n3  > maior and n3 > n1:
    maior = n3

print('O número maior é {} e o menor é {}'.format(maior, menor))    
