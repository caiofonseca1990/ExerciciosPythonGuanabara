'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.

'''

lista = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
          'doze','treze', 'quatorze', 'quinze', 'dezesseis','dezessete','dezoito','dezevone','vinte')
n = 0
while n in range (0,21):
 
    n = int(input('Digite um número entre 0 e 20: '))
    print(f'O nº:{n} por extenso é {lista[n].upper()}')
    print()



