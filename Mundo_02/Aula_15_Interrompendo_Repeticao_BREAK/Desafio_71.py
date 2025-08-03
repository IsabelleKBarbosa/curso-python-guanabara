#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 71 ##')
print ()
print ('=== CAIXA ELETRÔNICO ===')
print ('\033[1mSeja, bem vindo(a)!\033[m')
print ('Atenção: Cédulas disponíveis: R$50, R$20, R$10, R$1\n')

#Validação na Entrada do Usuário
while True:
    try:
        valor = int(input('\033[1;32mDigite o valor inteiro, sem contar os centavos, que deseja sacar: R$ \033[m'))
        if valor < 0:
            print('O valor deve ser positivo.')
        else:
            break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número.')

uni50 = uni20 = uni10 = uni1 = 0
if valor >= 50:
    uni50 = valor // 50
    valor = valor % 50
if valor >= 20:
    uni20 = valor // 20
    valor = valor % 20
if valor < 20:
    uni10 = valor // 10
    valor = valor % 10
if valor < 10:
    uni1 = valor // 1

print ('-'*40)
print ('\033[7mCÉDULAS\033[m'.center(40))
if uni50 > 0:
    print(f'R$50: {uni50} ')
if uni20 > 0:
    print(f'R$20: {uni20}')
if uni10 > 0:
    print(f'R$10: {uni10}')
if uni1 > 0:
    print(f'R$1: {uni1}')

#OUTRA FORMA:
# Cada cédula é processada sequencialmente, do maior para o menor valor, até que o valor seja zerado.
#Pode substituir das linhas 23 ate 45.

# for cedula in [50, 20, 10, 1]:
#     qtd = valor // cedula
#     valor %= cedula
#     if qtd > 0:
#         print(f'R${cedula}: {qtd}')
