#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 42 ##')
print ()
print ('=== CLASSIFICANDO TRIÂNGULOS ===')
print ('Forneça os seguintes dados na unidade de centímetros:\n')
lado1 = float (input ('Digite a primeira medida: '))
lado2 = float (input('Digite a segunda medida: '))
lado3 = float (input('Digite a última medida: '))
soma1 = lado1 + lado2
soma2 = lado2 + lado3
soma3 = lado1 + lado3
print ()
if soma1 > lado3 and soma2 > lado1 and soma3 > lado2:
    print (f'O triângulo de lados {lado1, lado2, lado3} EXISTE!')
    if lado1 == lado2 == lado3:
        print ('Classificação: EQUILÁTERO')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print ('Classificação: ISÓSCELES')
    elif lado1 != lado2 != lado3 != lado1:
        print ('Classificação: ESCALENO')
else:
    print ('Não é possível formar um triângulo com essas medidas.')
