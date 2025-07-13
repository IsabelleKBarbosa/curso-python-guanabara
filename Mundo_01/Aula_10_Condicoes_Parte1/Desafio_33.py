# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 33 ##')
print ()
print ('Vamos colocar os números em ordem e definir o maior e o menor?\n')
n1 = int (input ('Digite um número qualquer: '))
n2 = int (input ('Escolha outro número: '))
n3 = int (input ('Escolha mais um: '))
print ()
print ('Organizando...')
sleep(1)
lista = [n1, n2, n3]
ordem = sorted(lista)
print (f'A ordem dos números é: {ordem}')
menor = ordem[0]
maior = ordem[-1]
# - O maior também poderia ser ordem [2], mas se acrescentar mais números a posição do maior número irá mudar.
# Fazer -1 faz a leitura de trás pra frente, independente do tamanho da lista.
print (f' - O número MENOR é: {menor}')
print (f' - O número MAIOR é: {maior}')

### UTILIZANDO ESTRUTURA DE CONDIÇÃO
#maior = n1
#menor = n1
#if n2 > maior:
#   maior = n2
#if n3 > maior:
#   maior = n3
#if n2 < menor:
#   menor = n2
#if n3 < menor:
#   menor = n3
#print()
#print(f'O número MENOR é: {menor}')
#print(f'O número MAIOR é: {maior}')

