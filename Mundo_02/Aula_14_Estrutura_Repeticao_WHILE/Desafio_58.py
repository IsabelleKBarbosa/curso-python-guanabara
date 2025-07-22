#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 58 ##')
print ()
print ('Vamos jogar! Irei pensar em um número entre \033[1;30;41m 0 e 10 \033[m... E tente adivinhar qual é!\n')
numero = randint (0, 10)
c = 0
contador = 0
while c == 0:
    tentativa = int (input ('Digite um número entre \033[1;31m 0 e 10 \033[m: '))
    if tentativa == numero:
        print ('\n\033[7mParabéns! Você VENCEU!\033[m')
        c = 1
    elif tentativa > 10:
        print ('\nVocê digitou um número fora do combinado.\n'
               '\033[1mTente novamente!\n\033[m')
    else:
        if tentativa > numero:
            print (f'\nOps....É um número MENOR!\n'
                   f'\033[1mTente novamente!\n\033[m')
        else:
            print (f'\nQuase lá... É um número MAIOR!\n'
                   f'\033[1mTente novamente!\n\033[m')
    contador += 1
print (f'\nAdorei jogar com você!\nO número de tentativas até você ganhar foi: {contador}')
