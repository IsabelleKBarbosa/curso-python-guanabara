#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 55 ##')
print ()
print ('=== COMPARATIVO ===')
maior = 0
menor = 0
for x in range (1,6):
    peso = float (input (f'Digite o peso da {x}º pessoa em KG: '))
    if x == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print ()
print (f'Maior peso: {maior:.2f} kg')
print (f'Menor peso: {menor:.2f} kg')
