'''
Refaça o DESAFIO 49, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''


termo = int(input('Diigite o termo: '))
razao = int(input('Diigite a razao: '))
contador = 1

while contador <= 10:
    
    print('{} -> '.format(termo),end='')
    termo += razao
    contador +=1
 

print(' Fim !')   