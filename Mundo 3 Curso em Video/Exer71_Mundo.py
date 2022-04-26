'''
Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')


print(f'A-) Os 5 primeiros times são: {times[0:5]}')
print()
print(f'B-) Os 4 últimos times são: {times[-4:]}')
print()
print(f'C-) A ordem alfabética dos times é: {sorted(times)}')
print()
print(f'D-) A CHAPECOENCE está na: {times.index("Chapecoence") + 1}º posição')

