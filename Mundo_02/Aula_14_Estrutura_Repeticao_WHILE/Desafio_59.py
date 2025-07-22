#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 59 ##\n')
print ('=== OPERAÇÕES MATEMÁTICAS ===')
print ('A seguir, informe dois números e depois o código para a operação desejada.\n')
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite o segundo valor: '))
c = 0
while c == 0:
    print ('\n\033[1;30;45mMENU DE OPÇÕES\033[m')
    print ('Qual código da opção desejada?\n'
           '[1] Somar\n'
           '[2] Multiplicar\n'
           '[3] Maior número\n'
           '[4] Digitar novos números\n'
           '[5] Sair\n')
    op = int (input('Opção: '))
    print ()
    if op == 1:
        soma = n1 + n2
        print (f'\033[7mResultado: {n1} + {n2} = {soma:.2f}\033[m')
        print ()
    elif op == 2:
        multi = n1 * n2
        print (f'\033[7mResultado: {n1} x {n2} = {multi:.2f}\033[m')
    elif op == 3:
        if n1 > n2:
            print (f'\033[7mResultado: Maior Número é: {n1}\033[m')
        else:
            print (f'\033[7mMaior Número é: {n2}\033[m')
    elif op == 4:
        n1 = float(input('Digite um novo valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif op == 5:
        c = 1
    else:
        print ('Código não reconhecido. Tente novamente.')
print ('Fim')
