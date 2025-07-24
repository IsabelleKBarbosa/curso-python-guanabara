#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 61 ##')
print ()
print ('=== PROGRESSÃO ARITMÉTICA 02 ===')
a1 = float (input('Digite o primeiro termo da PA: '))
r = float (input('Digite a razão da PA: '))
c = 1
an = a1
while c < 11:
    print(f'{c}º Termo: {an:.1f}')
    an = an + r
    c += 1
print ('\nFim')
