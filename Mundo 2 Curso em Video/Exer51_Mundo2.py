'''
Crie um programa que leia uma frase qualquer e diga 
se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''

print('=*'*19)
print('           É PALINDROMO ??')
print('=*'*19)
print('\n')

texto = str(input('Digite uma frase por favor: ')).strip().upper()
palavra = texto.split()
juntar =''.join(palavra)
aocontrario = ''

for letra in range (len(juntar) -1, -1, -1):
    aocontrario += juntar[letra]
    

if aocontrario == juntar:
    print('Temos um palindromo !')
    print(juntar)
    print(aocontrario)   
else:
    print('Não é palindromo !')  
    print(juntar)
    print(aocontrario)