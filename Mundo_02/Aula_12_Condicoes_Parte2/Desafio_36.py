# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 36 ##')
print ()
print ('==== EMPRÉSTIMO BANCÁRIO ====\n')
print ('Para analisar sua solicitação de empréstimo, forneça os seguintes dados:')
valorcasa = float (input(' - Digite, em reais, o valor da casa que será comprada: R$ '))
salario = float (input (' - Digite o valor, em reais, do salário do(a) comprador(a): R$ '))
tempoano = int (input(' - Digite em quantos anos pretende quitar o valor: '))
print ()
parcela = valorcasa / (tempoano * 12)
if parcela > 0.3*salario:
    print ('ATENÇÃO: O valor da prestação mensal ultrapassa o limite de 30% do salário!\n'
           'Recomendado recalcular e aumentar o tempo de quitação.\n\n'
           f'Prestação Mensal: R$ {parcela:.2f} - Empréstimo será \033[7mNEGADO\033[m.')
else:
    print (' - Empréstimo poderá ser \033[7mAPROVADO\033[m.\n\n'
           f'Prestação Mensal: R$ {parcela:.2f}\n'
           f'Tempo Total: {(tempoano * 12)} meses')

