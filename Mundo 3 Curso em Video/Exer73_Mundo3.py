'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
n = (int(input('Digite o 1º número : ')),
    int(input('Digite o 2º número : ')),
    int(input('Digite o 3º número : ')),
    int(input('Digite o 4º número : ')))

print(f'Na listagem temos os seguintes números: {n}.')
print(f'Na listagem temos a seguinte ordem: {sorted(n)}.')
print(f'O número  9 aparece {n.count(9)} vez(es).')
print(f'O número  3 aparece na posição {n.index(3)+1}.')

for pares in n:
    if pares % 2 == 0:
        print(f'Os pares da sequencia foram {pares}')




    
    



        
