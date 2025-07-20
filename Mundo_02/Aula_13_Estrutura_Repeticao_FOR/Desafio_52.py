#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 52 ##')
print ()
print ('== NÚMERO PRIMO ==')
print ('Atenção: Número primo só pode ser divisível por 1 e por ele mesmo.\n')
n = int (input('Digite um número para descobrir se é primo: '))
print ()
controle = 0
print ('Divisível por: |', end = "")
for x in range (1,n + 1):
    div = n % x
    if div == 0:
        print (f' {x} |', end = "")
        controle += 1
print(f'\nTotal de divisores: {controle}')
print ()
if controle == 2:
    print (f'\033[1;32m{n} É PRIMO!\033[m')
else:
    print (f'\033[1;31m{n} NÃO é primo\033[m')
