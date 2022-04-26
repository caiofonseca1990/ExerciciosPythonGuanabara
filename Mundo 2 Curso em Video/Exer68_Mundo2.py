'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

contador = contamil = soma = 0
opc = ' '

while True:
    produto = str(input('Qual o nome do produto?: ').upper())
    valor = float(input('Qual o valor do produto? R$: '))
    soma += valor
    opc  = str(input('Deseja continuar? SIM ou NAO [S/N]: ').upper())
    print()
    contador += 1
    if valor > 1000:
        contamil += 1

    if contador == 1:
        menor = valor    
    else:
        if valor < menor:
            menor = valor      

    while opc not in 'SN':
        opc  = str(input('Digite novamente, somente SIM ou NAO [S/N]: ').upper())
        print()
    if opc in 'N':
        break
    
  
print(f'A soma das compras é R$: {soma:.2f}.')
print(f'Ao todo foram comprados {contador} produtos.')
print(f'Foram comprados {contamil} produto(s) acima de R$:1000,00 reais')
print(f'O menor valor R$: {menor:.2f}, produto {produto} ')
print('-='*40)
print('                  FIM DO PROGRAMA ! ')
print('-='*40)