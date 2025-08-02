#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 70 ##')
print ()
#Códigos Utilizáveis
linha = ('-' * 50)
on = '\033[1m'
off = '\033[m'
##
print('=== CAIXA DE LOJA ===')
cadastro = str(input('Deseja iniciar [S/N]? ')).upper().strip()[0]
while cadastro not in 'SN':
    print(f'\033[1;37mOpção inválida. Tente novamente!{off}')
    cadastro = str(input('Deseja iniciar [S/N]? ')).upper().strip()[0]
print(linha)

total = mil = 0
barato = None
nome = ''

while cadastro == 'S':
    produto = str(input('Produto: ')).upper().strip()

    # VALIDAÇÃO DE VALOR NUMÉRICO POSITIVO
    while True:
        try:
            valor = float(input('Preço: R$ '))
            if valor < 0:
                print(f'\033[1;33mO valor deve ser positivo.{off}')
            else:
                break
        except ValueError:
            print('\033[1;31mEntrada inválida! Por favor, digite um número.\033[m')
    total += valor

    if valor > 1000:
        mil += 1

    if barato is None or valor < barato:
        barato = valor
        nome = produto

    print(linha)
    cadastro = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while cadastro not in 'SN':
        print(f'\033[1;37mOpção inválida. Tente novamente!{off}')
        cadastro = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    print(linha)

if total == 0:
    print(f'\n{on}Programa encerrado sem cadastros.{off}'.center(50))
else:
    print(f'\033[7mRESULTADO{off}'.center(50))
    print(f'A) Total da compra: R${total:.2f}')
    if mil > 0:
        print (f'B) Quantidade de produtos que custam mais de R$1000: {mil}')
    else:
        print ('B) Nenhum produto custou mais de R$1000.')
    print (f'C) Produto mais barato: {nome}')
