'''
Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''

multiplicador = 1

while multiplicador :
    multiplicador += 1
    n = int(input('Digite o nº da tabuada que deseja: '))
    if n < 0:
        break
        
    for multiplicador in range (1,11):
        print(f'A tabuada do {n} é: {n} x {multiplicador} é: {n*multiplicador}')    
    


print('Número digitado é negativo, o programa sera encerrado!')