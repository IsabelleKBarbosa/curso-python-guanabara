# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 77 ##')
print ()
print ('=== CONTAGEM DE VOGAIS ===\n')

lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR')

for palavra in lista:
    print (f'Vogais de {palavra}: ', end = '')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print ()
