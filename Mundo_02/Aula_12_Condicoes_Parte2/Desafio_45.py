#Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import choice
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 45 ##')
print ()
print ('Vamos jogar Jokenpô?!')
print ('A opções são:\n'
       '[1] PEDRA 🗿\n'
       '[2] PAPEL 📄\n'
       '[3] TESOURA ✂️\n')
print ('Primeiro eu irei escolher. Depois digite a sua opção, ok? Não vale olhar! haha')
print ('Escolhendo...')
sleep(1)
lista = [1,2,3]
escolha = choice(lista)
print ('Já escolhi!')
usuario = int (input('Sua vez! Digite sua opção: '))
print ('\n')
print ('=== RESULTADO ===\n')
print (f'Minha escolha: {escolha} -', end=' ')
if escolha == 1:
    print ('PEDRA 🗿')
elif escolha == 2:
    print ('PAPEL 📄')
else:
    print ('TESOURA ✂️')
print (f'Sua escolha: {usuario} -', end=' ')
if usuario == 1:
    print ('PEDRA 🗿')
elif usuario == 2:
    print ('PAPEL 📄')
elif usuario == 3:
    print ('TESOURA ✂️')
else:
    print ('Opção inválida!')
print ()
if usuario == escolha:
    print ('EMPATE!')
elif usuario == 1 != escolha:
    if escolha == 2:
        print ('GANHEI!✨')
    elif escolha == 3:
        print ('VOCÊ GANHOU!🎉')
elif usuario == 2 != escolha:
    if escolha == 1:
        print ('VOCÊ GANHOU!🎉')
    elif escolha == 3:
        print ('GANHEI!✨')
elif usuario == 3 != escolha:
    if escolha == 1:
        print ('GANHEI!✨')
    elif escolha == 2:
        print ('VOCÊ GANHOU!🎉')
else:
    print ('Alguma coisa deu errado... Vamos tentar novamente!')
