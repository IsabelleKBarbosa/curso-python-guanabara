# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 27 ##')
print ()
nome = str (input('Digite o nome completo: ')).title().strip().split()
print ()
print (f' - Primeiro Nome: {nome[0]}')
print (f' - Último Sobrenome: {nome[len(nome) - 1]}')
