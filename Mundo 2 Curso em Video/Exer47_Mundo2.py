'''
Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for.
'''
n = int(input('Digite um número para ver a tabuada do mesmo: '))

for c in range (0,10):
    c+=1
    taboada = n*c
    print('A taboada do {}x{} é: {}'.format(n, c, taboada))


