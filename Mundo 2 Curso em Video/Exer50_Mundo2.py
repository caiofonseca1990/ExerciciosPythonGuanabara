'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

print('='*30)
print('  Descobrindo Número Primo')
print('='*30)
n = int(input('Digite um número por favor: '))

cont=0

for c in range (1,n+1):
    if n % c == 0:
        print('\033[35m',end='')
        cont += 1
    else:
        print('\033[31m',end='')

    print(c,end=' ')

print('\n')
print('O número {} foi divisivel {} vezes.'.format(n, cont))
    