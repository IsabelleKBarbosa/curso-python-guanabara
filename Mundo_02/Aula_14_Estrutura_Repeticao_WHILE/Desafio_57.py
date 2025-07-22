#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 57 ##')
print ()
s = 1
while s == 1:
    r = str (input('Digite o sexo [M] - Masculino [F] - Feminino): ')).strip().upper()[0]
    if r not in ('M','F'):
        print ('Código não reconhecido. Tente novamente!\n')
    else:
        s = 0
print ('\033[1mCadastro realizado!\033[m')
