#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 48 ##')
print ()
soma = 0
cont = 0
for n in range (1, 501):
    if n % 2 !=0 and n % 3 == 0:
        print (f'{n} + ', end = "")
        soma += n
        cont += 1
print (f'\n\nRESULTADO: {soma}')
print (f'A soma foi realizada: {cont} vezes')
