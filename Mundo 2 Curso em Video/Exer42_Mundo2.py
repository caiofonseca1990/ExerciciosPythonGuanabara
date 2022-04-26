'''
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal 
– 3x ou mais no cartão: 20% de juros
'''
print('-*'*15)
print('Bem vindo a loja!!')
print('-*'*15)
print('\n')

valor = float(input('Qual valor do produto que você comprou?: '))

print('[1] - A vista no dinheiro / Cheque. ( +10% Off ) ')
print('[2] - A vista no cartão . ( +5% Off )')
print('[3] - A vista ou Cheque. ( Sem desconto )')
print('[4] - A vista ou Cheque. ( +10% De Juros )')
print('\n')
opc = int(input(('Escolha uma opção de pagamento: ')))

print('\n')

dinheiro = valor - (valor* 10 / 100)
cartao = valor - (valor * 5/100)
juros = valor * 20/100

if opc == 1:
    print('O valor a pagar foi de R$:{:.2f} reais, o desconto foi de R$:{:.2f} reais, total de 10%. '.format(dinheiro, valor - dinheiro))
elif opc == 2:
    print('O valor a pagar foi de R$:{:.2f} reais, o desconto foi de R$:{:.2f} reais, total de 5%. '.format(cartao, valor  - cartao ))
elif opc == 3:
    print('O valor a pagar foi de R$:{:.2f} reais. '.format(valor))
elif opc == 4:
    print('O valor a pagar foi de R$:{:.2f} reais, com acréscimo foi para R$:{:.2f} reais, total de 20%. '.format(valor, valor  + juros ))