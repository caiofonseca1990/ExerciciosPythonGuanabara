#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome por favor: ')).strip()

print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))


