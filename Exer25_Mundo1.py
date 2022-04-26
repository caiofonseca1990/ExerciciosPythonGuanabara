#Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente
'''
Exemplo: Ana Maria de Souza
primeiro = Ana
última = Souza
'''
nome = str(input('Digite seu nome completo por favor: ')).strip().upper()

print('Seu nome completo é {}'.format(nome))

print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu primeiro nome é: {}'.format(nome.split()[-1])) 
