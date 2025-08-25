# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 78 ##')
print ()
print ('=== GUARDANDO VALORES ===')
print ('A seguir, digite 5 valores inteiros quaisquer: \n')
valores = list ()

for x in range (1,6):
    valores.append(int(input(f'Digite o {x}° valor: ')))

print ()
print ('-'*20)
print (f'Lista: \033[7m{valores}\033[m')
print ('-'*20)

maior = max(valores)
menor = min(valores)

print ()
print (f'\033[1;36mMAIOR:\033[m {maior}')
print (f'Quantidade de Aparições: {valores.count (maior)}')
print (f'Posição: ', end ='')
for i, v in enumerate(valores):
    if v == maior:
        print (f'{i+1}° ', end ='')

print ()
print('-'*10)

print(f'\033[1;36mMENOR:\033[m {menor}')
print (f'Quantidade de Aparições: {valores.count (menor)}')
print (f'Posição: ', end ='')
for i, v in enumerate(valores):
    if v == menor:
        print (f'{i+1}° ', end =' ')
