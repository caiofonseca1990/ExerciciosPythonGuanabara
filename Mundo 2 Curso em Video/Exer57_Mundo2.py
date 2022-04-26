'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
#Menu de opções
print('''Escolha umas das opções abaixo:
    [1] - Somar.
    [2] - Multiplicarr.
    [3] - Maior.
    [4] - Novos números.
    [5] - Sair. ''')
   
escolha = 0
while escolha != 5: # Loop onde indica que enquanto não for digitado a opção 5,
                    # fará todos os comandos 

    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1: # Soma
        soma = n1 + n2
        print(soma)
        print('='*40)

    elif escolha == 2: # Multisplica
        mult = n1 * n2
        print(mult)
        print('='*40)

    elif escolha == 3: # Exibe maior
        if n1 > n2:
            print(' O maior é o {}.'.format(n1))
            print('='*40)
        else:
            if n2 > n1: # Exibe maior
                print(' O maior é o {}.'.format(n2))
                print('='*40)

    elif escolha == 4: # Digita novamente os valores de n1 e n2
        print('Digite novos números')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        print('='*40)
    

print('Acabou o programa !') # Ao digitar 5 ele encerra o programa