# Faça um programa que leia uma frase pelo teclado
# Mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 26 ##')
print ()
frase = str (input ('Digite uma frase para ter a estrutura analisada: ')).lower().strip()
print ()
print (f' - Quantas vezes aparece a letra "A"? {frase.count('a')}')
print (f' - Em qual posição a letra "A" aparece a primeira vez? {frase.find('a') + 1}')
print (f' - Em qual posição a letra "A" aparece a última vez? {frase.rfind('a') + 1}')
