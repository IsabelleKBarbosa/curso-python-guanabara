# #Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
from random import sample

print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 75 ##')
print ()
on = '\033[7m'
off = '\033[m'
linha = ('-'*25)
print ('=== GUARDANDO VALORES ===')
print (f'A seguir, digite 4 valores inteiros aleatórios: \n')

n1 = int(input('Digite um número: '))
print (linha)
n2 = int (input('Digite outro número: '))
print (linha)
n3 = int (input('Digite mais um número: '))
print (linha)
n4 = int (input('Digite o último número: '))
print (linha)

valores = (n1, n2, n3, n4)
print (f'Valores digitados: {on}{valores}{off}')

print (f'\n{on}Resultados:{off}')
if 9 in valores:
    print (f'a) O valor 9 apareceu {valores.count(9)} vez(ez)')
else:
    print ('a) O valor 9 não foi digitado.')

if 3 in valores:
    print (f'b) O valor 3 foi digitado na {valores.index(3) + 1}ª posição')
else:
    print ('b) O valor 3 não foi digitado.')

print (f'c) Números pares digitados: ', end = '')
cont = 0
for x in valores:
    if x % 2 == 0:
        print (f'{x}', end = '  ')
        cont += 1
if cont == 0:
    print ('Não foram digitados números pares.')
