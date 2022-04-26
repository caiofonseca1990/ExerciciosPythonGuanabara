'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
par = []
impar = []
c = 0
opc = 'S'
while True:
    c += 1
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        n = par.append(n)
    else:
        n = impar.append(n)

    opc = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
    if opc not in 'SsNn':
        opc = str(input('Digite somente SIM ou NÃO... [S/N]: ').upper().strip()[0])
    elif opc in 'Nn':
        break

print(' ACABOU ! ')
print(f'A lista inteira é: {sorted(par+impar)}')
print(f'A lista par é: {sorted(par)}.')
print(f'A lista impar é: {sorted(impar)}.')