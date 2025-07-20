#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
from operator import invert

print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 53 ##')
print ()
print ('=== TESTE DE PALÍNDROMO ===\n')
frase = str(input('Digite uma frase qualquer: ')).upper().strip().replace(' ', '')
print ()
invertida = frase[::-1]
print(f'Frase invertida: {invertida}')
if invertida == frase:
    print ('\033[7mÉ UM PALÍNDROMO!\033[m')
else:
    print ('Não é um palíndromo.')
