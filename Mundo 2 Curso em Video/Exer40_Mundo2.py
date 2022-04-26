'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''


from cmath import log10



l1 = int(input('Digite o valor do 1º lado: '))
l2 = int(input('Digite o valor do 1º lado: '))
l3 = int(input('Digite o valor do 1º lado: '))


if l1 <  l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores FORMAM um TRIÂNGULO')
    if l1 == l2 == l3:
        print('Forma um triangulo EQUILÀTERO')
    if (l1 != l2 and l1 == l3) or (l2 != l3 and l2 == l1) or (l3 != l1 and l3 == l2):
        print('Forma um triangulo ISÓSCELES')    
    if (l1 != l2 and l1 != l3) or (l2 != l1 and l2 != l3) or (l3 != l1 and l3 != l2):
        print('Forma um triangulo ESCALENO')     
else:
    print('Os valores NÃO FORMAM um TRIÂNGULO') 


