#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
#Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 28 ##')
print ()
print ('Vamos jogar! Irei pensar em um número... E tente adivinhar qual é!\n')
numero = randint (0, 5)
tentativa = int (input (' - Digite um número entre 0 e 5: '))
if tentativa == numero:
    print ('\nParabéns! Você VENCEU!')
else:
    print (f'\nVocê PERDEU!\n'
           f'Tente me ganhar na próxima!\n'
           f'O número que pensei foi {numero}.')

