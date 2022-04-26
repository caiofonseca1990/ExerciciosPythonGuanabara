'''
 Desenvolva um programa que leia seis números inteiros 
 e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
print('Bem vindo ao SOMANDO SOMENTE PARES !')
print('O programa consiste em ler 6 númeiros inteiros e fazer a soma dos PARES:')
print('Vamos começar?')
print('\n')
contapar = 0
somapar = 0
for c in range (0,6):
    n = int(input('Digite o {}º número por favor: '.format(c+1)))
    c += 1
    if n % 2 == 0:
        par = n
        somapar += par
        contapar = contapar +1
        
               
print('Tivemos {} números pares e a soma de todos é {}'.format(contapar, somapar))
    
    

