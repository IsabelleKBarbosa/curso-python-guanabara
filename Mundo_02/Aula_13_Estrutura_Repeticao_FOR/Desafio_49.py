#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 49 ##')
print ()
print ('== TABUADA ==')
cont = 0
n = int (input('Digite um número inteiro para ver a tabuada: '))
print ()
for x in range (0, 11):
    print (f'{n} x {cont} = {n*cont}')
    cont += 1
print ('\nFim')
