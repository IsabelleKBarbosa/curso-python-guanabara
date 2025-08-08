# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 73 ##')
print ()
off = '\033[m'
on = '\033[7m'
linha = '-'*20
print ('=== CAMPEONATO BRASILEIRO DE FUTEBOL - 2025 ===')
print ('Atenção: São 20 times no total.\n')
lista = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Mirassol', 'Bragantino',
         'Botafogo', 'São Paulo', 'Fluminense', 'Atlético-MG', 'Ceará SC', 'Corinthians',
         'Internacional', 'Grêmio', 'Santos', 'EC Vitória', 'Vasco da Gama', 'Fortaleza',
         'Juventude', 'Sport Recife')
print (f'a) Os 5 primeiros times são: {on}{lista[0:5]}{off}')
print (linha)
print (f'b) Os 4 últimos colocados são: {on}{lista[-4:]}{off}')
print (linha)
print (f'c) Lista em Ordem Alfabética: {sorted(lista)}')
print (linha)
escolha = str(input('d) Qual time deseja ver a posição? ')).title().strip()
if escolha in lista:
    print (f'O time {escolha} está na {lista.index(escolha) + 1}º posição!')
else:
    print('Time não encontrado na lista.')
print (linha)
print (f'e) Lista Completa: ')
n = 0
for x in range (1,21):
    print (f'   {x}º {lista[n]}')
    n += 1
