'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

print('=-'*15)
print('      VALIDANDO VALORES')
print('=-'*15)
print('\n')

print('Somente valores M ou F por favor')

sexo = str(input('Digite seu sexo por favor: ')).upper().strip()[0] #Fatiando somente a primeira posição da string
while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo de forma CORRETA por favor, somente M ou F: ')).upper()

print('Sexo digitado com sucesso !!')