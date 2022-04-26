'''
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

n = media = soma = contador = 0
parar = 'N'

while parar in 'Nn':
    n = float(input('Digite o número: '))
    soma += n
    contador +=1
    parar = str(input('Deseja parar? [S - Sim / N - Não]: ').upper().strip()[0])
    
    if contador == 1:
        menor = maior = n

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

media = soma / contador
print('Você digitou: {:.0f} números'.format(contador))  
print('A soma é: {:.0f}.'.format(soma))
print('A média é: {:.1f}, dividido por: {:.0f} números.'.format(media, contador))
print('O maior é: {}, e o menor é {}'.format(maior, menor))



