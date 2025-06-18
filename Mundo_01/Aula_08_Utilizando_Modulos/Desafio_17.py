#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 17 ##')
print ()
print ('Vamos calcular o valor da hipotenusa. Para isso, informe os seguintes dados: \n')
oposto = float (input('Digite o valor do cateto oposto (cm): '))
adj = float (input ('Digite o valor do cateto adjacente (cm): '))
parcial = ((oposto.__pow__(2)) + (adj.__pow__(2)))
hip = math.sqrt(parcial)
#outro jeito: hy = math.hypot(oposto, adj)
print ()
print (f' - O resultado da hipotenusa é: {hip:.2f}')
