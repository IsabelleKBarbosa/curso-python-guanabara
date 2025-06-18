#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 20 ##')
print ()
print ('Digite o nome dos alunos que irão se apresentar para que a ordem seja aleatorizada: ')
n1 = str (input('- Aluno(a): '))
n2 = str (input ('- Aluno (a): '))
n3 = str (input('- Aluno(a): '))
n4 = str (input ('- Aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle (lista)
print ()
print (f' - A ordem de apresentação será: {lista}')
