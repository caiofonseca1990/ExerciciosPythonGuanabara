'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''
contidade = conth = contm20 = 0
opc = 'SsMm'
while True:
    idade = int(input('Digite sua idade por favor: '))
    sexo = str(input('Como você define sua sexualidade? [F/M]: ').strip()).upper() [0]
    print('-'*60)
    opc = str(input('   Deseja continuar o cadastro? [S / N]: ').strip()).upper() 
    print('-'*60)
    if opc in 'N':
        break
    
    elif sexo not in 'FfMm':
        print('Apemas o sexo senhor, nada de números!')
        sexo = str(input('Vamos denovo, sua sexualidade?: ').strip()).upper() [0]
            
    if idade >= 18:
        contidade += 1
        #print(f'maior que 18: {contidade} ')
    
    if sexo in 'M':
        conth += 1
        #print(f'Homens: {conth}')
    
    if sexo in 'F' and idade < 20:
        contm20 += 1
        #print(f'Mulher menor de 20 anos: {contm20}')

print('O programa foi encerrado!')
print('-'*60)
print(f'Temomo: {contm20} mulheres menores de 20 anos.')
print('-'*60)
print(f'Temos: {conth} homens cadastrados.')
print('-'*60)
print(f'Temos: {contidade} pessoas maiores de 18 anos.')
print('-'*60)