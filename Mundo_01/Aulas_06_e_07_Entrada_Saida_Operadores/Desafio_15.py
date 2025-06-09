#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 15 ##')
print ()
print ('Para calcular o valor a ser pago, informe os dados abaixo: \n')
dist = float (input ('Quantidade de quilômetros (KM) percorridos: '))
diaria = int (input ('Quantidade de diárias do aluguel: '))
valor = (dist * 0.15) + (diaria * 60)
print ()
print (f' - Preço a ser pago: R$ {valor:.2f}')
