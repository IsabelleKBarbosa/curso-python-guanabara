#Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 38 ##')
print ()
print ('Vamos comparar dois números inteiros! Faça o que se pede:')
n1 = int (input('Digite o primeiro número: '))
n2 = int (input('Digite o segundo número: '))
print ()
if n1 > n2:
    print ('O primeiro valor é maior!')
    print (f'\033[1;35m{n1} > {n2}\033[m')
elif n2 > n1:
    print ('O segundo valor é maior!')
    print (f'\033[1;35m{n2} > {n1}\033[m')
else:
    print ('Não existe valor maior. Os dois são iguais!')
