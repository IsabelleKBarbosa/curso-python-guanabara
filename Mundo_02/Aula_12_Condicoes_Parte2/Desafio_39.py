#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar,
# Se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 39 ##')
print ()
print ('=== PRAZO - ALISTAMENTO MILITAR ===')
print ('Atenção: Deve ocorrer no PRIMEIRO SEMESTRE do ano em que se completa 18 anos.\n')
nascimento = int (input('Digite o ano de nascimento: '))
print ()
anoatual = date.today().year
idade = anoatual - nascimento
if idade == 18:
    print ('Prazo de Alistamento: \033[7;32;40mEXATO!\033[m\n'
           'Deve-se alistar esse ano!')
elif idade < 18:
    falta = 18 - idade
    print ('Prazo de Alistamento: \033[7;33mINDISPONÍVEL!\033[m\n'
           f'Idade Atual: {idade} anos\n'
           f'Tempo até alistamento: {falta} anos\n'
           f'Alistamento deve ser feito em: {anoatual + falta} ')
else:
   atraso = idade - 18
   passado = anoatual - atraso
   print ('Prazo de Alistamento: \033[7;31mATRASADO!\033[m\n'
          f'O alistamento deveria ter sido realizado no ano de: {passado}\n'
          f'Tempo de atraso: {atraso} anos.\n'
          '\033[33mEntre em contato imediatamente.\033[m')

