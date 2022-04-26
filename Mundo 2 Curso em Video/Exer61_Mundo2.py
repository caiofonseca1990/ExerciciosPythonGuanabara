'''
Melhore o DESAFIO 60, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

termo = int(input('Diigite o termo: '))
razao = int(input('Diigite a razao: '))
maistermos = 0
contador = 1
maistermos = 10
total = 0
while maistermos != 0:
    total += maistermos
    if maistermos == 0: #Condição para encerrar o programa
        exit
    
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('Aguardando mais termos ...')    
    maistermos = int(input('Quanos termos você quer colocar?: '))
    print('Aperte 0 ( ZERO ) para encerrar o programa! ')

    
print('\n')
print('Programa encerrado! ')
