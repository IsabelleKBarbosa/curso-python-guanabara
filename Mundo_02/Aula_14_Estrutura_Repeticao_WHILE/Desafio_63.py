# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 63 ##')
print ()
print ('=== SEQUÊNCIA DE FIBONACCI === ')
print ('Curiosidade: Trata-se de uma sequência numérica em que cada termo subsequente é a soma dos dois termos anteriores, começando geralmente com 0 e 1.\n')
n = int (input('Digite a quantidade de termos de uma Sequência de Fibonacci que você queira conferir: '))
c = 0
soma = 0
ultimo = 1
anterior = 0
while c < n:
    print (f'{anterior} -> ', end = "")
    soma = ultimo + anterior
    anterior = ultimo
    ultimo = soma
    c += 1
print ('Fim')
