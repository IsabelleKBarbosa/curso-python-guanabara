#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 54 ##')
print ()
print ('== MAIORIDADE - 18 anos ==')
print ('Digite o que se pede de cada um dos 7 integrantes do grupo:\n')
maior = 0
menor = 0
for x in range (1,8):
    nasc = int (input(f'{x}º Pessoa - Ano de Nascimento: '))
    idade = date.today().year - nasc
    print (f'Idade: {idade} anos')
    if idade > 17:
        print ('MAIORIDADE ATINGIDA\n')
        maior += 1
    else:
        print ('Menor de idade.\n')
        menor += 1
print (f'Total de pessoas MAIORES de idade: {maior}')
print (f'Total de pessoas MENORES de idade: {menor}')
