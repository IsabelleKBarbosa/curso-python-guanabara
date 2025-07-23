#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
print('_____________________________________________________________________')
print()
print('## ATIVIDADE PRÁTICA - 60 ##')
print()
print('=== FATORIAL ===')
n = int(input('Digite um número inteiro para saber seu fatorial (!): '))
original = n
fatorial = 1
print ('\nRESULTADO:\n')
print (f'\033[7m{original}! = ', end = '')
while n > 0:
    print(f'{n}', end=' ')
    if n > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    fatorial *= n
    n -= 1
print(f'{fatorial}\033[m')
