#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 44 ##')
print ()
print ('=== CONDIÇÕES DE PAGAMENTO ===')
print ('Para saber o valor a ser pago, forneça as seguintes informações:\n')
valor = float (input('Digite o preço normal do produto: R$ '))
print ('Opções de pagamento:\n'
       '[1] - À vista, Dinheiro ou Cheque: 10% de desconto\n'
       '[2] - À vista no cartão: 5% de desconto\n'
       '[3] - Cartão em 2x: Preço normal\n'
       '[4] - Cartão em 3x ou mais: 20% de juros')
cod = int (input('Digite o código da opção de pagamento desejada: '))
print ()
if cod == 1:
    desconto = valor * 0.10
    pagamento = valor - desconto
    print (f'Desconto: R${desconto:.2f}')
elif cod == 2:
    desconto = valor * 0.05
    pagamento = valor - desconto
    print (f'Desconto: R${desconto:.2f}')
elif cod == 3:
    pagamento = valor
    mensalidade = pagamento / 2
    print (f'Mensalidade: R${mensalidade:.2f} durante 2 meses')
elif cod == 4:
    juros = valor * 0.20
    pagamento = valor + juros
    parcela = int (input('Digite o número de parcelas: '))
    mensalidade = pagamento / parcela
    print (f'Juros: R${juros:.2f}')
    print (f'Mensalidade: R${mensalidade:.2f} durante {parcela} meses\n')
else:
    print ('Atenção: Opção de pagamento não reconhecida.\nTente novamente!')
if cod in (1,2,3,4):
    print (f'\033[7mVALOR TOTAL: R$ {pagamento:.2f}\033[m')
