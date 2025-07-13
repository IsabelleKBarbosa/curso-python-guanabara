#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 30 ##')
print ()
numero = int (input('Digite um número inteiro para descobrir se é PAR ou ÍMPAR: '))
resposta = numero % 2
print ()
if resposta == 1:
    print (f'O número {numero} é: ÍMPAR')
else:
    print (f'O número {numero} é: PAR!')
  
