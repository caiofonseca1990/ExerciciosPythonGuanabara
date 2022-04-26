'''
 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []
contador = 0
for c in range(0,5):
    contador += 1
    n = int(input('Digite o {}º valor: '.format(contador)))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                break
            p += 1    
                

print(lista)