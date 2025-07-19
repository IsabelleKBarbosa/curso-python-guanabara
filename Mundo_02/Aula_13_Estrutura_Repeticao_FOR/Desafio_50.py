#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 50 ##')
print ()
print ('Digite seis números inteiros, um por um, a seguir:')
soma = 0
cont = 1
for x in range (0,6):
    n = int (input(f'{cont}º Número: '))
    cont += 1
    if n % 2 == 0:
        soma = soma + n
print (f'\nA soma dos números pares é: {soma}')
