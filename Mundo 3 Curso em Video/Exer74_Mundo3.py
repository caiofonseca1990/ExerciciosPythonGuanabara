'''
Crie um programa que tenha uma tupla única com nomes de produtos 
e seus respectivos preços, na sequência. No final, mostre 
uma listagem de preços, organizando os dados em forma tabular.
'''
lista = ('Bolacha',  1.75,
        'Sal',       1.99,
        'Sabonete',  0.98,
        'Pão',       7.90,
        'Fandangos', 10.50,
        'Pepsi',     7.50,
        'Arroz',     25.00)
print('-'*100)
print(f'{"VENDINHA GUANABARA":^100}')
print('-'*100)
print()
for p in range(0,len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]: <35}',end='')
    else:           
        print(f'R$: {lista[p]:>4.2f}')