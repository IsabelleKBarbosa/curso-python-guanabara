#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 35 ##')
print ()
print ('Vamos verificar a existência de um triâgulo a partir do comprimento de três retas!\n')
r1 = float (input('Digite o comprimento da primeira reta: '))
r2 = float (input ('Digite o comprimento da segunda reta: '))
r3 = float (input ('Digite o comprimento da última reta: '))
print ()
soma1 = r1 + r2
soma2 = r2 + r3
soma3 = r1 + r3
if soma1 > r3 and soma2 > r1 and soma3 > r2:
    print ('- Sim, um triângulo pode ser formado a partir dessas três retas!')
else:
    print ('- Não, não é possível formar um triângulo com essas medidas!')

