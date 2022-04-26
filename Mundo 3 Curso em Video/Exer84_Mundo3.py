'''
 Crie um programa que declare uma matriz de dimensão 3×3 e preencha 
 com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matr = [[0,0,0], [0,0,0], [0,0,0]]

for l in range (0,3):
    for c in range (0,3):
        matr[l][c] = int(input('Digite o número: '))
print('-'*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matr[l] [c]:^5}]',end=' ')    
    print()




