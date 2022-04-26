'''
 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
 No final, mostre os 10 primeiros termos dessa progressão.
'''
print('='*46)
print('  Os 10 termos de uma Progressão Aritimética')
print('='*46)
print('\n')

termo = int(input('Digite o termo: '))
razao = int(input('Digite o razão: '))
dec = termo + (10-1) * razao
for n in range (termo, dec + razao, razao):
    print(termo,end=' -> ')
    
    
print('Fim !')  



