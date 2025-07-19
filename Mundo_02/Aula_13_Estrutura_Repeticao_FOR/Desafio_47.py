#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
from time import sleep
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 47 ##')
print ()
print ('Os números pares que estão no intervalo entre 1 e 50 são:\n')
for pares in range (0,51,2):
    print (f' - {pares}', end= '')
    sleep(0.2)
print ('\n\nFIM!')
