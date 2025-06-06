#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
print ('_____________________________________________________________________')
print ('## ATIVIDADE PRÁTICA ##')
print ()
n = int(input ('Digite um número: '))
suc = n + 1
ant = n - 1
print (f'Antecessor de {n} é {ant}.')
print (f'Sucessor de {n} é {suc}.')
print ()
print (f'Resultado Visual:  {ant} | {n} | {suc}')
