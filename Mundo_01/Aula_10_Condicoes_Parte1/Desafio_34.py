#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 34 ##')
print ()
print ('=== AJUSTE SALARIAL ===\n')
atual = float (input('Digite o salário atual em R$: '))
if atual > 1250:
    ajuste = (atual * 0.1)
    novo = ajuste + atual
else:
    ajuste = (atual * 0.15)
    novo = ajuste + atual
print (f'- O salário terá AUMENTO de R$ {ajuste:.2f} \n'
           f'- Novo Salário: R${novo:.2f}')
