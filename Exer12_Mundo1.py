#Conversor de temperatura

ce = float(input('Digite a temperatura em Cº: '))
fa = float(input('Digite a temperatura em Fº: '))
kel = float(input('Digite a temperatura em Kº: '))

cefa = (ce * 1.8) + 32
face = (fa - 32) / 1.8
cekel = ce + 273.15
kelce = kel - 273.15


print('A temperatura em Cº {:.2f} convertido para Fº é: {:.2f}'.format(ce, cefa))
print('A temperatura em Fº {:.2f} convertido para Cº é: {:.2f}'.format(fa, face))
print('A temperatura em Cº {:.2f} convertido para Kº é: {:.2f}'.format(ce, cekel))
print('A temperatura em Kº {:.2f} convertido para Cº é: {:.2f}'.format(kel, kelce))