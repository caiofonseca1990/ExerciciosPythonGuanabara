'''
Crie um algoritimo que leia as notas de um aluno, 
calculo e exiba a sua média
'''

n1 = n2 = n3 = n4 = 0

n1 = float(input('Digite a 1º nota por favor: '))
n2 = float(input('Digite a 2º nota por favor: '))
n3 = float(input('Digite a 3º nota por favor: '))
n4 = float(input('Digite a 4º nota por favor: '))

media = (n1+n2+n3+n4) /4
# a barra invertida "\" no fim da primeira linha do print após ao "1ºnota: {:.2f}", faz uma quebra automatica possibilitando a identação
#com uma melhor visualização ao código, é permitido

print('As notas inseridas foram \n1ºnota: {:.2f}\
    \n2ºnota: {:.2f}\n3ºnota: {:.2f}\n4ºnota: {:.2f}\nA média do aluno é: {:.2f}'.format(n1,n2,n3,n4,media))