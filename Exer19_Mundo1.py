#Faça um programa que leia os 4 alunos e mostre a ordem sorteada.
from dataclasses import replace
from time import sleep
import os
from random import choice, choices, random, shuffle

aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))

#Criado uma lista para armazenar as variaveis para sorteio
lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print('Os alunos que irão apresentar o trabalho na ordem são: {}'.format(lista))











sleep(10)
os.system('cls')

#print('O aluno sorteado para limpar o quadro foi: ',choice(aluno1, aluno2, aluno3, aluno4))



