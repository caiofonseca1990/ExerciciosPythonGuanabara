#Faça um programa que leia um número de 0 a 9999 e mostre cada um dos digitos separados
# #exemplo 
'''
Digite um número: 1834
unidade: 4
dezena : 3
centena: 8
milhar: 4
'''

n = int(input('Digite um número por favor: '))

print('O número digitado é :{}'.format(n))

u = n //1 %10
d = n //10 %10
c = n //100 %10
m = n //1000 %10

print('O número: {} é uma unidade '.format(u))
print('O número: {} é uma dezena '.format(d))
print('O número: {} é uma centena'.format(c))
print('O número: {} é um milhar '.format(m))





