'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
lista = list()
dados = list()
opc = 'SN'

while True:
    dados.append(str(input('Digite seu nome: ').upper()))
    dados.append(float(input('Digite seu peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]            

    lista.append(dados[:]) # armazena dados de 1 lista dentro da outra
    dados.clear() # Limpa a lista de dados para não duplicar os itens
    
    opc = str(input('Deseja continuar? [S/N]: ').upper()).strip()[0]
    print()
    
    if opc in 'Nn':
        break

  
print('Programa encerrado !')
print()
print(f'Temos {len(lista)} pessoas cadastradas na lista.')
print(f'O maior peso foi {maior:.2f}Kg, ',end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}, ',end=' ')
        
print()
print(f'O menor peso foi {menor:.2f}Kg, ',end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}, ',end=' ')
