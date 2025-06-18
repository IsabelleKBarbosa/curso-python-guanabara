#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 16 ##')
print ()
num = float (input('Digite um número real qualquer: '))
print(f' - A porção inteira de {num} corresponde a:  {num.__trunc__()}')
