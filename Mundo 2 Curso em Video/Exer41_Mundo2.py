'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Por favor, digite seu peso: '))
altura = float(input('Por favor, digite sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('O seu peso é {:.2f} e seu IMC é {:.2f}, você esta ABAIXO DO PESO'.format(peso, imc))
elif imc < 25:
    print('O seu peso é {:.2f} e seu IMC é {:.2f}, você esta no PESO IDEAL'.format(peso, imc))    
elif imc < 30:
    print('O seu peso é {:.2f} e seu IMC é {:.2f}, você esta com SOBREPESO'.format(peso, imc))    
elif imc < 40:
    print('O seu peso é {:.2f} e seu IMC é {:.2f}, você esta com OBESIDADE'.format(peso, imc))    
else:
    print('O seu peso é {:.2f} e seu IMC é {:.2f}, você esta com OBESIDADE MÒRBIDA'.format(peso, imc))    