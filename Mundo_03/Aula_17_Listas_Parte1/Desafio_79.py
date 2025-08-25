# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 79 ##')
print ()
print ('=== LISTA SEM REPETIÇÃO ===')
print ('Digite números inteiros quaisquer: ')

valores = list ()
linha = ('-'*30)

while True:
    print (linha)
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print ('\033[1;32mValor registrado!\033[m')
    else:
        print ('\033[1;31mValor já existe!\033[m\nTente Novamente.')
    print (linha)

    continuar = str(input('\033[1mDeseja adicionar mais números [S/N]?\033[m ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Escolha inválida.\nDigite [N] para NÃO ou [S] para SIM: ')).strip().upper()[0]
    if continuar == 'N':
        print ('Cadastro encerrado.')
        break

print (linha)
print ('Resultado: ')
print (f'\033[7m{sorted(valores)}\033[m')
