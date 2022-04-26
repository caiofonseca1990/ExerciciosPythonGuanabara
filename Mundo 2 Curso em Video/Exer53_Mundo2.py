'''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
'''
menor = maior = 0,0
for c in range(0,5):
    c += 1
    peso = float(input('Por favor, digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso    

print(' O MAIOR peso é {} e o MENOR peso é {}'.format(maior, menor))