'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e 
todas as informações possiveis sobre ele
'''
algo = input('Digite algo para exibir na tela: ')
print('A frase tem espaços? =', algo.isspace())
print('Qual tipo do input? =', type(algo))
print('Quantos caracteres tem o input? =', len(algo.strip()))
print('É maiusculo? =', algo.isupper())
print('É minusculo? =', algo.islower())
print('Esta capitalizada? =', algo.istitle())
print('É número? =' ,algo.isnumeric())
print('É texto? =' ,algo.isalpha())
