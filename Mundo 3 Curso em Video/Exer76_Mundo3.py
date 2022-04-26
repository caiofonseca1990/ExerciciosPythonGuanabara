'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista.
'''
menor = maior = 0

lista = []
for c in range (0,5):
    lista.append(int(input('Digite o {} número: '.format(c+1))))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('\n')
print('O MAIOR digitado foi: {} nas posições: '.format(maior),end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ',end='')
print()
print('O MENOR digitado foi: {} nas posições: '.format(menor),end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')

print()
print('Os valores digitados foram: {}'.format(lista))
lista.sort()
print('Os valores digitados em ORDEM é: {}'.format(lista))