'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite o 1º número por favor: '))
n2 = int(input('Digite o 2º número por favor: '))


menor = maior = n1

if n2 > n1:
    maior = n2
    print('O 2º valor: {} é o MAIOR, o 1º valor é: {}.'.format(maior, n1))
elif n1 > n2:
    maior = n1
    print('O 1º valor {} é o MAIOR,  o 2º valor é: {}'.format(maior,n2))
#elif menor == maior:
 #   print(' Os 2 valores são iguais, {} e {}.'.format(menor, maior))    
else:
    print('Não existe valor maior, os dois são iguais')