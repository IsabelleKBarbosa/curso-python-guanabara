#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 64 ##')
print ()
print ('=== SOMA E QUANTIDADE ===')
print ('Atenção: Digite \033[31m999\033[m para encerrar o programa e parar a contagem.\n')
n = int (input('Digite um número inteiro qualquer: '))
c = 0
soma = 0
while n != 999:
    soma += n
    c += 1
    n = int(input('Novamente: '))
if c > 1:
    print ()
    print ('-'*10)
    print (f'Condição de parada identificada!\n'
           f'Quantidade de números digitados: {c}\n'
           f'Soma entre todos os números: {soma}')
    print ('-'*10)
print ('\033[1mPrograma Encerrado.')
