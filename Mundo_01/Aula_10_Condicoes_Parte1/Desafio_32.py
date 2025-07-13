#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 32 ##')
print ()
print ('Por definição, o ano BISSEXTO trata-se de um ano que tem um dia extra, ou seja, 366 dias em vez de 365!\n'
       'Isso ocorre a cada quatro anos e o mês de fevereiro terá 29 dias. Legal, né?\n')
ano = int (input('Digite um ano par saber se é BISSEXTO ou não: '))
print ()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'- Sim, o ano de {ano} É BISSEXTO!')
else:
    print (f'- Não, o ano de {ano} NÃO é bissexto!')

