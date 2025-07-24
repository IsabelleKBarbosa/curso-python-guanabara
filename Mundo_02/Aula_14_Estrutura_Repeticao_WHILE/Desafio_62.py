#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 62 ##')
print ()
print ('=== PROGRESSÃO ARITMÉTICA 03 ===')
a1 = float (input('Digite o primeiro termo da PA: '))
r = float (input('Digite a razão da PA: '))
c = 1
an = a1
while c != 0:
    print(f'{c}º Termo: {an:.1f}')
    an = an + r
    c += 1
    if c > 10:
        mais = int (input('\nSe quiser saber mais "n" termos, digite a quantidade. '
                          'Caso queira encerrar, digite [0]: '))
        contador = 0
        for x in range (contador, mais-1):
            print(f'{c}º Termo: {an:.1f}')
            an = an + r
            c += 1
            contador += 1
        if mais == 0:
            print (f'\033[7mPA encerrada com o total de {c-1} termos.\033[m')
            c = 0
print ('\nFim')

# OUTRA FORMA
#
# a1 = float(input('Digite o primeiro termo da PA: '))
# r = float(input('Digite a razão da PA: '))
#
# termo = a1
# contador = 1
# total = 0
# mais = 10  # Começa mostrando 10 termos
#
# while mais != 0:
#     total += mais  # soma os termos que serão mostrados
#     while contador <= total:
#         print(f'{contador}º Termo: {termo:.1f}')
#         termo += r
#         contador += 1
#     print()
#     mais = int(input('Quantos termos você quer mostrar a mais? [0 para encerrar] '))
#
# print(f'\nPA encerrada com um total de {total} termos mostrados.')
# print('Fim')
