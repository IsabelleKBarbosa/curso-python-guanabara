#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 25 ##')
print ()
nome = str (input('Digite o nome completo: ')).lower().strip()
print (f' * A pessoa faz parte da família "Silva"? {'silva' in nome}')
