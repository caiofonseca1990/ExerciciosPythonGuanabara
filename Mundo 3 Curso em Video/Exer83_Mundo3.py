'''
Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista = [[],[]]
dados = 0

for c in range(0,7):
    c += 1
    dados = (int(input(f'Digite o {c}º número: ')))
    if dados  % 2 == 0:
        lista[0].append(dados)        
    else:
        lista[1].append(dados)

print(f'Os pares são: {sorted(lista[0])},\nOs impares são: {sorted(lista[1])}')
