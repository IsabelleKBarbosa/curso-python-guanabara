#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 13 ##')
print ()
sal = float(input('Informe o salário atual: R$ '))
ajuste = (sal * 0.15)
novo = ajuste + sal
print (f'Aumento salarial: R$ {ajuste:.2f}')
print (f' - Salário atualizado com aumento de 15%: R$ {novo:.2f}')
