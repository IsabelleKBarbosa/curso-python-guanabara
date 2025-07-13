#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 31 ##')
print ()
print ('Vamos calcular o custo do translado da sua viagem.')
dist = float (input('- Qual a distância em KM que será percorrido? '))
if dist <= 200:
    custo = dist * 0.5
    print (f'\nO custo do deslocamento será: R$ {custo:.2f}')
else:
    custo = dist * 0.45
    print (f'\nO custo do deslocamento será: R$ {custo:.2f}')

