# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 37 ##')
print ()
print ('Vamos fazer conversões numéricas!')
numero = int (input('Digite um número inteiro qualquer para ser convertido: '))
print ('Observe o código de cada base de conversão:\n'
                  '1 - BINÁRIA\n'
                  '2 - OCTAL\n'
                  '3 - HEXADECIMAL ')
base = int (input('Agora, digite o código da conversão que deseja: '))
if base == 1:
    escolha = 'Binária'
    conversao = bin(numero)[2:]
elif base == 2:
    escolha = 'Octal'
    conversao = oct(numero)[2:]
elif base == 3:
    escolha = 'Hexadecimal'
    conversao = hex(numero)[2:]
else:
    print ()
    print ('\033[1;31mOpção Inválida\033[m!'
           '\nTente Novamente.')
if base in (1, 2, 3):
    print ('\n== RESULTADO ==')
    print (f'- O número {numero} convertido para base {escolha} é: \033[1;7m{conversao}\033[m')
