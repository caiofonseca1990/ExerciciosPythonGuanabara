'''Escreva um programa que leia a velocidade de um carro.
   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
   A multa vai custar R$7,00 por cada Km acima do limite.
'''

from time import sleep
import os

percorrido = float(input('Olá senhor, quantos KM você percorreu?: '))
sleep(2)
print('Calculando...')
sleep(3)

pagar = (percorrido - 80) *7

if percorrido > 80:
    print('Infelizmente o senhor será multado, ultrapassou o limite de 80-KMh!!')
    sleep(1)
    print('A multa será de R$:7,00 reais por KM ultrapassado')
    sleep(2)
    print('O senhor ira pagar o valor de R$:{:.2f} reais'.format(pagar))
else:
    print('Parabéns senhor, continue com prudência!! ')

   
sleep(10)
os.system('cls')