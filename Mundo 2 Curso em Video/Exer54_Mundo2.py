'''
Desenvolva um programa que leia o 
nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
a média de idade do grupo, 
qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.
'''
mulher = 0
somaidade = 0
for c in range (0,4):
    c += 1
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    somaidade += idade 
    media = somaidade / 4
#Bloco que verifica o mais velho do grupo e o mais novo.
    if c == 1 and sexo in 'Mm':
        velho = idade
        novo = idade
        nomevelho = nome
        nomenovo = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade < novo:
        novo = idade
        nomenovo = nome
#Bloco onde verifica a mulher mais nova.
    if sexo in 'Ff' and idade < 20:
        mulher += 1
        media = somaidade /4


print('\n')
print('A média de idade do grupo é: {:.2f}'.format(somaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(velho, nomevelho))
print('O homem mais novo do grupo tem {} anos e se chama {}.'.format(novo, nomenovo))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(mulher))
