#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
print ('_____________________________________________________________________')
print ()
print ('## ATIVIDADE PRÁTICA - 22 ##')
print ()
nome = str (input('Digite seu nome completo: '))
print ()
print ('--> Confira o nome com duas configurações diferentes:')
print (nome.upper())
print (nome.lower() + '\n')
print ('--> Contagem: ')
print (f'Total de letras: {len(nome)}')
nospace = nome.replace(" ", "")
print(f'Tamanho sem considerar os espaços: {len(nospace)}')
print (f'O primeiro nome é: {(nome.split()[0])}')
print (f'Total de letras apenas no primeiro nome: {len(nome.split()[0])}')
