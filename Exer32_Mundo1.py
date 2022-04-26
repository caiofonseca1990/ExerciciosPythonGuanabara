'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
'''
from time import sleep
import os

salario = float(input('Digite o salário por favor R$:'))
sleep(1)
if salario <= 1250:
    aumento = salario*0.15
    print('O séu aumento foi de 15%, somando R$: {:.2f} reais ao seu salário.'.format(aumento))
    print('Seu salário final é de R$:{:.2f} reais.'.format(salario+aumento))
else:
    aumento=salario*0.10
    print('O séu aumento foi de 10%, somando R$: {:.2f} reais ao seu salário.'.format(aumento))
    print('Seu salário final é de R$:{:.2f} reais.'.format(salario+aumento))


sleep(10)
os.system('cls')