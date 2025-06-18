#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 18 ##')
print ()
ang = float (input('Digite um ângulo qualquer para obter o valor do seno, cosseno e tangente:  '))
#Precisa converter o ângulo para radianos. Pode criar nova variável ou fazer aninhado.
num = math.radians(ang)
print (f' - Seno: {math.sin(num):.2f}')
#Aninhado: print (f' - Seno: {math.sin(math.radians(ang)):.2f}')
print (f' - Cosseno: {math.cos(num):.2f}')
print (f' - Tangente: {math.tan(num):.2f}')
