'''
Escreva um programa em Python que leia um número inteiro qualquer e peça 
para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''
bi = octa = hexa = 0, 0, 0

n = int(input('Olá querido, tudo bom ?. Digite um número por favor: '))

print('\n[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal\n')
opc = int(input('Agora escolha uma opção: '))


if opc == 1:
    print('O número {} em Binário ficaria: {}'.format(n,bin(n).replace('0b','')))
elif opc == 2:    
    print('O número {} em Octal ficaria: {}'.format(n, oct(n).replace('0c','')))
elif opc == 3:
    print('O número {} em Hexadecimal ficaria: {}'.format(n, hex(n).replace('0x','')))