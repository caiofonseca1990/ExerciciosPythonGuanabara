#Crie um programa que leia o comprimento do cateto oposto e do adjacente
# de um triangulo retângulo e calcule a area da hipotenusa.


import math
from time import sleep
import os

catO = int(input('Digite o valor do CATETO OPOSTO: '))
catA = int(input('Digite o valor do CATETO ADJACENTE: '))

print('\nTemos como Cateto Oposto o valor de: {}, e como Cateto Adjacente o valor de: {}'.format(catO,catA))
print('A Hipotenusa dos catetos digitados são:',math.hypot(catO,catA))

sleep(10)
os.system('cls')


#ou podemos fazer da seguinte forma tradicional
'''
catO = float(input('Digite o primeiro valor: '))
catA = float(input('Digite o segundo valor: '))

#calculando a soma dos catetos

re =  (catO**2) + (catA**2)
#calculando a hipotenusa

hip = re**0.5

print('A Hipotenusa é: 'hip)'''