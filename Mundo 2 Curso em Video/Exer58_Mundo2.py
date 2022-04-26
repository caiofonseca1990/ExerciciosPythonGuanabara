'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
n = int(input('Digite um número para calcular o Fatorial: '))
fatorial = 1
contador = n

while contador > 0:
    
    print(contador,end='')
    print(' x ' if contador > 1 else ' = ', end=' ')
    fatorial *= contador
    contador -= 1
    
    

print('O fatorial de {} é {}'.format(n, fatorial))


