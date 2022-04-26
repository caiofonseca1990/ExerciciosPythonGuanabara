'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
km = float(input('Qual distância que você ira percorrer?: '))

if km <=200:
    preço = km * 0.50
    print('O valor a ser cobrado para esta viagem de {} KHh é de R$:{:.2f} reais'.format(km,preço))
else:
    preço = km * 0.45  
    print('O valor a ser cobrado para esta viagem de {} KHh é de R$:{:.2f} reais'.format(km,preço))