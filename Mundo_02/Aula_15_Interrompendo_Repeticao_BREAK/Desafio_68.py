#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 68 ##')
print ()
on = '\033[1m'
dest = '\033[7m'
off = '\033[m'
print ('=== GAME: PAR OU ÍMPAR ===')
print (f'{on}Regras{off}: Você escolhe {dest}PAR ou ÍMPAR{off} e, em seguida, um número inteiro qualquer.\n'
       'Enquanto isso, eu irei escolher outro número e irei realizar a soma entre eles.\n'
       'Se a soma der a sua escolha (PAR ou ÍMPAR), você ganha e seguimos o jogo!\n'
       'Se não, você perde.\n')
print ('Vamos começar!')
num = soma = c = v = 0
r = 1
while True:
    print('-' * 50)
    print (f'{r}º RODADA: ')
    num = int (input('Digite o seu número: '))
    escolha = str(input('Escolha Par [P] ou Ímpar [I]: ')).strip().upper()[0]
    while escolha not in 'PIÍ':
        escolha = str(input('Escolha inválida.\nDigite [P] para Par ou [I] para Ímpar: ')).strip().upper()[0]
    pc = randint (0,11)
    soma = num + pc
    c += 1
    r += 1
    print (f'Meu número: {pc}\n')
    print (f'{on}SOMA: {num} + {pc} = {soma}{off}', end = '  ->  ')
    if soma % 2 == 1:
        print (f'{dest}ÍMPAR!{off}')
        if escolha == 'I' or escolha == 'Í':
            print ('Você ganhou...')
            v += 1
        else:
            break
    if soma % 2 == 0:
        print (f'{dest}PAR!{off}')
        if escolha == 'P':
            print ('Você ganhou...')
            v += 1
        else:
            break
print ('-'*50)
print ()
print (f'\033[1;31mVocê perdeu!{off}')
print(f'- Quantidade de rodadas: {c}\n'
      f'- Quantidade de vitórias: {v}')
