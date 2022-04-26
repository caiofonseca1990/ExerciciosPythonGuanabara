'''
Faça um programa que calcule a soma entre todos os números 
que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
soma = 0
csoma = 0

for c in range (1,501,2):
    if c % 3 ==0:
        soma +=c
        csoma +=1
        c+=1
               
    
print('São ao todo {} valores multiplos de 3, e a soma de todos é {}.'.format(csoma, soma))