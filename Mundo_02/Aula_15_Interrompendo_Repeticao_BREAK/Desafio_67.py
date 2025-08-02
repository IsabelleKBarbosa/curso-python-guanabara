#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 67 ##')
print ()
print ('=== MÚLTIPLAS TABUADAS ===')
print ('Atenção: O programa será interrompido quando for digitado um \033[31mnúmero negativo\033[m.\n')
n = 0
linha = '\033[1;32m'
off = '\033[m'
while True:
    n = int(input('Digite o número para conferir a respectiva tabuada: '))
    print(f'{linha}-{off}' * 50)
    if n < 0:
        break
    print (f'\033[7mTABUADA DE {n}{off}')
    for cont in range (0,11):
        print (f'{cont} x {n} = {cont*n}')
    print (f'{linha}={off}'*50)
print ('Programa Encerrado')
