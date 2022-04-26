'''
Refazer o exêrcicio anterior usando o laço FOR
'''

n = int(input('Digite um número para calcular o Fatorial: '))
fatorial = 1
print('O fatorial de {}!:  '.format(n),end='')

for n in range (n,fatorial -1,-1 ):
    
    print(n,end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial *= n
 

print('É {}'.format(fatorial))
