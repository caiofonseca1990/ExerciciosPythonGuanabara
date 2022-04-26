'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do  comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
from time import sleep
import os

print('-_-'*13)
print('Bem vindo ao projeto Minha Casa')
print('-_-'*13)

casa = float(input('Qual valor do imovél? R$: '))
salario = float(input('Qual a renda? R$: '))
tempo = int(input('Em quanto tempo pretende pagar o imóvel?: '))

mensalidade = casa / (tempo * 12)
minimo = salario * 30 / 100
if mensalidade <= minimo:
    print('Sua renda é de R$:{:.2f} reais mensais.'.format(salario))
    print('Seu imóvel sera financiado em {} anos.'.format(tempo))
    print('Sua mensalidade sera de R$:{:.2f} reais em {} parcelas'.format(mensalidade, tempo * 12))
    print('O seu financeiamento foi APROVADO!!')
else:
    print('Infelizmente a mensalidade ultrapassa os requisitos para financiamento.')
    print('O seu financeiamento foi NÃO FOI APROVADO!!')
    


sleep(15)
os.system('cls') 


