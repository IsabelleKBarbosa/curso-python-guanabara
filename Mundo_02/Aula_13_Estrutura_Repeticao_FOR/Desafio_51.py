#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 51 ##')
print ()
print ('== PROGRESSÃO ARITMÉTICA ===')
print ('Forneça as seguintes informações:\n')
a1 = float (input('Digite o primeiro termo da PA: '))
r = float (input('Digite a razão da PA: '))
print ()
print ('- 10 primeiros termos -\n')
n = 0
sn = 0
for x in range (1,11):
    n += 1
    an = a1 + ((n - 1) * r)
    sn =+ an
    print (f'{n}º Termo: {an:.1f}')
print ('Fim')
