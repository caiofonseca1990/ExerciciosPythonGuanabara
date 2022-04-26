'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint, choices
from time import sleep


vitoria = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0,10)
    soma = n + pc
    escolha =' '
    while escolha not in 'PI':
        escolha = str(input('Escolha PAR ou IMPAR [P/I]: ').strip()).upper() [0]
    print(f'O JOGADOR escolheu o número: {n}..., a MÁQUINA escolheu {pc}, a soma é : {soma}') # cont. do primeiro laço hile 
    if escolha == 'P':
        if soma % 2 == 0:
            print(' PARABÈNS !!!! VENCEU !!!')
            print('-*'*20)
            vitoria += 1
        else:
            print(' PERDEU PARA O COMPUTADOR =(')
            print('-*'*20)
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print(' PARABÈNS !!!! VENCEU !!!')
            print('-*'*20)
            vitoria += 1
        else:
            print(' PERDEU PARA O COMPUTADOR =(')
            break
    print('Vamos denovo?')


print(f'JOGO encerrado, você venceu {vitoria} vezes')    

        
