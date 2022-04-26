'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                   
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
c = 0
opc = 'S'
while True:
    c += 1
    n = int(input(f'Digite o {c}º número: '))
    n = lista.append(n)
    opc = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    print()
    if opc in 'Nn':
        print()
        print('ENCERRADO')
        print()
        break

print(f'A lista contem {len(lista)} números.')
if 5 in lista:
    print(f'O valor 5 está na lista {lista.count(5)} vez(es). ')
print(f'A lista contem os seguintes valores: {lista}.')
print(f'A lista de forma decrescente é: {sorted(lista)[::-1]}')
