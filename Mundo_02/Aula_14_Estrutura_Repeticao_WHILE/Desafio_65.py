#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 65 ##')
print ()
print ('=== MÉDIA E COMPARAÇÃO ===')
n = int (input('Digite um número inteiro qualquer: '))
r = str (input('Deseja continuar? [S/N] ')).strip(). upper()[0]
print ()
soma = maior = menor = n
contador = 1
while r == 'S':
    n = int(input('Digite um número inteiro qualquer: '))
    soma += n
    contador += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print ()
media = soma/contador
print ('\033[7m---- RESULTADOS ----\033[m')
print (f'Soma de todos os números: {soma}')
print (f'Maior número digitado: {maior}')
print (f'Menor número digitado: {menor}')
print (f'Total de números digitados: {contador}')
print (f'Média: {media:.2f}')
