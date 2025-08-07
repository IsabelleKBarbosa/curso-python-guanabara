#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 72 ##')
print ()
print ('=== ESCRITA NUMÉRICA ===\n')

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'Seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
linha = ('-'*20)

while True:
    n = int (input('Digite um número de \33[1m0 até 20\033[m para ver a respectiva escrita: '))

    while n < 0 or n > 20:
        print ('Fora do intervalo.\nTente novamente!')
        print (linha)
        n = int(input('Digite um número de \33[1m0 até 20\033[m: '))

    print (f'\nEscrita: \033[7m{extenso[n]}\033[m')
    print (linha)
    continuar = str(input('Deseja fazer novamente [S/N] ? ')).upper().strip()[0]
    print ()
    while continuar not in 'SN':
        continuar = str(input('Escolha inválida.\nDigite [N] para NÃO ou [S] para SIM: ')).strip().upper()[0]
        print (linha)
    if continuar == 'N':
        break

print('\n\033[1;32mPrograma Finalizado!\033[m')
