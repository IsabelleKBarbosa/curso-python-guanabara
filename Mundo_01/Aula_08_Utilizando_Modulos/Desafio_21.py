#Crie um programa que sorteie 6 números aleatórios entre 1 e 60, como um jogo da Mega-Sena.
from random import sample
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 21 ##')
print ()
print("=== MEGA SENA ===")
numeros = sample(range(1, 61), 6)
print ()
print(f'- Números sorteados: {sorted(numeros)}')
