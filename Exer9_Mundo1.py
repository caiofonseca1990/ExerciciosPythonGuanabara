#Calcular quntos litros de tinta vai para pintar uma parede

largura = float(input('Digite a largura da parede:  '))
altura = float(input('Digite a altura da parede:  '))

area = largura * altura

print('Para pintar uma area de {:.2f}m² metros será nescessário usar {:.2f} latas de tinta'.format(area, area/2))