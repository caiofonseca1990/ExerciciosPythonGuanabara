#Crie um programa que calcule descontos baseado no desconto de 5%

produto = float(input('Informe o valor do produto R$:'))

taxa = produto * 0.05
desconto = produto - taxa

print('O produto inserido no valor de R$:{:.2f} reais.\nNa promoção sai por\
 R$:{:.2f} reais.\nO desconto foi de R$:{:.2f} reais'.format(produto,desconto,taxa))