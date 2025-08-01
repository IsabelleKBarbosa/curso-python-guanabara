# Crie um programa que leia números inteiros pelo teclado.
# programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 66 ##')
print ()
print ('=== LEITURA E SOMA DE NÚMEROS ===')
print ('Atenção: Para encerrar o programa digite \033[7m999\033[m\n')
n = s = c = 0
while True:
    n = int (input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print ()
print (f'SOMA TOTAL = \033[7;35m{s}\033[m')
print (f'Quantidade total de números: {c}')
