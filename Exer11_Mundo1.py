#Crie um programa que leia o salário de um funcionário e mostre seu novo salario com aumento de 15%

salario = float(input('Qual o seu salário por favor? \nR$: '))

taxa = salario * 0.15
acres =  taxa + salario

print('O salário do funcionário é R$:{:.2f} reais.\nO aumento de 15%, totaliza R$:{:.2f} reais.\n\
O aumento foi de R$:{:.2f} reais.'.format(salario, acres, taxa))