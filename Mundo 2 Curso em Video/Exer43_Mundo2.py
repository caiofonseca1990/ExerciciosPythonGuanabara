#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

armas = ('Pedra', 'Papel','Tesoura')
comp = randint(0,2)

print('[0] - Pedra')
print('[1] - Papel')
print('[2] - Tesoura')
player = int(input('Digite qual arma ira usar: '))
print('-='*20)
print('A MÀQUINA escolheu: {}'.format(armas[comp]))
print('O JOGADOR escolheu: {}'.format(armas[player]))
print('-='*20)

if comp == 0: #Comp escolhe PEDRA
    if player == 0: #Jogador escolhe PEDRA
        print('Deu EMPATE !')
    elif player == 1: #Jogador escolhe PAPEL
        print('O jogador VENCEU !')
    elif player == 2: #Jogador escolhe TESOURA
        print('O computador VENCEU !')   
    else:
        print('VALIORES somente entre 0 e 2')    

elif comp == 1: #Comp escolhe PAPEL
    if player == 0: #Jogador escolhe PEDRA
        print('o computador VENCEU !')
    elif player == 1: #Jogador escolhe PAPEL
        print('Deu EMPATE !')
    elif player == 2: #Jogador escolhe TESOURA
        print('O jogador VENCEU !')   
    else:
        print('VALIORES somente entre 0 e 2')   

elif comp == 2: #Comp escolhe TESOURA   
    if player == 0: #Jogador escolhe PEDRA
        print('o jogador VENCEU !')
    elif player == 1: #Jogador escolhe PEDRA
        print('O computador VENCEU !')
    elif player == 2: #Jogador escolhe TESOURA
        print('Deu EMPATE !')   
    else:
        print('VALIORES somente entre 0 e 2')    

