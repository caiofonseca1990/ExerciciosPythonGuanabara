'''
Crie um programa que converta a quantidade de valor que ele tem em carteira, 
considerando a cotação do dolar atual 18/01/2022  R$:5,53 
'''
carteira = float(input('Quanto você tem em carteira?: ').replace('.',','))

dolar = 5.52
convertido = carteira / dolar

print('O senhor tem R${:.2f} em carteira e pode comprar US${:.2f}'.format(carteira, convertido).replace('.',','))


