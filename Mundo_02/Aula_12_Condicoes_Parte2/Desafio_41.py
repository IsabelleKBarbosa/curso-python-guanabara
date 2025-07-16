#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from datetime import date
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 41 ##')
print ()
print ('== CATEGORIA DE ACORDO COM IDADE ==')
print ('Para calcular, conforme regulamento, a categoria do(a) atleta, forneça:\n')
nasc = int (input('Digite o ano de nascimento: ').strip())
idade = date.today ().year - nasc
print ()
print (f'IDADE: {idade} anos')
if idade <= 9:
    print (f'Categoria: MIRIM')
elif 9 < idade < 15:
    print ('Categoria: INFANTIL')
elif 14 < idade < 20:
    print ('Categoria: JÚNIOR')
elif 19 < idade < 26:
    print ('Categoria: SÊNIOR')
elif idade > 25:
    print ('Categoria: MASTER')

