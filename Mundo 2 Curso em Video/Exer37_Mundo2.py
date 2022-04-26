'''
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date


hoje = 2021

print('-='*40)
#nome = str(input('Bem vindo ao Serviço de alistamento militar Sr, qual seu nome?: '))
#print('Vamos iniciar o alistamento Sr.{}.'.format(nome))
print('-='*40)
print('\n')
ano = int(input('Em que ano você nasceu,  por favor?: '))

hoje = date.today().year
idade = hoje - ano

if idade > 18:
    print('Sua idade é {} anos, e você está atrasado para se alistar em {} anos.'.format(idade, idade -18))
elif idade == 18:
    print('Sua idade é {} anos, e você está no momento certo  para se alistar, seu ano é {}.'.format(idade, hoje))
elif idade <18:
    print('Sua idade é {} anos, e ainda falta {} ano(s) para seu alistamento.'.format(idade, 18-idade))    