'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date, datetime

contmaior = 0
contmenor = 0
for c in range (0,7):
    c+=1
    ano = int(input('Digite o ano de nascimento da {}ª pessoa por favor: '.format(c)))
    
    hoje = datetime.today().year
    maior = hoje - ano
    
    if maior >= 18:
         contmaior += 1
    
    elif maior < 18:
        contmenor += 1


print('Temos {} MENORES de idade e temos {} MAIORES de idade !'.format(contmenor,contmaior))