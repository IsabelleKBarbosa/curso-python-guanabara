#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC).
#Mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 43 ##')
print ()
print ('=== ÍNDICE DE MASSA CORPORAL ===')
print ('Para calcular o IMC, forneça os seguintes dados:\n')
peso = float (input('Digite o peso em kg: ').strip())
altura = float (input ('Digite a altura em metros: ').strip())
imc = peso / (altura * altura)
print ()
print (f'Resultado IMC: {imc:.1f}')
if imc < 18.5:
    print ('Status: Abaixo do Peso')
elif imc <= 25:
    print ('Status: Peso Ideal')
elif imc <= 30:
    print ('Status: Sobrepeso')
elif imc <= 40:
    print ('Status: Obesidade')
else:
    print ('Status: Obesidade Mórbida')


