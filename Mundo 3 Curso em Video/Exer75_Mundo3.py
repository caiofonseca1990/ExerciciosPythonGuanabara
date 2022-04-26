'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('cafe', 'melao', 'pastel', 
            'jogo', 'bicicleta', 'bola', 
            'chiclete', 'bife', 'pandora', 
            'mosaico', 'xadrez', 'tenis',)

for indice in palavras:
    print(f'\nNa palavra {indice} temos as vogais: ',end=' ')            
    for vogal in indice:
        if vogal.lower() in 'aeiou':
            print(f'{vogal} ',end='')

    
