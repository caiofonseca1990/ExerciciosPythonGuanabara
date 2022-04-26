'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
'''
guardar = []
esp = str(input('Digite sua expressão: '))

abre = '('
fecha = ')'

for paren in esp:
    if paren == abre:
        guardar.append(abre)
    elif paren == fecha:
        if len(guardar) > 0:
            guardar.pop()
        else:
            guardar.append(')')    
            break

if len(guardar) == 0:
    print('Expressão correta !')
else:
    print('Expressão invalida !')