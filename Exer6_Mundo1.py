#Crie um algoritimo que converta um valor inputado para metros, centimetros e milimetros.

n = int(input('Digite um valor para conversão: '))

metro = n*100
centimetro = n*0.01
milimetro = n*0.001

print('O valor digitado é: {}\nO valor em Metros é: {}\nO valor em Centimetros é: {}\
    \nO valor em Milimetros é: {}'.format(n, metro,centimetro,milimetro))

