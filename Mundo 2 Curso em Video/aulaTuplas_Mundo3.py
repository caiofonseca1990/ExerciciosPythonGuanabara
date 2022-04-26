# Aula de LISTAS

# as TUPLAS são imutaveis, ou seja, tuplas nao podem ser alteradas
# as LISTAS pode ser alteradas


lanche = ['bolo', 'beirute', 'mistinho', 'rocambole', 'coxinha', 'risoli']

lanche.append('pizza') # adciona um novo elemento ou item ao fim da lista
lanche.insert(0,'cachorro quente') # adciona um novo elemento ou item a lista utilizando o indice desejado ou posição desejada
del lanche[2] # elimina o item desejado e refaz os indices, reposicionando os outros indices
lanche.pop(3) # elimina o ultimo elemento de uma lista, porém sendo passado o parametro ele elimina o indice selecionado
lanche.remove('pizza') # elimina o elemento da lista informado.

valores = [2,5,1,7,4,3,7,82]
valores.sort()
#valores = list(range(4,11))


print(lanche)
print(valores)