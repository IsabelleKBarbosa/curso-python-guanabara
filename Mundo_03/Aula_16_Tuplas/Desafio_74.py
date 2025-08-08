# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from time import sleep
from random import sample
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 74 ##')
print ()
print ('=== NÚMEROS ALEATÓRIOS ===')
print ('Aguarde enquanto eu sorteio 5 números aleatórios no intervalo de 0 até 15.')
for x in range (0,5):
    sleep(0.2)
    print ('.\n', end = '')
    sleep(0.2)
    x += 1
n = sorted(sample(range(0,16), 5))
print (f'Números selecionados: \033[7m{n}\033[m')

print (f'O maior número foi: {n[4]}')
print (f'O menor número foi: {n[0]}')
#Também poderia usar a função:
# {max(n)} e {min(n)}
