#Sortear um dos 4 alunos
from time import sleep
import os
from random import choice

aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))

#Criado uma tupla para armazenar as variaveis para sorteio
lista = (aluno1, aluno2, aluno3, aluno4)

print('O aluno escolhido foi {}'.format(choice(lista).upper()))

sleep(10)
os.system('cls')

#print('O aluno sorteado para limpar o quadro foi: ',choice(aluno1, aluno2, aluno3, aluno4))

