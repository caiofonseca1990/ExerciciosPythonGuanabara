'''
 Crie um programa que leia duas notas de um aluno e calcule sua média, 
 mostrando uma mensagem no final, de acordo com a média atingida
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))

med = (n1 + n2) / 2

if med < 5.0:
    print('O aluno tem a média de {:.1f} e está REPROVADO.'.format(med))
elif med >= 5.0 and med  <7.0:
    print('O aluno tem a média de {:.1f} e está de RECUPERAÇÂO.'.format(med))
elif med >= 7.0:
    print('O aluno tem a média de {:.1f} e está APROVADO.'.format(med))    