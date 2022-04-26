'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''

lista = []
opc ='S'

while opc in 'Ss':
    n = int(input('Digite o valor: '))
    if n not in  lista:
        lista.append(n)
        print('Valor adcionado !')
    else:
        print('Valor duplicado, não vou adcionar !')
    opc = str(input('DEseja continuar? [S / N]').upper().strip()[0])


lista.sort()
print(lista)    



