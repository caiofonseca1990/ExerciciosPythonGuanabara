#Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi 
#alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
# R$0,15 por Km rodado.

km = float(input('Quantos KM foram percorridos com o veículo?:  '))
dias = int(input('Por quantos dias o veículo foi alugad?:  '))

kmv = km * 0.15
diasv = dias * 60

print('\nVocê irá pagar um total de R$:{:.2f} reais.'.format(kmv+diasv))
print('Referente a {} dias alugados, e {:.2f} KM rodados\n'.format(dias, km))

